
function checkValid()
{

	var name = document.getElementById("username").value;
	if (name != "")
	{
		xhr = new XMLHttpRequest();
		xhr.onreadystatechange = handle;
		xhr.open("GET","/checkValidity/"+name)
		xhr.send()
	}	
}

function handle()
{
	if(xhr.status==200 && xhr.readyState == 4)
	{
		d = document.getElementById("icon")
		if(xhr.responseText == "YES")
		{
			d.innerHTML = "done"
		}
		else
		{
			d.innerHTML = "error"
		}
	}
}

