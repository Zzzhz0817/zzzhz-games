#!/usr/bin/env python3
"""
Steam Trailer Downloader
从 Steam 商店页面提取并下载 trailer 视频（包括顶部大视频）

依赖安装:
    pip install requests yt-dlp
    # 还需要安装 ffmpeg (用于合并音视频流)
    # macOS: brew install ffmpeg
    # Ubuntu: sudo apt install ffmpeg
    # Windows: choco install ffmpeg

使用方法:
    python steam_trailer_download.py
    # 或指定URL:
    python steam_trailer_download.py --url "https://store.steampowered.com/app/3128590/Right_Click_To_Activate_Translator/"
"""

import re
import json
import argparse
import subprocess
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ 缺少 requests 库，请运行: pip install requests")
    sys.exit(1)


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

DEFAULT_URL = "https://store.steampowered.com/app/3128590/Right_Click_To_Activate_Translator/"


def get_page_html(url: str) -> str:
    """获取 Steam 商店页面 HTML"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "birthtime=0; wants_mature_content=1; lastagecheckage=1-0-1990;",
    }
    print(f"📥 正在获取页面: {url}")
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def extract_trailer_manifests(html: str) -> list[dict]:
    """
    从页面 HTML 中提取 trailer 的 DASH manifest URL。
    Steam 页面中 trailer 数据通常嵌在 JavaScript 变量里，
    格式类似: "webm": {...}, "mp4": {...}, 或者在 data-webm-source / rgMovieFlashvars 中。
    """
    trailers = []

    # 方法1: 查找 rgMovieFlashvars 或类似的 JSON 数据块
    # Steam 通常在页面中嵌入类似这样的结构:
    # var rgMovieFlashvars = { "MOVIE_ID": { MOVIE_URL: "...", ... } };
    flashvars_match = re.search(r'var\s+rgMovieFlashvars\s*=\s*(\{.*?\});', html, re.DOTALL)
    if flashvars_match:
        try:
            data = json.loads(flashvars_match.group(1))
            for movie_id, movie_data in data.items():
                trailer_info = {"id": movie_id}
                # 提取 webm/mp4 URL
                if "MOVIE_URL" in movie_data:
                    trailer_info["url"] = movie_data["MOVIE_URL"]
                if "FILENAME" in movie_data:
                    trailer_info["filename"] = movie_data["FILENAME"]
                trailers.append(trailer_info)
            print(f"✅ 方法1 (rgMovieFlashvars): 找到 {len(trailers)} 个 trailer")
        except json.JSONDecodeError:
            print("⚠️  方法1: JSON 解析失败，尝试其他方法...")

    # 方法2: 查找 DASH manifest URL (video.fastly.steamstatic.com/store_trailers/...)
    dash_urls = re.findall(
        r'(https?://video\.fastly\.steamstatic\.com/store_trailers/[^\s"\'<>]+\.mpd[^\s"\'<>]*)',
        html
    )
    if dash_urls:
        for url in set(dash_urls):
            trailers.append({"type": "dash_manifest", "url": url})
        print(f"✅ 方法2 (DASH manifest): 找到 {len(dash_urls)} 个 manifest URL")

    # 方法3: 查找 webm/mp4 直接链接 (cdn.akamai.steamstatic.com 或 video.fastly...)
    webm_urls = re.findall(
        r'(https?://(?:cdn\.akamai|video\.fastly|shared\.fastly)\.steamstatic\.com/[^\s"\'<>]+?(?:movie[^\s"\'<>]*?\.(?:webm|mp4))[^\s"\'<>]*)',
        html
    )
    if webm_urls:
        for url in set(webm_urls):
            trailers.append({"type": "direct_video", "url": url})
        print(f"✅ 方法3 (直接视频链接): 找到 {len(webm_urls)} 个")

    # 方法4: 查找 data-webm-source 属性
    webm_source = re.findall(r'data-webm-source="([^"]+)"', html)
    if webm_source:
        for url in set(webm_source):
            trailers.append({"type": "webm_source", "url": url})
        print(f"✅ 方法4 (data-webm-source): 找到 {len(webm_source)} 个")

    # 方法5: 查找 SteamVideoPlayer 相关的 JSON 配置
    video_config = re.findall(
        r'(https?://[^\s"\'<>]+store_trailers[^\s"\'<>]+)',
        html
    )
    if video_config:
        for url in set(video_config):
            if url not in [t.get("url") for t in trailers]:
                trailers.append({"type": "store_trailer", "url": url})
        print(f"✅ 方法5 (store_trailers): 找到 {len(video_config)} 个")

    # 方法6: 同时提取 About 区域的内嵌 webm 视频
    extras_urls = re.findall(
        r'(https?://shared\.fastly\.steamstatic\.com/store_item_assets/steam/apps/\d+/extras/[^\s"\'<>]+\.webm[^\s"\'<>]*)',
        html
    )
    if extras_urls:
        for url in set(extras_urls):
            trailers.append({"type": "extras_video", "url": url})
        print(f"✅ 方法6 (extras 内嵌视频): 找到 {len(extras_urls)} 个")

    # 方法7: 提取图片 (avif/jpg/png)
    img_urls = re.findall(
        r'(https?://shared\.fastly\.steamstatic\.com/store_item_assets/steam/apps/\d+/(?:extras/[^\s"\'<>]+\.(?:avif|jpg|png|gif)|header\.jpg|page_bg_raw\.jpg)[^\s"\'<>]*)',
        html
    )
    if img_urls:
        for url in set(img_urls):
            trailers.append({"type": "image", "url": url})
        print(f"✅ 方法7 (图片): 找到 {len(img_urls)} 个")

    return trailers


def download_with_ytdlp(url: str, output_dir: str, filename_prefix: str = "trailer"):
    """使用 yt-dlp 下载 DASH manifest 视频"""
    output_path = str(Path(output_dir) / f"{filename_prefix}.%(ext)s")
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--output", output_path,
        "--merge-output-format", "mp4",
        url
    ]
    print(f"🎬 使用 yt-dlp 下载: {url[:80]}...")
    try:
        # Avoid character encoding crash on Windows by piping output/error
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✅ 下载完成 -> {output_dir}/")
    except FileNotFoundError:
        print("❌ yt-dlp 未安装，请运行: pip install yt-dlp")
    except subprocess.CalledProcessError as e:
        print(f"❌ yt-dlp 下载失败: {e.stderr.decode('utf-8', errors='ignore')}")


def download_direct(url: str, output_dir: str, filename: str = None):
    """直接下载文件"""
    if not filename:
        # 从 URL 中提取文件名
        filename = url.split("/")[-1].split("?")[0]
    filepath = Path(output_dir) / filename
    if filepath.exists():
        print(f"⏭️  已存在，跳过: {filename}")
        return

    print(f"📥 下载: {filename}")
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=60, stream=True)
    resp.raise_for_status()

    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    size_mb = filepath.stat().st_size / (1024 * 1024)
    print(f"✅ 已保存: {filepath} ({size_mb:.1f} MB)")


def main():
    # Force utf-8 stdout on windows to prevent crash
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(description="Steam Trailer Downloader")
    parser.add_argument("--url", default=DEFAULT_URL, help="Steam 商店页面 URL")
    parser.add_argument("--output", default="downloads", help="输出目录 (默认: downloads)")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "videos").mkdir(exist_ok=True)
    (output_dir / "images").mkdir(exist_ok=True)

    # 1. 获取页面
    html = get_page_html(args.url)

    # 2. 提取所有媒体链接
    media = extract_trailer_manifests(html)

    if not media:
        print("❌ 未找到任何媒体资源。")
        print("💡 提示: Steam trailer 视频可能通过 JavaScript 动态加载。")
        print("   可以尝试:")
        print("   1. 在浏览器中打开页面 -> F12 -> Network -> 播放视频")
        print("   2. 筛选 .mpd 请求，复制 URL")
        print("   3. 运行: yt-dlp \"粘贴URL\"")
        return

    # 3. 分类下载
    print(f"\n{'='*60}")
    print(f"共找到 {len(media)} 个媒体资源，开始下载...")
    print(f"{'='*60}\n")

    dash_count = 0
    for item in media:
        item_type = item.get("type", "unknown")
        url = item.get("url", "")

        if not url:
            continue

        if item_type == "dash_manifest":
            dash_count += 1
            download_with_ytdlp(url, str(output_dir / "videos"), f"trailer_{dash_count}")

        elif item_type in ("direct_video", "webm_source", "extras_video", "store_trailer"):
            download_direct(url, str(output_dir / "videos"))

        elif item_type == "image":
            download_direct(url, str(output_dir / "images"))

    # 4. 打印摘要
    print(f"\n{'='*60}")
    print("📦 下载完成！")
    print(f"   视频目录: {output_dir / 'videos'}")
    print(f"   图片目录: {output_dir / 'images'}")
    print(f"{'='*60}")

    # 额外提示
    print("\n💡 如果顶部大 trailer 视频没有被提取到（DASH manifest），请:")
    print("   1. 浏览器打开页面 -> F12 -> Network 标签")
    print("   2. 播放顶部视频")
    print("   3. 在 Network 中搜索 '.mpd'")
    print("   4. 复制完整 URL，然后运行:")
    print('   yt-dlp "粘贴的URL" -o "downloads/videos/main_trailer.%(ext)s" --merge-output-format mp4')


if __name__ == "__main__":
    main()


    # https://store.steampowered.com/app/3128590/Right_Click_To_Activate_Translator/
    # https://store.steampowered.com/app/2990190/MagiScapes/