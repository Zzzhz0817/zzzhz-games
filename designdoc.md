张涵哲 作品集网站 设计文档
Portfolio Website Design Document
zzzhz.games | 手机端优先 | GDC名片扫码场景

目录
1. 设计背景与目标
2. 信息架构总览
3. 首页（Hero + 项目概览）— 中英双语
4. 项目详情页 — 麦琪的花园 MagiScape — 中英双语
5. 项目详情页 — Widget Idle — 中英双语
6. 项目详情页 — 按右键打开翻译器 — 中英双语
7. 关于我 — 中英双语
8. 联系方式
9. 技术规格：双语切换 & 视频交互
10. 视觉设计备注
 
1. 设计背景与目标
使用场景
GDC名片扫码 → 手机浏览器打开。用户可能只有30秒到2分钟的注意力。
核心目标
5秒内传达“我是谁、我做什么、我做得怎么样”。感兴趣的人往下滑看项目详情，最后能一键联系或下载简历。
技术约束
域名：zzzhz.games，部署于GitHub Pages。手机端优先，纵向滑动为主。视频内嵌播放，不跳转外部平台。双语支持（默认英文，自动检测切换）。
受众
游戏行业 HR、主管、制作人。需要同时服务技术向（系统策划、技术策划）和设计向（任务、叙事、关卡）的读者。

2. 信息架构总览
网站分为以下区域，纵向排列，单页滚动：

① 首页（Hero + 项目卡片总览）— 右上角语言切换按钮
② 项目详情页 × 3（点击卡片展开或跳转）
③ 关于我
④ 联系方式

项目排序逻辑：行业经验（麦琪的花园）→ 系统深度（Widget Idle）→ 创意与团队管理（翻译器）。
每个详情页结构：标题区 → 媒体区（仅图片/视频）→ 项目介绍（只写游戏）→ 贡献板块（纯文字，通过视觉设计与项目介绍区分）。
 
3. 首页（Hero + 项目概览）
以下内容按 ZH/EN 双语对照列出。网站实际运行时根据语言设置只显示一种。
名字 + 定位
ZH: 张涵哲
EN: Hanzhe Zhang
ZH: 游戏设计师 | 游戏设计硕士 ’26
EN: Game Designer | MFA in Game Science & Design ’26
关键词标签
ZH: 技术策划 · AI + 游戏 · 系统设计 · 任务与叙事
EN: Technical Design · AI + Games · Systems Design · Quest & Narrative
语言切换按钮
位于首屏右上角，显示“中/EN”，点击切换。覆盖自动检测结果。

项目卡片 1
ZH: 麦琪的花园 MagiScape
EN: MagiScape
ZH: AI生存建造 · GenAI系统策划
EN: AI Survival Builder · GenAI Systems Design

项目卡片 2
ZH: Widget Idle
EN: Widget Idle
ZH: 桌面放置游戏 · 系统设计 & 全栈开发
EN: Desktop Idle Game · Systems Design & Full-Stack Dev

项目卡片 3
ZH: 按右键打开翻译器
EN: Right Click to Open Translator
ZH: CUSGA最佳解谜 · 谜题与叙事设计
EN: Best Puzzle Game, CUSGA 2024 · Puzzle & Narrative Design
 
4. 项目详情页 — 麦琪的花园 MagiScape
标题区
ZH: 麦琪的花园 MagiScape
EN: MagiScape
ZH: LLM驱动的生存建造游戏 | GenAI系统策划（实习）
EN: LLM-Driven Survival Builder | GenAI Systems Design (Internship)
媒体区
PV视频自动播放（静音）→ 左滑查看截图（任务界面、NPC交互、游戏场景）
视频占宽约85%，右侧露出下一张截图的一角作为滑动提示
项目介绍（只写游戏，不提“我”）
ZH: 一款俯视角生存建造游戏。NPC由大语言模型驱动，能记住与玩家的互动历史，根据好感度关系动态生成任务和对话。已上线。
EN: A top-down survival builder where NPCs are powered by large language models. They remember player interactions, build relationships based on favorability, and dynamically generate quests and dialogue. Shipped.

以下为贡献板块，通过视觉设计与上方项目介绍区分，纯文字，不放素材。
ZH
任务框架重构
将原有的一次性任务生成改为模块化架构——把触发条件、交互流程、奖励结构拆分为可组合单元，并引入好感度驱动的任务解锁机制。Beta测试中可玩内容量显著提升。
LLM生成管线设计
设计从世界设定→NPC人设→任务生成→质量校验的完整管线。通过分层prompt注入和世界知识库检索，平衡生成内容的多样性与世界观一致性。
项目管理 & PV制作
管理三次Sprint迭代，协调策划与QA优先级。主导宣传PV全流程，上线一周播放量5万。

