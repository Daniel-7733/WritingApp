// ----- Disappearing Text logic ----

document.addEventListener("DOMContentLoaded", () => {
    const box = document.getElementById("box"); // textarea
    const status = document.getElementById("status"); // status paragraph

    // Safety check (helps avoid "null" errors if IDs are wrong)
    if (!box || !status) {
        console.error("Missing #box or #status in HTML.");
        return;
    }

    const TIMEOUT_MS = 5000; // 5 seconds
    let timerId = null;
    let hasStarted = false;

    function setStatus(message) {
        status.textContent = message;
    }

    function stopTimer() {
        if (timerId !== null) {
            clearTimeout(timerId);
            timerId = null;
        }
    }

    function startOrResetTimer() {
        // Only start the "game" after the first real input
        if (!hasStarted) {
            hasStarted = true;
            setStatus("Typing started — keep going!");
        } else {
            setStatus("User is typing...");
        }

        // Reset the countdown
        stopTimer();

        timerId = setTimeout(() => {
            // If there's nothing, don't spam delete message
            if (box.value.trim() === "") {
                setStatus("Start typing to begin…");
                hasStarted = false;
                timerId = null;
                return;
            }

            // Delete the text
            box.value = "";
            setStatus("Stopped for 5 seconds — text deleted!");

            // Optional: notify Flask backend
            fetch("/lose", { method: "POST" }).catch(() => {
                // If server isn't running or route missing, ignore
            });

            // Reset game state (optional)
            hasStarted = false;
            timerId = null;
        }, TIMEOUT_MS);
    }

    // Run when user types, pastes, deletes, etc.
    box.addEventListener("input", startOrResetTimer);

    // Initial message (no timer running yet)
    setStatus("Start typing to begin…");
});
