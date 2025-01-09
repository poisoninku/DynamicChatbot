document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const userInput = document.querySelector("#user_input");
    const responseDiv = document.querySelector("#response");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const userMessage = userInput.value;
        if (userMessage) {
            const userMessageElement = document.createElement("p");
            userMessageElement.textContent = "You: " + userMessage;
            responseDiv.appendChild(userMessageElement);

            // Simulate a response (this would be a dynamic response in a real app)
            const botResponse = getBotResponse(userMessage);
            const botMessageElement = document.createElement("p");
            botMessageElement.textContent = "Bot: " + botResponse;
            responseDiv.appendChild(botMessageElement);

            // Clear input field
            userInput.value = "";
        }
    });

    function getBotResponse(userMessage) {
        // Simple logic for bot responses
        if (userMessage.toLowerCase().includes("hello")) {
            return "Hi there! How can I help you today?";
        } else if (userMessage.toLowerCase().includes("bye")) {
            return "Goodbye! Have a great day!";
        } else {
            return "Sorry, I don't understand. Can you rephrase?";
        }
    }
});