EN
Quest Framework Redesign
Restructured the one-shot quest generation into a modular architecture—decomposing triggers, interaction flows, and reward structures into composable units, and introducing a favorability-driven quest unlock system. Playable content volume increased significantly in beta testing.
LLM Pipeline Design
Designed the full generation pipeline from world lore → NPC persona → quest generation → quality validation. Balanced content diversity and world consistency through layered prompt injection and a world knowledge base for retrieval.
Production & PV
Managed three sprint iterations, coordinating design priorities with QA. Led the full promotional video production pipeline (scripting → in-engine VFX → gameplay capture); reached 50K views within one week of release.
 
5. 项目详情页 — Widget Idle
标题区
ZH: Widget Idle
EN: Widget Idle
ZH: 齿轮驱动的桌面放置游戏 | 系统设计 & 全栈开发 | 硕士毕设
EN: Gear-Driven Desktop Idle Game | Systems Design & Full-Stack Dev | MFA Capstone
媒体区
游戏运行视频自动播放（静音）→ 左滑查看截图（齿轮系统、Prestige界面、技能树、桌面Widget）
项目介绍
ZH: 一款以桌面小组件为载体的放置游戏。核心循环建立在齿轮物理系统上——齿轮的大小、转速与啮合关系决定资源产出效率，玩家在手动操作与自动化挂机之间做出策略选择。
EN: An idle game that lives on your desktop as a collection of interactive widgets. The core loop is built on a gear physics system—gear size, speed, and meshing relationships determine resource output efficiency. Players make strategic choices between manual effort and automated idling.

贡献板块（纯文字）
ZH
齿轮经济 & Prestige系统
设计基于物理直觉的资源循环。Prestige重置机制提供meta层策略深度，技能树为不同play style提供差异化build路线。
A/B测试研究
设计三组对照实验（无反馈/基础/丰富），基于自我决定理论（SDT）框架，研究视听反馈如何影响玩家在“手动vs挂机”之间的决策倾向。
独立全栈开发
React + TypeScript + Electron，从系统设计到前端实现独立完成。

EN
Gear Economy & Prestige System
Designed a resource loop grounded in physical intuition. The Prestige reset mechanic adds meta-level strategic depth, while the skill tree offers differentiated build paths for different play styles.
A/B Testing Research
Designed a three-condition experiment (no feedback / basic / rich), grounded in Self-Determination Theory (SDT), studying how audiovisual feedback affects player tendencies between manual effort and idle waiting.
Solo Full-Stack Development
React + TypeScript + Electron. Independently completed everything from systems design to frontend implementation.
 
6. 项目详情页 — 按右键打开翻译器
标题区
ZH: 按右键打开翻译器
EN: Right Click to Open Translator
ZH: 横版语言解谜冒险 | 谜题与叙事设计 | CUSGA 2024 最佳解谜游戏
EN: Side-Scrolling Language Puzzle Adventure | Puzzle & Narrative Design | Best Puzzle Game, CUSGA 2024
媒体区
游戏trailer或实机视频自动播放（静音）→ 左滑查看截图（解谜界面、语言系统、场景美术）
项目介绍
ZH: 一款围绕破译虚构语言展开的横版解谜冒险游戏。玩家在探索中逐步发现词汇和语法规则，通过“学会一门语言”本身来推进解谜与叙事。
EN: A side-scrolling puzzle adventure built around deciphering a fictional language. Players gradually discover vocabulary and grammar rules through exploration, driving both puzzle-solving and narrative progression through the act of learning the language itself.

贡献板块（纯文字）
ZH
语言系统 & 谜题设计
参考自然语言学、构造语言（Toki Pona等）和普遍语法理论，设计服务于谜题的虚构语言体系。核心原则：每个新语法规则的引入即是关卡的核心谜题。
竞品分析 & 迭代测试
分析Chants of Sennaar、Heaven’s Vault等同类作品确定差异化方向。每个谜题经过多轮playtest，根据卡关数据调整难度曲线与提示节奏。
主策划：范围管理与叙事协作
确定项目scope，在资源受限时做关键取舍。编写故事大纲，与文案协作打磨对话和环境叙事。

EN
Language System & Puzzle Design
Designed a fictional language system for puzzle purposes, drawing from natural linguistics, constructed languages (e.g. Toki Pona), and Universal Grammar theory. Core principle: the introduction of each new grammar rule IS the core puzzle of its level.
Competitor Analysis & Iterative Testing
Analyzed comparable titles including Chants of Sennaar and Heaven’s Vault to define our differentiation. Each puzzle went through multiple rounds of playtesting, with difficulty curves and hint pacing adjusted based on player stuck-point data.
Lead Designer: Scope Management & Narrative
Defined project scope and made critical trade-offs under resource constraints. Authored the story outline and collaborated with writers to refine dialogue and environmental storytelling.
 
