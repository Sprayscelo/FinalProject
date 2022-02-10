document.addEventListener("DOMContentLoaded", e => {

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
