document.addEventListener("DOMContentLoaded", () => {
     // Click event
 document.getElementById("click-btn").addEventListener("click", () => {
    alert("You clicked me!");
  });

  // Keypress detection
  document.addEventListener("keydown", (e) => {
    document.getElementById("keypress-output").textContent = `You pressed: ${e.key}`;
  });

  let clicked = false; // Use let instead of const

  // Text and color change
  document.getElementById("change-text").onclick = () => {
      if (!clicked) {
          document.getElementById("text").textContent = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis eum doloremque, libero ratione iste sit et vero suscipit culpa nihil inventore esse voluptatem minima omnis repellendus minus perferendis quaerat optio at ullam magni pariatur cum reprehenderit! Ex voluptatem fugiat possimus excepturi ducimus dolor sed totam, ut sequi praesentium expedita ullam.";
          clicked = true; // Update the state
      } else {
          document.getElementById("text").textContent = "I'm waiting for interaction...";
          clicked = false; // Reset the state
      }
  };


  document.getElementById("change-color").onclick = () => {
    const colors = ["red", "blue", "green", "purple", "orange"];
    let colorIndex = 0;
    let intervalId = null; // Ensure intervalId is properly scoped
    const colorChange = document.getElementById("text");

    // Toggle functionality
    if (intervalId) {
        // If the interval is running, stop it
        clearInterval(intervalId);
        intervalId = null; // Reset the intervalId
    } else {
        // If the interval is not running, start it
        intervalId = setInterval(() => {
            colorChange.style.color = colors[colorIndex];
            colorIndex = (colorIndex + 1) % colors.length; // Cycle through colors
        }, 200); // Change every 200ms
    }
};

  // Accordion
  document.querySelector(".accordion").addEventListener("click", function () {
    const panel = document.querySelector(".panel");
    panel.style.display = panel.style.display === "block" ? "none" : "block";
  });

  // Double-click secret
  document.getElementById("hover-box").addEventListener("dblclick", () => {
    alert("Secret double-click action!");
  });

  // Form validation with real-time feedback
  const username = document.getElementById("username");
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  username.addEventListener("input", () => {
    document.getElementById("user-error").textContent = username.value.trim() === "" ? " Required" : "";
  });

  email.addEventListener("input", () => {
    const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value);
    document.getElementById("email-error").textContent = valid ? "" : " Invalid email";
  });

  password.addEventListener("input", () => {
    document.getElementById("pass-error").textContent = password.value.length >= 8 ? "" : " Min 8 characters";
  });

  document.getElementById("signup-form").addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Form submitted successfully!");
    e.target.reset();
  });
});