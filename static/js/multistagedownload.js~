function getImage(){
	console.log("getImage called")
	xhr = new XMLHttpRequest();	
	if(xhr)
	{
		xhr.onreadystatechange = getLoadingImage;
		xhr.open("GET", "/static/imageLink/loading.txt", true);
		xhr.send(null);
	}	
}
function getLoadingImage(){
	if(xhr.readyState=="4"&&xhr.status==200){
		var loadIm=xhr.responseText;
		document.getElementById("imgAlb").innerHTML=loadIm;
		setTimeout(getContent, 3000);
	}	
}
function getContent(){
	console.log("in getContent");
	xhr.open("GET", "/static/imageLink/"+songnm+".txt", true);
	xhr.onreadystatechange = showContent;
	xhr.send(null);
}
function showContent(){
	if(xhr.readyState=="4"&&xhr.status==200){
		var content=xhr.responseText;
		document.getElementById("imgAlb").innerHTML=content;
			
	}
}
