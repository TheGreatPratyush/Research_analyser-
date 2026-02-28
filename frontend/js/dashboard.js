async function analyze() {
    const question = document.getElementById("question").value;

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({question})
    });

    const data = await response.json();

    document.getElementById("summary").innerText = data.report;
    document.getElementById("report").innerText = data.report;

    document.getElementById("confidence").innerText = "75%";
    document.getElementById("credibility").innerText = "82%";
    document.getElementById("volatility").innerText = "Moderate";
    document.getElementById("trend").innerText = "Strong Growth";

    renderChart();
}

function renderChart() {
    new Chart(document.getElementById("chart"), {
        type: "bar",
        data: {
            labels: ["Confidence","Credibility"],
            datasets: [{
                data: [75,82],
                backgroundColor:["#3b82f6","#10b981"]
            }]
        }
    });
}

function showTab(tab) {
    document.querySelectorAll(".tab").forEach(t=>t.classList.add("hidden"));
    document.getElementById(tab).classList.remove("hidden");
}