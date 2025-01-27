// Get the elements
const menuIcon = document.getElementById("menu-icon");
const closeIcon = document.getElementById("close-icon");
const mobileNav = document.getElementById("mobile-nav");

// Show menu when the menu icon is clicked
menuIcon.addEventListener("click", () => {
    mobileNav.classList.remove("hidden"); // Show the nav
    menuIcon.classList.add("hidden");    // Hide the menu icon
    closeIcon.classList.remove("hidden"); // Show the close icon
});

// Hide menu when the close icon is clicked
closeIcon.addEventListener("click", () => {
    mobileNav.classList.add("hidden");   // Hide the nav
    menuIcon.classList.remove("hidden"); // Show the menu icon
    closeIcon.classList.add("hidden");   // Hide the close icon
});
