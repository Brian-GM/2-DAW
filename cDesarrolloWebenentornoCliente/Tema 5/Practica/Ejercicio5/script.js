class Cancion {
    constructor(titulo, artista, genero, duracion, fechaLanzamiento, productor) {
        this.titulo = titulo && titulo.length >= 5 ? titulo : "Sin titulo";
        this.artista = artista && artista.length >= 3 ? artista : "Anonimo";
        this.genero = ["Rock", "Electronica", "Hip-hop", "Jazz", "Country", "Reggae", "Clasica"].includes(genero) ? genero : "Sin genero";
        this.listasReproduccion = [];
        this.duracion = typeof duracion === "number" && duracion > 0 ? duracion : "Indeterminada";
        this.fechaLanzamiento = fechaLanzamiento instanceof Date && !isNaN(fechaLanzamiento.getTime()) ? fechaLanzamiento : new Date();
        this.productor = productor && productor.length >= 3 ? productor : "Sin productor";
    }

    anyadeListaRep(listaRep) {
        this.listasReproduccion.push(listaRep);
    }

    muestraListaRep() {
        console.log("Listas de Reproducción:");
        this.listasReproduccion.forEach(lista => console.log("- " + lista));
    }

    borraListaRep(listaRep) {
        const index = this.listasReproduccion.indexOf(listaRep);
        if (index !== -1) {
            this.listasReproduccion.splice(index, 1);
            console.log("Lista de reproducción borrada:", listaRep);
        } else {
            console.log("La lista de reproducción no existe:", listaRep);
        }
    }
}

class CancionPopular extends Cancion {
    constructor(titulo, artista, genero, duracion, fechaLanzamiento, productor, paisOrigen, festividad) {
        super(titulo, artista, genero, duracion, fechaLanzamiento, productor);
        this.paisOrigen = ["España", "UK", "Francia", "Italia", "Rusia", "Alemania", "Belgica", "Rumania"].includes(paisOrigen) ? paisOrigen : "Indeterminado";
        this.festividad = festividad && festividad.length > 0 ? festividad : "No asociada";
    }
}

const cancionesPopulares = [
    new CancionPopular("Title 1", "Artist 1", "Rock", 180, new Date(2022, 0, 1), "Producer 1", "España", "Fiesta Nacional"),
    new CancionPopular("Title 2", "Artist 2", "Hip-hop", 200, new Date(2022, 3, 15), "Producer 2", "UK", "Carnaval"),
    new CancionPopular("Title 3", "Artist 3", "Electronica", 160, new Date(2022, 6, 30), "Producer 3", "Francia", "Bastille Day"),
    new CancionPopular("Title 4", "Artist 4", "Jazz", 220, new Date(2022, 11, 25), "Producer 4", "Italia", "Ferragosto"),
    new CancionPopular("Title 5", "Artist 5", "Reggae", 240, new Date(2022, 8, 10), "Producer 5", "Rusia", "Día de la Victoria")
];

cancionesPopulares[0].anyadeListaRep("Lista 1");
cancionesPopulares[0].anyadeListaRep("Lista 2");
cancionesPopulares[0].muestraListaRep();
cancionesPopulares[0].borraListaRep("Lista 2");
cancionesPopulares[0].muestraListaRep();
