function Cancion(titulo, artista, genero, duracion, fechaLanzamiento, productor) {
    if (titulo && titulo.length >= 5) {
        this.titulo = titulo;
    } else {
        this.titulo = "Sin titulo";
    }

    if (artista && artista.length >= 3) {
        this.artista = artista;
    } else {
        this.artista = "Anonimo";
    }

    if (["Rock", "Electronica", "Hip-hop", "Jazz", "Country", "Reggae", "Clasica"].includes(genero)) {
        this.genero = genero;
    } else {
        this.genero = "Sin genero";
    }

    this.listasReproduccion = [];
    
    if (typeof duracion === "number" && duracion > 0) {
        this.duracion = duracion;
    } else {
        this.duracion = "Indeterminada";
    }

    if (fechaLanzamiento instanceof Date && !isNaN(fechaLanzamiento.getTime())) {
        this.fechaLanzamiento = fechaLanzamiento;
    } else {
        this.fechaLanzamiento = new Date();
    }

    if (productor && productor.length >= 3) {
        this.productor = productor;
    } else {
        this.productor = "Sin productor";
    }
}

Cancion.prototype.anyadeListaRep = function(listaRep) {
    this.listasReproduccion.push(listaRep);
};

Cancion.prototype.muestraListaRep = function() {
    console.log("Listas de Reproducción:");
    this.listasReproduccion.forEach(lista => console.log("- " + lista));
};

Cancion.prototype.borraListaRep = function(listaRep) {
    const index = this.listasReproduccion.indexOf(listaRep);
    if (index !== -1) {
        this.listasReproduccion.splice(index, 1);
        console.log("Lista de reproducción borrada:", listaRep);
    } else {
        console.log("La lista de reproducción no existe:", listaRep);
    }
};

function CancionPopular(titulo, artista, genero, duracion, fechaLanzamiento, productor, paisOrigen, festividad) {
    Cancion.call(this, titulo, artista, genero, duracion, fechaLanzamiento, productor);

    if (["España", "UK", "Francia", "Italia", "Rusia", "Alemania", "Belgica", "Rumania"].includes(paisOrigen)) {
        this.paisOrigen = paisOrigen;
    } else {
        this.paisOrigen = "Indeterminado";
    }
    
    if (festividad && festividad.length > 0) {
        this.festividad = festividad;
    } else {
        this.festividad = "No asociada";
    }
}

CancionPopular.prototype = Object.create(Cancion.prototype);
CancionPopular.prototype.constructor = CancionPopular;

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
