document.querySelector(".registerTelaInfo").addEventListener(`submit`, e => {
    verificarSenha()
})

function verificarSenha() {
    let senha = document.querySelector(".registerPassword").value
    let confirmarSenha = document.querySelector(".registerConfirmarPassword").value
    console.log(senha, confirmarSenha)
    if(senha !== confirmarSenha) {
        confirmarSenha.style.backgroundcolor = 'red'
        senha.style.backgroundcolor = 'red'
        alert(`Senhas estão diferentes!`)
    }

}