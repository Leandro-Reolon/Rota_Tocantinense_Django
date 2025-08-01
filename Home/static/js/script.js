function copiarCupom(id) {
    var input = document.getElementById(id);
    input.select();
    input.setSelectionRange(0, 99999); // Para mobile
    document.execCommand("copy");
    alert("Cupom copiado: " + input.value);
}