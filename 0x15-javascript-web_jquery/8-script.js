/** A script that fetches and lists the title for all movies by using this
 *  + URL: https://swapi-api.alx-tools.com/api/films/?format=json
 *
 *  - All movie titles must be listed in the HTML tag UL#list_movies
 *  - document.querySelector cannot be used
 *  - JQuery API cannot be used
 */
$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(
    ...data.results.map((movie) => `<li>${movie.title}</li>`)
  );
});
