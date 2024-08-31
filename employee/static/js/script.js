// Function to open the login form
function openLoginForm() {
    document.getElementById('loginForm').style.display = 'block';
    localStorage.setItem('isLoginFormOpen', 'true'); // Save state to localStorage
}

// Function to close the login form
function closeLoginForm() {
    document.getElementById('loginForm').style.display = 'none';
    localStorage.setItem('isLoginFormOpen', 'false'); // Save state to localStorage
}

// Check on page load if the form was open
window.onload = function() {
    if (localStorage.getItem('isLoginFormOpen') === 'true') {
        document.getElementById('loginForm').style.display = 'block';
    } else {
        document.getElementById('loginForm').style.display = 'none';
    }
};