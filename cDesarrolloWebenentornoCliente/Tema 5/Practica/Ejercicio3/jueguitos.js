function search() {
    let input
    let filter 
    let games
    let game
    let title;
    let noResultsDisplay;
    let noResultsElement = document.getElementById('no-results-message');

    input = document.getElementById('input');
    filter = input.value.toUpperCase();
    games = document.getElementById('game-container').getElementsByClassName('game');

    let noResultsCount = 0;

    for (let i = 0; i < games.length; i++) {
        game = games[i];
        title = game.getElementsByClassName('game-title')[0];

        if (title.innerHTML.toUpperCase().indexOf(filter) > -1) {
            game.style.display = "";
        } else {
            game.style.display = "none";
            noResultsCount++;
        }
    }

    if (!noResultsElement) {
        noResultsElement = document.createElement("div");
        noResultsElement.innerHTML = "Lo sentimos, no hemos podido encontrar el juego que buscas.";
        noResultsElement.id = "no-results-message";
        noResultsElement.style.display = "none";
        document.getElementById('game-container').appendChild(noResultsElement);
    }
    if (noResultsCount === games.length) {
        noResultsDisplay = "block";
    } else {
        noResultsDisplay = "none";
    }
    noResultsElement.style.display = noResultsDisplay;
    
}
