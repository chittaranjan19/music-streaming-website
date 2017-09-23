var addEvent = function(){return document.addEventListener?function(a,c,d){if(a&&a.nodeName||a===window)a.addEventListener(c,d,!1);else if(a&&a.length)for(var b=0;b<a.length;b++)addEvent(a[b],c,d)}:function(a,c,d){if(a&&a.nodeName||a===window)a.attachEvent("on"+c,function(){return d.call(a,window.event)});else if(a&&a.length)for(var b=0;b<a.length;b++)addEvent(a[b],c,d)}}();

function playSong(songname)
{
	s = songname;
	xhr = new XMLHttpRequest();
	
	xhr.onreadystatechange = showAudio;
	
	console.log("inplaysong s="+s);
	xhr.open("GET","/static/music/"+songname+".mp3",true);
	//xhr.open("GET", "static/music/Paradise.mp3")
	xhr.responseType = "blob";
	xhr.send();
}

function showAudio()
{
	if(xhr.readyState == 4 && xhr.status == 200)
	{
		
		data = xhr.response
		
		if(document.getElementById("audio-player"))
		{
			var ap = document.getElementById("audio-player")
			document.body.removeChild(ap);
			
		}
	
		d = document.createElement("audio")
		d.style = "position:fixed;width:100%;bottom:0px;z-index:100;"
		d.id = "audio-player"
		d.autoplay = "autoplay"
		d.controls = "controls"
		d.volume = 0.0
		d.onpause = function(){song.disconnect(); }
		d.onplay = function(){song.connect(); }
		d2 = document.createElement("source")
		d2.id = "audio-source";
		d2.src = window.URL.createObjectURL(data);
		d2.type = "audio/mp3"
		d.appendChild(d2)
		document.body.appendChild(d)
	}
	
}

