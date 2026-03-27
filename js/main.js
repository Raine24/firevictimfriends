document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lenis
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // https://www.desmos.com/calculator/brs54l4xou
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 1,
        smoothTouch: false,
        touchMultiplier: 2,
        infinite: false,
    });

    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
    // 1. Sticky Header
    const header = document.querySelector('.site-header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 2. Mobile Menu Toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            // Simple toggle for now, can be expanded with a proper mobile menu overlay
            const isVisible = navLinks.style.display === 'flex';
            navLinks.style.display = isVisible ? 'none' : 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.width = '100%';
            navLinks.style.backgroundColor = 'var(--color-white)';
            navLinks.style.padding = 'var(--spacing-lg) 0';
            navLinks.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
            
            if (!isVisible) {
                // When showing menu, ensure it has a background
                header.classList.add('scrolled');
            }
        });
    }

    // 3. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOptions = {
        threshold: 0.10,
        rootMargin: "50px"
    };
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        let delay = 0;
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('active');
                }, delay);
                delay += 100; // 100ms staggered entrance
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);
    
    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // 4. Parallax Layered Depth effect
    const heroBgs = document.querySelectorAll('.hero-bg');
    const foregroundElements = document.querySelectorAll('.hero-content, .floating-widget');
    
    if (heroBgs.length > 0 || foregroundElements.length > 0) {
        let ticking = false;

        window.addEventListener('scroll', () => {
            const scroll = window.scrollY;
            
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    // Hero background: Scroll speed 0.5x
                    heroBgs.forEach(bg => {
                        let moveBg = scroll * 0.15; // Lower multiplier for natural subtle feel
                        bg.style.transform = `translateY(${moveBg}px) scale(1.05)`;
                    });
                    
                    // Foreground elements: Scroll speed 1.2x
                    foregroundElements.forEach(fg => {
                        let moveFg = scroll * 0.08; 
                        fg.style.transform = `translateY(-${moveFg}px)`;
                    });
                    
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // 5. Hero Slider Auto-Play
    const heroSlides = document.querySelectorAll('.hero-slide');
    if (heroSlides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            heroSlides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % heroSlides.length;
            heroSlides[currentSlide].classList.add('active');
        }, 5000); // 5 seconds per slide transition
    }
});
