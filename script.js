document.getElementById("prediction-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Show the loading screen
    document.getElementById("loading-screen").classList.remove("hidden");
    document.getElementById("main-content").classList.add("hidden");

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        alert(`Predicted Price: ₹${result.predicted_price.toFixed(2)}\nPrice Range: ₹${result.lower_bound.toFixed(2)} - ₹${result.upper_bound.toFixed(2)}`);
    } catch (error) {
        alert("Error occurred while predicting the price.");
    } finally {
        document.getElementById("loading-screen").classList.add("hidden");
        document.getElementById("main-content").classList.remove("hidden");
    }
});
