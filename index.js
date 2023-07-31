/**************************************
TITLE: index.js							
AUTHOR: Malik Falana (MF)			
CREATE DATE: 07/29/2023	
PURPOSE: To use jquery and functions for index page
LAST MODIFIED ON: 07/29/2023
LAST MODIFIED BY: Malik Falana (MF)
MODIFICATION HISTORY:
07/29/2023: Original Build
***************************************/
//import getRecentGames from './intrests.js';
//import {getRecentGames, createGame} from './intrests.js';

$(document).ready(function() 
{
    const gen = ["I", "II", "III"]; // Playable Nintendo Systems

    var games = [] //

    function selectGame() // Selects playlist to convert
    {
        const selectedOption = $("#Game").val();

        console.log(`Selected Playlist: ${selectedOption}`);
    
        const source = games.find(item => item.id == selectedOption); // where selectedOption is the value of id in playlists array, set source to the playlist object

        //console.log(`Playlist: ${source.title}`); // Log the title of the playlist

        /*

        var html = `<div class = "card card${source.id}">`;
        html += `<div class="container">`;
        html += `<img src=${source.image} alt=${source.id}>`;
        html += `</div>`;
        html += `<div class="details">`;
        html += `<h3>${source.title}</h3>`;
        html += `<p>${source.description}</p>`;
        html += `</div>`;
        html += `</div>`;
        $("#Assignments div.master").html(html); //Append to Intrests Section

        return source;
        */
    }

    function renderGraphics()
    {
        for(var i = 0; i < gen.length; i++) // Populates Dropdown Menu for Source
        {
            var html = `<option value=${gen[i]}>Gen ${gen[i]}</option>`;
            $("#Gen").append(html);
        }
    }

    function fetchGames(Gen) 
    {
        //const url = `http://127.0.0.1:5000/Gen/${Gen}`; // Url to test on local server

        const url = `https://pokepal.vercel.app/Gen/${Gen}`; // Url to test on vercel server

        console.log(`URL: ${url}`);

        return new Promise(function (resolve, reject) 
        {
            $.getJSON(url, function (data) {
            resolve(data);
            }).fail(function (error) {
            reject(error);
            });
        });
    }

    async function Start() 
    {
        try 
        {
            var selectedGen = $("#Gen").val();

            console.log(`Platform: ${selectedGen}`);

            const data = await fetchGames(selectedGen);

            games.push(...data.Games); // Push the fetched data directly to the games array
        
            populateMenu(); // Use the games data here or perform further actions
        
        } 
        catch (error) 
        {
            console.error('Error fetching data:', error);
        }
    }

    function populateMenu() // Populates Dropdown Menu with Games
    {
        for(var i = 0; i < games.length; i++)
        {
            var source = games[i]; // Grabs game from array
            var game = `<option>${source}</option>`;
            $("#Game").append(game); //populate dropdown menu
            $("#Game").on("change", selectGame); //Not sure if still needed
            
        }
    }

    function updateMenu() // Updates Dropdown Menu for Playlist to convert
    {
        games = [] // Empties array

        $("#Game").empty(); // Empties dropdown menu

        Start() // Restarts function

        populateMenu(); // Populates dropdown menu
    }

    function loadRom() // Loads Rom
    {
        
    }

    renderGraphics() //Populates dropdowns and such

    $("#Gen").on("change", updateMenu) // When selected system changes, change the list of games in the dropdown

    //$("#Game").on("change", updateMenu);

    //Buttons

    

    

});  // end of $(document).ready()