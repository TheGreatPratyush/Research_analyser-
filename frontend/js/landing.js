const text = "Transform fragmented information into structured, confidence-scored decision intelligence.";
const typingElement = document.getElementById("typing-text");

let index = 0;

function typeEffect() {
    if (index < text.length) {
        typingElement.innerHTML += text.charAt(index);
        index++;
        setTimeout(typeEffect, 20);
    }
}

window.addEventListener("load", typeEffect);