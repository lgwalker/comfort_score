// Function to save user preferences
async function savePreferences() {
    const userPrefs = {
        softness: parseInt(document.getElementById("softness").value),
        breathability: parseInt(document.getElementById("breathability").value),
    };

    await fetch('/set-preferences', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ preferences: userPrefs })
    });
    alert("Preferences saved!");
}

// Function to retrieve and display the comfort score
async function getComfortScore() {
    const response = await fetch('/comfort-score', { method: 'POST' });
    const result = await response.json();
    document.getElementById("scoreDisplay").innerText = 
        result.comfort_score ? `Comfort Score: ${result.comfort_score}` : "Error: Please set preferences first";
}
