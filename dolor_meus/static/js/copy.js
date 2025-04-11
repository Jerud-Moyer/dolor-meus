window.addEventListener("DOMContentLoaded", () => { 
    const copyButton = document.querySelector("#copy_button");

    copyButton.addEventListener("click", () => {
        const text = document.querySelector("#view_box").innerText
        const tooltip = document.querySelector("#copy_tooltip")

        navigator.clipboard.writeText(text)
            .then(() => {
                tooltip.classList.add('visible')
                setTimeout(() => {
                    tooltip.classList.remove('visible')
                }, 2000);
            })
            .catch(err => {
                console.error("Error copying text: ", err);
            });
    })
})