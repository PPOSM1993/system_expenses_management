const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector('.invalid_feedback');

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    if (usernameVal.length > 0) {
        fetch("/validate_username/", {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                if (data.username_error) {
                    usernameField.classList.add("is-invalid");
                    feedBackArea.style.display='block';
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`
                }
            })
    }
})