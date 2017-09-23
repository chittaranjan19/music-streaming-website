var Suggest = function()
{

	temp=this;		
	this.timer=null;
	this.search=null;
	this.xhr=new XMLHttpRequest();

	this.getMusic=function(){

	if(this.timer){
	
		clearTimeout(this.timer);
	}

	this.timer=setTimeout(this.sendTerm,300);
	
}


this.sendTerm=function()
{
	//window.location.reload();
	temp.search=document.getElementById("search");
	url="/submissionthrottling?term="+temp.search.value;
	//console.log(this);
	//console.log(temp);
	
	temp.container = document.getElementById("container");
	temp.container.innerHTML="";
	temp.container.style.display="none";
	//Empty?
	if(temp.search.value==""){
		console.log("Empty String.\n");
		document.getElementById("container").innerHTML = "";
		document.getElementById("search").style.backgroundColor="white";
	}
	else {
		//Cache?
		if(localStorage.getItem(url))
		{
		//Send
			//console.log("In Cache.\n");
			var r = JSON.parse(localStorage.getItem(url));
			temp.populateMusic(r);
		}
		else
		{
		temp.xhr.onreadystatechange=temp.fetchMusic;
		temp.xhr.open("GET", url, true);
		temp.xhr.send();
		}
	}
		

}
this.fetchMusic=function(){
	if(this.readyState==4 && this.status==200){
				//console.log(this.responseText);
				localStorage.setItem(this.responseURL,this.responseText);
				music=JSON.parse(this.responseText);
				
				if (music.length==0)
				{
					//console.log("here");
					document.getElementById("search").style.backgroundColor="gray";
				}
				temp.populateMusic(music);
				//console.log(music.length);
			}
}
this.populateMusic=function(music){

				//console.log(music.length);
				for(var i=0;i<music.length;i++)
				{
					//console.log(music[i]);
					document.getElementById("search").style.backgroundColor="white";
					d = document.createElement("div");
					d.className = "i";
					d.innerHTML = music[i]+"\n";
					temp.container.style.display="block";
					temp.container.appendChild(d);
					d.onclick=temp.setMusic2;
					d.onmouseover = temp.setMusic;
				}

}
this.setMusic=function(e){
	temp.search.value = e.target.innerHTML;
	//temp.container.style.display="none";
	document.getElementById("search").style.display="block";
	document.getElementById("search").value = temp.search.value;
	//document.getElementById("searchform").submit();
}		
this.setMusic2=function(e){
	temp.search.value = e.target.innerHTML;
	//temp.container.style.display="none";
	document.getElementById("search").style.display="block";
	document.getElementById("search").value = temp.search.value;
	document.getElementById("searchform").submit();
}		
		
}
		
obj=new Suggest();
