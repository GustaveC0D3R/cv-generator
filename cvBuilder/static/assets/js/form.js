function validateForm() {
    var password = document.getElementById("id_password").value;
    var confirmPassword = document.getElementById("id_password_confirm").value;
    if (password != confirmPassword) {
        document.getElementById("password-error").innerText = "Passwords do not match.";
        return false;
    } else {
        passwordError.innerText = "";  // Clear the error message
        return true;
    }
    return true;
}