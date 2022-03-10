


let selectionCat = document.querySelector('#newTicketSelectOptions')

selectionCat.addEventListener('change', e => {
    if (selectionCat.value !== "0") {
        document.querySelector(".Abrir-chamado").hidden = false
    }
    newTicket(e.target)
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
    let selecionarCategoria = document.querySelector("#newTicketSelectOptions")
    selecionarCategoria.dataset.selected = document.querySelector(`.${element.className}`).value
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

                case 8: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketTreinamentoContainer").innerHTML
                break

                case 9:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketProblemasRelatorioContainer").innerHTML
                break
                
                case 10:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketLeituraDeDadosContainer").innerHTML
                break

                case 11:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketProcedimentosInternosContainer").innerHTML
                break
                
                case 12:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketTesteCANContainer").innerHTML
                break

                case 13: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketRegistroPassageiroContainer").innerHTML
                break

                case 14:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketConfiguracaoContainer").innerHTML
                break

                case 15:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketValidacaoEventosContainer").innerHTML
                break

                case 16: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketVeiculoApitandoContainer").innerHTML
                break

                case 17: 
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketAlteracaoEventoContainer").innerHTML
                break

                case 18:
                    ticketOptionsContent.innerHTML = document.querySelector("#newTicketLiberacaoVeiculoContainer").innerHTML
                break
            }
        }
        else{

        }
    }
}

