function doFirst(){
	var login = document.mainform.loginButton.addEventListener("click", saveText, false);
}
function saveText(){
	var usernameText = document.mainform.usr.value;
	var passwordText = document.mainform.pass.value;
	sessionStorage.setItem(usernameText, pass);
}