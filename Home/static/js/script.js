function copiarCupom(id) {
    var input = document.getElementById(id);
    input.select();
    input.setSelectionRange(0, 99999); // Para mobile
    document.execCommand("copy");

    var button = input.nextElementSibling; // Assume que o botão é o próximo irmão do input
    var originalText = button.innerText;
    button.innerText = "Copiado!";
    button.classList.add('btn-success');
    button.classList.remove('btn-outline-primary');

    setTimeout(function() {
        button.innerText = originalText;
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-primary');
    }, 2000); // Volta ao normal após 2 segundos
}

// Botão Voltar ao Topo
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    var backToTopBtn = document.getElementById("backToTopBtn");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
}

function topFunction() {
    window.scrollTo({top: 0, behavior: 'smooth'}); // Rolagem suave
}