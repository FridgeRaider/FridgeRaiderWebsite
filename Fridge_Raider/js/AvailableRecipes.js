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
            ingredientName: "chicken"
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
	var table = document.getElementById("recipeTableData");
	table.innerHTML = "";
    $.each(data.results, function (i, item) {
		var newRow = table.insertRow(-1);
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        // A thumbnail image for the recipe
        cell1.innerHTML = "<img src='" + item.thumbnail + "' alt='' width='100' height = '100'>";
        // A link to the recipe with the title as the text
        cell2.innerHTML = "<a href='" + item.href + "' style='color:grey'>" + item.title + "</a>";
		cell2.innerHTML += "<br />" + item.ingredients;
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

var tempscript = null;

function CallURL(args) {
  if (tempscript) return; // a fetch is already in progress
  tempscript = document.createElement("script");
  tempscript.type = "text/javascript";
  tempscript.id = "tempscript";
  tempscript.src = args.url + "&format=json&callback=onFetchComplete&requestid=";
  document.body.appendChild(tempscript);
  // onFetchComplete invoked when finished
}

function onFetchComplete(data) {
  document.body.removeChild(tempscript);
  tempscript = null;
  fillRecipeTable(data);
}
