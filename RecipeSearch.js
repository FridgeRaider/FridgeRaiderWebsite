function GetRecipe(args) {
  /***
	This function will take a list of ingredients that we want to search for. 
	The function will return a a list of objects consisting of a title, link, 
	ingredients, and a thumbnail.
	The function forms the link string then makes an ajax call to get the 
	results of the search.
	***/
	
	var AjaxCallArgs;
	AjaxCallArgs.url = FormURL(args.ingredientList);
	
	var results = CallURL(AjaxCallArgs);
	
	return results.results;
}

function FormURL(args){
	/***
	This function will for a url link from the arguments given. The link will 
	point to the recipe puppy api for search.
	***/
	
	var link = "http://www.recipepuppy.com/api/?i="
	for(var i = 0; i < args.ingredientList.length; i++){
		link += args.ingredientList[i] + ",";
	}
	return link;
}

function CallURL(args){
	/***
	Makes an ajax get call to the url provided.
	***/
	
	$.ajax({
		url: args.url,
		type: "GET",
		dataType: "jsonp",
		async:false,
		 success: function (msg) {
			 return json.result;
		},
		error: function () {
			ErrorFunction();
		}
	});
}

function ErrorFunction() {
	alert("An error occured during the json call to the recipe api. Please contact and administrator.");
}
