const text = "Transform complex research questions into structured strategic intelligence in minutes.";
let index = 0;

function typeEffect() {
    if (index < text.length) {
        document.getElementById("typing").innerHTML += text.charAt(index);
        index++;
        setTimeout(typeEffect, 30);
    }
}

window.onload = typeEffect;