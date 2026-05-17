let encryptedGlobal = "";

const encryptForm = document.getElementById("encryptForm");
const decryptButton = document.getElementById("decryptButton");
const statusMessage = document.getElementById("statusMessage");
const flyingMessage = document.getElementById("flyingMessage");

encryptForm.addEventListener("submit", (event) => {
    event.preventDefault();
    encryptText();
});

decryptButton.addEventListener("click", decryptText);

flyingMessage.addEventListener("animationend", () => {
    flyingMessage.classList.remove("is-flying");
    flyingMessage.innerText = "";
});

function setStatus(message, isError = false) {
    statusMessage.innerText = message;
    statusMessage.style.color = isError ? "#FFC1CC" : "#A8DADC";
}

async function postCipherAction(endpoint, payload) {
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Something went wrong.");
    }

    return data;
}

async function encryptText() {

    const text = document.getElementById("text").value;
    const key = document.getElementById("key").value;

    try {
        const data = await postCipherAction("/encrypt", {
            text: text,
            key: key
        });

        encryptedGlobal = data.result;
        document.getElementById("result").innerText = "Nothing decrypted yet.";
        setStatus("Encrypted message sent.");

        animateMessage(encryptedGlobal);
    } catch (error) {
        setStatus(error.message, true);
    }
}


function animateMessage(message) {

    flyingMessage.innerText = message;
    flyingMessage.classList.remove("is-flying");
    void flyingMessage.offsetWidth;
    flyingMessage.classList.add("is-flying");

    window.setTimeout(() => {
        document.getElementById("encryptedResult").innerText = message;
    }, 700);
}


async function decryptText() {

    const key = document.getElementById("key").value;

    try {
        const data = await postCipherAction("/decrypt", {
            text: encryptedGlobal,
            key: key
        });

        document.getElementById("result").innerText = data.result;
        setStatus("Message decrypted.");
    } catch (error) {
        setStatus(error.message, true);
    }
}
