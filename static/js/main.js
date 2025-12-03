let inactivityTimer;
const timeout = 5000;  // 5 seconds

function resetTimer() {
    clearTimeout(inactivityTimer);

    document.getElementById("status").textContent = "User is typing...";

    inactivityTimer = setTimeout(() => {
        document.getElementById("status").textContent = "Stopped for 5 seconds — text deleted!";

        // DELETE all text
        document.getElementById("box").value = "";

        // Notify backend (optional)
        fetch("/lose", { method: "POST" });
    }, timeout);
}

document.getElementById("box").addEventListener("input", resetTimer);

// Start timer when page loads
resetTimer();
