document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // check local storage for dark mode preference
    if (localStorage.getItem("dark-mode") === "enabled") {
        body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Light Mode";
    }

    toggleButton.addEventListener("click", function () {
        body.classList.toggle("dark-mode");

        // save preference in local storage
        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
            toggleButton.textContent = "☀️ Light Mode";
        } else {
            localStorage.setItem("dark-mode", "disabled");
            toggleButton.textContent = "🌙 Dark Mode";
        }
    });
});