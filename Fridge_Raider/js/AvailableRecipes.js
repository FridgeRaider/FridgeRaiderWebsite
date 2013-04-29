document.onload = createTable;

function createRecipeTable() {
    /***
    This function will search for some recipes and fill the recipe table with the results.
    This function should be called on page load and when the query string has been changed.
    ***/
    // Get random ingredients
	var searchbox = document.getElementById('availableRecipeSearch');
    var search  = { ingredientList: GetIngredients(), query: searchbox.value};
    // Search for Recipes
    GetRecipe(search);
}

function GetIngredients() {
    // Get 3 random ingredients
    return [
        {
            ingredientName: "Flour"
        }, {
            ingredientName: "milk"
        }, {
            ingredientName: "eggs"
        }
    ];
}

function fillRecipeTable(data) {
    /***
    This function will fill the recipe table based on the api results. Each 
    row of the table will have a thumbnail, a link to the recipe, and a list of
    the ingredients in the recipe.
    ***/
    $.each(data.results, function (i, item) {
        var table = document.getElementById("recipeTable").getElementsByTagName('tbody');
        table.empty();
        var newRow = table.insertRow(-1);
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);
        // A thumbnail image for the recipe
        cell1.innerHTML = "<img src='" + item.thumbnail + "' alt=''>";
        // A link to the recipe with the title as the text
        cell2.innerHTML = "<a href='" + item.href + "'>" + item.title + "</a>";
        // A list of ingredients in the recipe
        cell3.innerHTML = item.ingredients;
    });
}

function GetRecipe(args) {
    /***
  This function will take a list of ingredients that we want to search for. 
	The function will return a a list of objects consisting of a title, link, 
	ingredients, and a thumbnail.
	The function forms the link string then makes an ajax call to get the 
	results of the search.
	***/

    var AjaxCallArgs = { url: FormURL(args)};

    CallURL(AjaxCallArgs);
}

function FormURL(args) {
    /***
	This function will for a url link from the arguments given. The link will 
	point to the recipe puppy api for search.
	***/

    var link = "http://www.recipepuppy.com/api/?i=";
    for (var i = 0; i < args.ingredientList.length; i++) {
        link += args.ingredientList[i].ingredientName + ",";
    }
    link = link.substring(0, link.length - 1);

    if (args.query !== null && args.query !== "" && args.query !== 'undefined') {
        link += "&q=" + args.query;
    }
    return link;
}

function CallURL(args) {
    /***
	Makes an ajax get call to the url provided.
	***/
	//alert(args.url);
    $.getJSON(args.url, { format: "jsonp" })
    .done(fillRecipeTable);
}

function ErrorFunction() {
    alert("An error occured during the json call to the recipe api. Please contact and administrator.");
}