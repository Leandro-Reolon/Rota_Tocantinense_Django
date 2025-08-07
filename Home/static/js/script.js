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

// --- MELHORIAS DE PERFORMANCE E EXPERIÊNCIA DO USUÁRIO ---

// Executa o script quando o conteúdo do HTML estiver completamente carregado
document.addEventListener("DOMContentLoaded", function() {

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
});