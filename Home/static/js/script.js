// Função para copiar o código do cupom para a área de transferência
function copiarCupom(id) {
    var input = document.getElementById(id);
    input.select();
    input.setSelectionRange(0, 99999); // Para compatibilidade com dispositivos móveis
    document.execCommand("copy");

    var button = input.nextElementSibling; // Pega o botão que está ao lado do input
    var originalText = button.innerText;
    button.innerText = "Copiado!";
    button.classList.add('btn-success');
    button.classList.remove('btn-outline-primary');

    // Retorna ao texto original depois de 2 segundos
    setTimeout(function() {
        button.innerText = originalText;
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-primary');
    }, 2000);
}

// Função para rolar a página suavemente para o topo (declarada globalmente para ser acessível pelo HTML)
function topFunction() {
    window.scrollTo({top: 0, behavior: 'smooth'}); // Rolagem suave
}

// Executa o script quando o conteúdo do HTML estiver completamente carregado
document.addEventListener("DOMContentLoaded", function() {

    // --- CONTROLE DO CARROSSEL COM VÍDEO ---
    const carouselElement = document.getElementById('mainCarousel');
    const videoElement = document.getElementById('carouselVideo');

    if (carouselElement && videoElement) {
        const carousel = new bootstrap.Carousel(carouselElement, {
            interval: 5000, // Intervalo para slides de imagem
            pause: false
        });

        const handleSlideChange = () => {
            const activeItem = carouselElement.querySelector('.carousel-item.active');

            if (activeItem && activeItem.contains(videoElement)) {
                carousel.pause();
                videoElement.currentTime = 0;
                const playPromise = videoElement.play();
                if (playPromise !== undefined) {
                    playPromise.catch(error => {
                        console.warn("A reprodução automática foi bloqueada. O usuário precisará interagir.");
                        // Se a reprodução falhar, tratamos como uma imagem e avançamos após o intervalo
                        setTimeout(() => carousel.next(), 5000);
                    });
                }
            } else {
                videoElement.pause();
                carousel.cycle();
            }
        };

        videoElement.addEventListener('ended', () => {
            carousel.next();
        });

        carouselElement.addEventListener('slid.bs.carousel', handleSlideChange);

        // Inicia a lógica para o primeiro slide
        handleSlideChange();
    }

    // --- BOTÃO 'VOLTAR AO TOPO' ---
    const backToTopBtn = document.getElementById("backToTopBtn");

    if (backToTopBtn) {
        // Mostra ou esconde o botão baseado na posição da rolagem da página
        window.onscroll = function() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                backToTopBtn.style.display = "block";
            } else {
                backToTopBtn.style.display = "none";
            }
        };
    }

    // --- LAZY LOADING (CARREGAMENTO LENTO) DE IMAGENS ---
    const lazyImages = document.querySelectorAll('img.lazy-load');

    if ("IntersectionObserver" in window) {
        let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    let lazyImage = entry.target;
                    lazyImage.src = lazyImage.dataset.src;
                    lazyImage.classList.remove('lazy-load');
                    lazyImageObserver.unobserve(lazyImage);
                }
            });
        });

        lazyImages.forEach(function(lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    } else {
        // Fallback para navegadores antigos
        lazyImages.forEach(function(lazyImage) {
            lazyImage.src = lazyImage.dataset.src;
            lazyImage.classList.remove('lazy-load');
        });
    }

    // --- ANIMAÇÕES AO ROLAR A PÁGINA ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    if ("IntersectionObserver" in window) {
        let animationObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        animatedElements.forEach(function(element) {
            animationObserver.observe(element);
        });
    } else {
        // Fallback para navegadores antigos
        animatedElements.forEach(function(element) {
            element.classList.add('is-visible');
        });
    }

    // --- LINK ATIVO NA NAVEGAÇÃO ---
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    let currentPath = window.location.pathname;

    // Normaliza o currentPath (remove a barra final, a menos que seja a raiz)
    if (currentPath.endsWith('/') && currentPath.length > 1) {
        currentPath = currentPath.slice(0, -1);
    }

    console.log("Normalized Current Path:", currentPath); // Adicionado para depuração

    navLinks.forEach(link => {
        let linkPath = link.getAttribute('href');

        // Normaliza o linkPath (remove a barra final, a menos que seja a raiz)
        if (linkPath.endsWith('/') && linkPath.length > 1) {
            linkPath = linkPath.slice(0, -1);
        }

        console.log("Normalized Link Path:", linkPath); // Adicionado para depuração

        // Remove a classe 'active' de todos os links primeiro
        link.classList.remove('active');

        // Adiciona a classe 'active' se os caminhos normalizados corresponderem
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
});