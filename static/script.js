const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function signin() {
	var email = document.getElementById('lemail').value;
	var pass = document.getElementById('lpass').value;
	$.get("/verify", { email: email, pass: pass }).done(function(resp){
		if(resp == 'success') {
			location.reload();
		}
		else alert("Please check email & password!");
	});
}

function signup() {
	var name = document.getElementById('sname').value;
	var email = document.getElementById('semail').value;
	var pass = document.getElementById('spass').value;
	$.get("/register", { name: name, email: email, pass: pass }).done(function(resp){
		if(resp == 'success') {
			location.reload();
		}
		else alert("Invaild operation!");
	});
}
