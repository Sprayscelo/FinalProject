document.addEventListener(`DOMContentLoaded`, e => {
    CNPJValidator()
})

function CNPJValidator() {
    cnpj = document.querySelector("#costumersDetailsCNPJ")
    cnpj.addEventListener("keydown", e => {
        if (cnpj.value.length > 14 && e.key !== "Backspace") {
            e.preventDefault()
        }
        
    })
}