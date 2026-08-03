const themeButton = document.getElementByID("themeButton")

themeButton.addEventListener("click", function () { 
  document.body.classList.toggle("dark-mode");
});
