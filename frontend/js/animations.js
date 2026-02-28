// animations.js

// Fade in elements on load
function fadeInElements() {
    const elements = document.querySelectorAll(".fade-in");

    elements.forEach((el, index) => {
        el.style.opacity = 0;
        el.style.transform = "translateY(20px)";

        setTimeout(() => {
            el.style.transition = "all 0.6s ease";
            el.style.opacity = 1;
            el.style.transform = "translateY(0)";
        }, index * 150);
    });
}

// Smooth page transition
function smoothNavigation() {
    document.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function (e) {
            if (this.hostname === window.location.hostname) {
                e.preventDefault();
                const target = this.href;

                document.body.style.opacity = 0;
                document.body.style.transition = "opacity 0.3s ease";

                setTimeout(() => {
                    window.location.href = target;
                }, 300);
            }
        });
    });
}

// Loading spinner animation
function showLoader() {
    const loader = document.getElementById("loading");
    if (loader) loader.classList.remove("hidden");
}

function hideLoader() {
    const loader = document.getElementById("loading");
    if (loader) loader.classList.add("hidden");
}

// Button ripple effect
function enableRippleEffect() {
    document.querySelectorAll("button").forEach(button => {
        button.addEventListener("click", function (e) {
            const circle = document.createElement("span");
            circle.classList.add("ripple");
            this.appendChild(circle);

            const d = Math.max(this.clientWidth, this.clientHeight);
            circle.style.width = circle.style.height = d + "px";

            circle.style.left = e.clientX - this.offsetLeft - d / 2 + "px";
            circle.style.top = e.clientY - this.offsetTop - d / 2 + "px";

            setTimeout(() => circle.remove(), 600);
        });
    });
}

// Scroll reveal effect
function scrollReveal() {
    const revealElements = document.querySelectorAll(".reveal");

    window.addEventListener("scroll", () => {
        const windowHeight = window.innerHeight;

        revealElements.forEach(el => {
            const top = el.getBoundingClientRect().top;
            if (top < windowHeight - 100) {
                el.style.opacity = 1;
                el.style.transform = "translateY(0)";
                el.style.transition = "all 0.6s ease";
            }
        });
    });
}

// Initialize all animations
window.addEventListener("DOMContentLoaded", () => {
    fadeInElements();
    smoothNavigation();
    enableRippleEffect();
    scrollReveal();
});