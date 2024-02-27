
let barra = document.getElementsByClassName("barra")[0];



function scroll() {
    let body_max = document.body.offsetHeight;
    let window_max = window.innerHeight;
    let scrollmax = body_max - window_max;

    let scroll_actual = (window.scrollY / scrollmax) * 100;

    barra.style.width = scroll_actual + "%";
    console.log(window.scrollY);
    console.log(scrollmax);

    console.log(scroll_actual);

    if (scroll_actual < 16) {
        barra.style.background = "red"
    }else if(scroll_actual > 17 && scroll_actual < 33){
        barra.style.background = "orange"
    }else if(scroll_actual > 33 && scroll_actual < 50){
        barra.style.background = "yellow"
    }else if(scroll_actual > 50 && scroll_actual < 67){
        barra.style.background = "green"
    }else if(scroll_actual > 67 && scroll_actual < 84){
        barra.style.background = "blue"
    }else if(scroll_actual > 84 && scroll_actual < 100){
        barra.style.background = "purple"
    }
}