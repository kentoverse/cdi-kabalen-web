document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const msg = document.getElementById("message").value.trim();

    if (!name || !email || !msg) {
        document.getElementById("formStatus").innerText = "All fields are required.";
        return;
    }

    document.getElementById("formStatus").innerText = "Message sent!";
});
