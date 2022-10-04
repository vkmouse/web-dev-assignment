function handleNavbarTogglerClick(element) {
  const parent = element.parentElement;
  element = parent.querySelector('.navbar__nav');
  if (element.style.display !== "flex") {
    element.style.display = "flex";
  } else {
    element.style.display = "";
  }
}

function handleStarClick(element) {
  if (element.classList.contains("star--active")) {
    element.classList.remove("star--active");
  } else {
    element.classList.add("star--active");
  }
}
