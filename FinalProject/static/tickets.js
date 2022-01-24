document.addEventListener("DOMContentLoaded", e => {
    // Mudanca de status via API (PUT)
        // allTicketStatus.forEach(ticketStatus => {
        //     ticketStatus.addEventListener("click", e => {
        //         fetch(``, {
        //             method: "PUT",
        //             body: JSON.stringify({
        //                 newStatus: e.target.innerText
        //             }),
        //             headers: {"X-CSRFToken" : csrftoken}
        //         }).then(response => 
        //             allTicketStatus.forEach(i => {
        //             i.style.backgroundColor = "white"
        //             i.style.color = "#6C757D"
        //             e.target.style.backgroundColor = "#6C757D"
        //             e.target.style.color = "white"
                    
        //         }))
                

                    // Setar ticket end date para NULO
    
                    // if (e.target.value != "Closed") {
                    //     document.querySelector("#ticketDetailsEndDate").value = ""
                    // }
    
                    // // ----------
    
                    // // Setar ticket end date para data de fechamento do ticket
    
                    // if(document.querySelector("#ticketDetailsEndDate").value === "" && e.target.innerText === "Closed") {
                    //     const endDate = new Date()
                    //     document.querySelector("#ticketDetailsEndDate").value = endDate.toLocaleString("pt-BR", {timezone: "UTC"})
                        
                    // }
                    // ----------------
                })
        // })
        /* ------- */ 
        

    // })
   
function statusSelected(id){
    let inputStatus = document.querySelectorAll(`#${id}`)
    inputStatus.forEach(statusTicket => {
        if(statusTicket.dataset.status === statusTicket.innerText) {
            statusTicket.style.backgroundColor = "#6C757D"
            statusTicket.style.color = "white"
        }
    });
    
}

function newComment() {
    // let ticketDetailsID = document.querySelector("#ticketDetailsContainer")
    fetch(``, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            content: commentContent
        })
    })
}
