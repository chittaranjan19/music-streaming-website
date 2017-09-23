function submit1()
{
	document.getElementById("hiddensubmit").click();
	//document.getElementById("signupform").submit();
}
function submit2()
{
	document.getElementById("loginform").submit();
}


var whiteBox = document.getElementById('white-box')

var showLoginBtn = document.getElementById('show-login')
var loginForm = document.getElementById('login-form')
var loginInfo = document.getElementById('login-info')

var showSignupBtn = document.getElementById('show-signup')
var signupForm = document.getElementById('signup-form')
var signupInfo = document.getElementById('signup-info')

showLoginBtn.addEventListener('click', showLogin)
showSignupBtn.addEventListener('click', showSignup)

function showLogin() {
  whiteBox.classList.remove('slide-right')
  whiteBox.classList.add('slide-left')
  
  signupForm.classList.add('hidden')
  signupInfo.classList.remove('hidden')
  
  loginForm.classList.remove('hidden')
  loginInfo.classList.add('hidden')
  
}

function showSignup() {
  whiteBox.classList.remove('slide-left')
  whiteBox.classList.add('slide-right')
  
  signupForm.classList.remove('hidden')
  signupInfo.classList.add('hidden')
  
  loginForm.classList.add('hidden')
  loginInfo.classList.remove('hidden')


}














