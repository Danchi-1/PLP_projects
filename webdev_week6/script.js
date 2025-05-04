document.addEventListener("DOMContentLoaded", function () {
    const greetings = document.getElementById("greet");
    const nameSpan = document.getElementById("name");

    document.getElementById("background-color").addEventListener("click", function () {
        if (document.body.style.backgroundColor == "black") {
            document.body.style.backgroundColor = "white";
            document.getElementById("background-color").innerHTML = "Black background";
            document.getElementById("background-color").style.border = "2px solid white"
        } else {
            document.body.style.backgroundColor = "black";
            document.getElementById("background-color").innerHTML = "White background";
            document.getElementById("background-color").style.border = "2px solid black"
        }
    });

    const name = prompt("Please enter your name:");
    if (name && name.trim() !== "") {
        nameSpan.innerHTML = name;
    } else {
            nameSpan.innerHTML = "Guest";
    }

    const gibberish = document.getElementById("jargons");
    document.getElementById("hide").addEventListener("click", function () {
        if (gibberish.style.display == "none"){
            gibberish.style.display = "block";
        } else {
            gibberish.style.display = "none";
            document.getElementById("hide").innerHTML = "Show Jargons";
        }
    })
});
