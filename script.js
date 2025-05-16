// Change text content dynamically
document.getElementById("change-text-btn").addEventListener("click", () => {
  document.getElementById("dynamic-text").textContent = "The text has been changed!";
});

// Modify CSS styles via JavaScript
document.getElementById("style-btn").addEventListener("click", () => {
  const paragraph = document.getElementById("style-paragraph");
  paragraph.classList.toggle("highlight");
});

// Add or remove an element when a button is clicked
document.getElementById("toggle-element-btn").addEventListener("click", () => {
  const container = document.getElementById("element-container");
  const existing = document.getElementById("new-element");

  if (existing) {
    existing.remove();
  } else {
    const newEl = document.createElement("p");
    newEl.id = "new-element";
    newEl.textContent = "I was added dynamically!";
    container.appendChild(newEl);
  }
});
