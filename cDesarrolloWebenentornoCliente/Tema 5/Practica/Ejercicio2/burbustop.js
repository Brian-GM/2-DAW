let bubling_boton = document.getElementById("botBub")
bubling_boton.addEventListener("click",bubbling)

function bubbling(){
    let div = document.getElementById("myDiv")
    let p = document.getElementById("myP")
    
    div.removeEventListener("click",click_div,true)
    p.removeEventListener("click",click_p,true)

    div.addEventListener("click",click_div,false)
    p.addEventListener("click",click_p,false)
    div.querySelector("h2").innerHTML = "EVENTO CLICK: BUBBLING"
    }


let capturing_boton = document.getElementById("botCapt")
capturing_boton.addEventListener("click",capturing)

function capturing(){
    let div = document.getElementById("myDiv")
    let p = document.getElementById("myP")

    div.removeEventListener("click",click_div,false)
    p.removeEventListener("click",click_p,false)

    div.addEventListener("click",click_div,true)
    p.addEventListener("click",click_p,true)
    div.querySelector("h2").innerHTML = "EVENTO CLICK: CAPTURING"
}

let stop_boton = document.getElementById("botStop")
stop_boton.addEventListener("click",stop)

function stop(){

    let div = document.getElementById("myDiv")
    let p = document.getElementById("myP")

    div.removeEventListener("click",click_div,true)
    p.removeEventListener("click",click_p,true)
    div.removeEventListener("click",click_div,false)
    p.removeEventListener("click",click_p,false)
    div.querySelector("h2").innerHTML = "EVENTO CLICK: DESACTIVADO"
}

function click_div(){
    alert("Has hecho clic en el naranja")

}
function click_p(){
    alert("Has hecho clic en el blanco")
}