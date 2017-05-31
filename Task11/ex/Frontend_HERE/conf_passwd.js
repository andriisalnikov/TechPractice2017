var passwd = document.getElementById("passwd");
var confpasswd = document.getElementById("confpasswd");


function validatePassword(){
    if(passwd.value != confpasswd.value) {
        confpasswd.setCustomValidity("Passwords Don't Match");
    } else {
        confpasswd.setCustomValidity('');
    }
}
passwd.onchange = validatePassword;
confpasswd.onkeyup = validatePassword;
