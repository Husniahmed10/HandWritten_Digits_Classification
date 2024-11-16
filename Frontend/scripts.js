function displayPreview(event) {
    const imagePreview = document.getElementById('image-preview');
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = `<p>No image uploaded.</p>`;
    }
}

function predictDigit() {
    const fileInput = document.getElementById('file-input');
    const output = document.getElementById('output');

    if (fileInput.files.length === 0) {
        output.textContent = 'Please upload an image.';
        output.style.color = '#e53935'; // Error feedback
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                output.textContent = `Error: ${data.error}`;
                output.style.color = '#e53935';
            } else {
                output.innerHTML = `Predicted Digit: <span style="color: #4a90e2;">${data.digit}</span>`;
                output.style.color = '#333';
            }
        })
        .catch((error) => {
            output.textContent = `Error: ${error.message}`;
            output.style.color = '#e53935';
        });
}
