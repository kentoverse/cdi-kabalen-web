// main.js — Marc Cavdada, Assignment 3
document.getElementById("alertBtn").addEventListener("click", () => {
  alert("Hello from Assignment 3 – Marc Cavdada!");
});

document.getElementById("contactForm").addEventListener("submit", e => {
  e.preventDefault();
  alert("Thank you, " + document.getElementById("name").value + "!");
});
