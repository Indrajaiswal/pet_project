function toggleChat() {
    var chatContainer = document.getElementById("chat-container");
    chatContainer.style.display = chatContainer.style.display === "none" || chatContainer.style.display === "" ? "block" : "none";
}

function sendMessage() {
    var question = document.getElementById("question").value;
    var chatBox = document.getElementById("chat-box");
    if (question.trim() === "") return;  // Avoid sending empty messages

    // Add user message
    var userMessage = document.createElement("p");
    userMessage.className = "user-message";
    userMessage.innerText = question;
    chatBox.appendChild(userMessage);

    // Fetch response from the server
    fetch(`/get_response/?question=${encodeURIComponent(question)}`)
        .then(response => response.json())
        .then(data => {
            var botMessage = document.createElement("p");
            botMessage.className = "bot-message";
            botMessage.innerText = data.answer;
            chatBox.appendChild(botMessage);
            chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to the bottom
        })
        .catch(error => {
            console.error('Error fetching response:', error);
        });

    document.getElementById("question").value = "";  // Clear input field
}

function askPredefinedQuestion(question) {
    document.getElementById("question").value = question;
    sendMessage();
}
