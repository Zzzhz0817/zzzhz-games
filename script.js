document.addEventListener('DOMContentLoaded', () => {
    initI18n();
    initVideoInteractions();
    initSwipeHints();
});

// i18n Logic
let currentLang = 'en';

function initI18n() {
    const savedLang = localStorage.getItem('preferredLang');
    if (savedLang) {
        currentLang = savedLang;
    } else {
        const browserLang = navigator.language || navigator.userLanguage;
        currentLang = browserLang.toLowerCase().startsWith('zh') ? 'zh' : 'en';
    }
    applyLanguage(currentLang);

    const toggleBtn = document.getElementById('lang-toggle');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            currentLang = currentLang === 'en' ? 'zh' : 'en';
            localStorage.setItem('preferredLang', currentLang);
            applyLanguage(currentLang);
        });
    }
}

function applyLanguage(lang) {
    document.documentElement.lang = lang;
    const dict = i18n[lang];
    if (!dict) return;

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });
}

// Video Interaction Logic
function initVideoInteractions() {
    const videos = document.querySelectorAll('.project-video');
    
    // Intersection Observer for auto-play/pause when scrolling into view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            const mediaItem = video.closest('.media-item');
            
            if (entry.isIntersecting) {
                // Video is visible (at least 50% based on threshold)
                // Using a small timeout to avoid play() interruptions if quickly scrolling
                setTimeout(() => {
                    if (video.paused) {
                        const playPromise = video.play();
                        if (playPromise !== undefined) {
                            playPromise.then(() => {
                                mediaItem.classList.remove('paused');
                                mediaItem.classList.add('playing');
                            }).catch(e => {
                                console.log("Autoplay prevented:", e);
                                mediaItem.classList.add('paused');
                                mediaItem.classList.remove('playing');
                            });
                        }
                    }
                }, 100);
            } else {
                // Video is out of view
                video.pause();
                mediaItem.classList.add('paused');
                mediaItem.classList.remove('playing');
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% visible
    });

    videos.forEach(video => {
        observer.observe(video);
        
        const mediaItem = video.closest('.media-item');
        const overlay = mediaItem.querySelector('.play-pause-overlay');
        
        // Manual play/pause click
        if (overlay) {
            overlay.addEventListener('click', (e) => {
                e.stopPropagation();
                togglePlayPause(video, mediaItem);
            });
        }
        
        // Also allow clicking video itself
        video.addEventListener('click', () => {
            togglePlayPause(video, mediaItem);
        });
    });
}

function togglePlayPause(video, mediaItem) {
    if (video.paused) {
        video.play();
        mediaItem.classList.remove('paused');
        mediaItem.classList.add('playing');
    } else {
        video.pause();
        mediaItem.classList.add('paused');
        mediaItem.classList.remove('playing');
    }
}

// Swipe Hint Logic
function initSwipeHints() {
    const scrollers = document.querySelectorAll('.media-scroller');
    
    scrollers.forEach(scroller => {
        const hint = scroller.parentElement.querySelector('.swipe-hint');
        if (!hint) return;

        let hasScrolled = false;
        
        scroller.addEventListener('scroll', () => {
            if (!hasScrolled && scroller.scrollLeft > 20) {
                hasScrolled = true;
                hint.classList.add('hidden');
                localStorage.setItem('hasSeenSwipeHint', 'true');
            }
        });

        // If globally seen, hide immediately
        if (localStorage.getItem('hasSeenSwipeHint') === 'true') {
            hint.classList.add('hidden');
        }
    });
}
