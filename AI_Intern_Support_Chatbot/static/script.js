async function sendMessage() {

    const inputField = document.getElementById("user-input");

    const message = inputField.value;

    if(message === "") return;

    const chatBox = document.getElementById("chat-box");

    // User Message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    const response = await fetch('/chat', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    // Bot Response
    chatBox.innerHTML += `
        <div class="bot-message">
            ${data.response}
        </div>
    `;

    inputField.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}