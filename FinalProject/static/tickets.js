document.addEventListener("DOMContentLoaded", e => {
    let options = document.querySelectorAll("option")
    for (valor of options) {
        valor.addEventListener(`click`, e => {
            newTicket(e.target)
        })
    }
    // document.querySelectorAll("option").addEventListener("click", e => {
    //     newTicket(e.target)
    // })
})

function statusSelected(id){
    let inputStatus = document.querySelectorAll(`#${id}`)
    inputStatus.forEach(statusTicket => {
        if(statusTicket.dataset.status === statusTicket.innerText) {
            statusTicket.style.backgroundColor = "#6C757D"
            statusTicket.style.color = "white"
        }
    });
    
}

function newTicket(element) {
    document.querySelector(".DefaultOption").hidden = true
    let mainFormDiv = document.querySelector(".mainFormDiv")
    let selecionarCategoria = document.querySelector("#newTicketSelectOptions")
    selecionarCategoria.dataset.selected = element.value
    console.log(mainFormDiv.lastElementChild)
    for (select of selecionarCategoria) {
        if(Number(select.value) == Number(selecionarCategoria.dataset.selected)) {
            let ticketOptionsContent = document.querySelector(".newTicketOptionsContent")
            switch(Number(selecionarCategoria.dataset.selected)) {
                case 1:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketAlteracaoPlacaContainer").innerHTML; 
                break

                case 2: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketAlteracaoDescricaoContainer").innerHTML;
                break

                case 3: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketJornadaContainer").innerHTML
                break

                case 4: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketAlteracaoMetaConsumoContainer").innerHTML
                break

                case 5:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketCriacaoUsuarioContainer").innerHTML
                break

                case 6: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketBloqueioUsuarioContainer").innerHTML
                break

                case 7:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketVeiculoComunicacaoContainer").innerHTML
                break
                
                case 8: ticketOptionsContent.innerHTML = document.querySelector("#newTicketTreinamentoContainer").innerHTML
                break
            }
        }
        else{

        }
    }
}
