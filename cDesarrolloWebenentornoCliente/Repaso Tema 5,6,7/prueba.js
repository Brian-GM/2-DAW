// Array de números enteros (20 números diferentes)
var numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

// Primera función: Sumar 15 unidades a cada número con un retraso de medio segundo por cada número
function sumarQuince() {
    return new Promise(function (resolve, reject) {
        var index = 0;
        var intervalo = setInterval(function () {
            numeros[index] += 15;
            index++;
            if (index === numeros.length) {
                clearInterval(intervalo);
                console.log('+15 a todos los elementos');
                resolve(); // Resuelve la promesa cuando ha terminado de modificar todos los elementos
            }
        }, 500);
    });
}

// Segunda función: Multiplicar cada número por 7 con un retraso general de 1 segundo
function multiplicarPorSiete() {
    return new Promise(function (resolve, reject) {
        setTimeout(function () {
            for (var i = 0; i < numeros.length; i++) {
                numeros[i] *= 7;
            }
            console.log('*7 a todos los elementos');
            resolve(); // Resuelve la promesa cuando ha terminado de modificar todos los elementos
        }, 1000);
    });
}

// Tercera función: Restar 10 unidades a cada número con un retraso de 0.2 segundos por cada número
function restarDiez() {
    return new Promise(function (resolve, reject) {
        var index = 0;
        var intervalo = setInterval(function () {
            numeros[index] -= 10;
            index++;
            if (index === numeros.length) {
                clearInterval(intervalo);
                console.log('-10 a todos los elementos');
                resolve(); // Resuelve la promesa cuando ha terminado de modificar todos los elementos
            }
        }, 200);
    });
}

// Llamada a las funciones usando Promesas
sumarQuince()
    .then(multiplicarPorSiete) // Llama a la siguiente función después de que la primera haya terminado
    .then(restarDiez) // Llama a la siguiente función después de que la segunda haya terminado
    .then(function () { // Finalmente, muestra por consola el array modificado
        console.log(numeros);
    });

    eje
    ejer_sc

    fet