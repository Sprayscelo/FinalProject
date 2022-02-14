// GET CSRF TOKEN VIA JAVASCRIPT

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/* -----  */

document.addEventListener("DOMContentLoaded", e => {
    let classChanger = document.querySelectorAll("input")
    let statusIDs = ["serviceOrderDetailsStatus", "ticketDetailstStatus"]
    for (sts of statusIDs) {
        statusSelected(sts)
    }
    
    let allTicketStatus = document.querySelectorAll("#ticketDetailstStatus")
    let allServiceOrderStatus = document.querySelectorAll("#serviceOrderDetailsStatus")
    let allStatus = [allTicketStatus, allServiceOrderStatus]

    for (i of allStatus) {
        i.forEach(element => {
            element.addEventListener("click", e => {
                fetch(``, {
                    method: "PUT",
                    body: JSON.stringify({
                        element: element.id,
                        newStatus: e.target.innerText
                    }),
                    headers: {"X-CSRFToken" : csrftoken}
                }).then(response => {
                    e.target.style.backgroundColor = "#6C757D"
                    e.target.style.color = "white"
                    location.reload()
                    switch(element.id) {
                        case "ticketDetailstStatus":
                            console.log(element.id)
                            if (e.target.value != "Closed") {
                                document.querySelector("#ticketDetailsEndDate").value = ""
                            }
            
                            // ----------
            
                            // Setar ticket end date para data de fechamento do ticket
            
                            if(document.querySelector("#ticketDetailsEndDate").value === "" && e.target.innerText === "Closed") {
                                const endDate = new Date()
                                document.querySelector("#ticketDetailsEndDate").value = endDate.toLocaleString("pt-BR", {timezone: "UTC"})
                                
                            }
                            break
                        case "serviceOrderDetailsStatus":
                            
                        }
                    }
                )
            })
        })
    }


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

function transition() {
    const navBarContainer = document.querySelector(".mainNavContainer")
    let menu_icon = document.querySelector(".menu-icon")
    if (navBarContainer.dataset.menu === "closed") {
        navBarContainer.dataset.menu = "open"
        menu_icon.innerText = "segment"
        menu_icon.dataset.status = "open"
    }
    else {
        navBarContainer.dataset.menu = "closed"
        menu_icon.innerText = "menu"
        menu_icon.dataset.status = "closed"
    }
}