7. 关于我
ZH
计算机本科，游戏设计硕士（Northeastern University, Game Science & Design ’26），UC Berkeley交换期间学习人工智能与认知科学。

设计上，我关注两个维度：一是基于玩家体验的任务与叙事设计——怎么通过节奏、情境和信息控制让玩家产生特定的情感反应；二是用数学建模和数据分析驱动的系统设计——经济循环、数值平衡、行为预测。CS背景让我能快速搭建原型并独立迭代，用实际的可玩版本来验证和反哺设计判断。

我有LLM内容生成管线的实际项目经验，关注的核心问题是：当AI的行为不完全可控时，系统层面该怎么设计，才能让“不确定性”变成乐趣而不是风险。

我的长期兴趣在于游戏作为一种体验媒介如何塑造人的认知与文化——以及大语言模型和新技术正在怎样改变这个过程。

EN
BS in Computer Science, MFA in Game Science & Design (Northeastern University ’26). Studied AI and cognitive science during an exchange at UC Berkeley.

My design work spans two dimensions: experience-driven quest and narrative design—shaping emotional responses through pacing, context, and information control; and analytically-driven systems design—economic loops, numerical balancing, and behavioral prediction. My CS background lets me rapidly prototype and iterate independently, using playable builds to validate and refine design decisions.

I have hands-on project experience with LLM content generation pipelines. The core question I care about: when AI behavior is not fully controllable, how should we design at the systems level to turn “uncertainty” into delight rather than risk?

My long-term interest lies in how games, as an experiential medium, shape human cognition and culture—and how large language models and emerging technologies are transforming that process.

8. 联系方式
简洁排列，均可点击：

·  邮箱：zzzhz0817@gmail.com
·  LinkedIn：图标 + 链接
·  itch.io：zzzhz.itch.io
·  简历下载：PDF下载按钮
·  GitHub：可选，对TD岗位加分
 
9. 技术规格：双语切换 & 视频交互
双语切换
自动检测
页面加载时读取 navigator.language。以 zh 开头（zh-CN、zh-TW等）切换为中文，其余默认英文。
手动切换
首屏右上角显示“中 / EN”切换按钮。点击后切换全部文字内容，同时将用户选择存入 localStorage 覆盖自动检测结果，下次访问时沉默使用用户上次的选择。
实现方式
所有文本存储在 i18n 对象中（如 lang/en.json 和 lang/zh.json），按语言 key 取值渲染。图片和视频路径也纳入 i18n 管理，需要替换的素材出中英两套。不需要替换的素材（如游戏截图本身没有文字）两语言共用同一份。
注意事项
页面切换时不重新加载，直接替换 DOM 内容。保持当前滚动位置不变。

媒体区视频交互
内嵌播放器
使用原生 HTML5 <video> 标签，不用 YouTube/Bilibili iframe。关闭默认控件（不加 controls 属性），自定义极简操作层：视频中央叠加半透明播放/暂停按钮，点击切换状态。静音播放，无音量控制。
滚动自动播放
使用 Intersection Observer API。视频元素进入视口（50%以上可见）时自动 play()，滑出视口时 pause()。默认 muted（移动端浏览器硬性要求）。
横向滑动轮播
使用 CSS scroll-snap-type: x mandatory 实现横向卡片式滑动。视频卡片宽度约占屏幥85%，右侧露出下一张截图的约15%，作为可滑动的视觉暗示。
滑动提示动画
首次加载时，右侧露出的截图一角叠加一个半透明的左右滑动箭头微动画，看过一次后消失不再出现。
视频与滑动的联动
左滑离开视频时自动 pause()，滑回视频时从当前时间点继续 play()，不重新加载。同样通过 Intersection Observer 监听各卡片的可见性实现。
视频托管与性能
视频压缩到 720p、H.264 MP4，控制在30秒内。GitHub Pages 有仓库容量限制，若视频较多/较大，可考虑外部 CDN（如 Cloudflare R2）托管，页面中只引用链接。

10. 视觉设计备注
布局
手机端优先，纵向堆叠。项目卡片点击展开详情或跳转锡点位置。避免横向滚动（媒体区左右滑动除外）。
媒体区
只在媒体区集中放置图片和视频。下方贡献板块为纯文字，不内嵌素材。
信息层级与视觉区分
项目介绍与贡献板块之间通过视觉设计区分（如不同背景色、缩进、分隔线等），不使用显式标题。
总体节奏
控制在4–5屏内完成全部浏览。
