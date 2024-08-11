<<<<<<< HEAD
// DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', function() {
    // Code to execute when the DOM is fully loaded

    // Example code: Change the text color of an element with id "myElement"
    var myElement = document.getElementById('myElement');
    myElement.style.color = 'red';
});
=======
document.getElementById('uploadForm').onsubmit = function() {
    document.getElementById('loading').classList.remove('hidden');
};

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const request = new XMLHttpRequest();
    request.open('POST', this.action, true);
    request.responseType = 'blob';

    request.onload = function() {
        if (this.status === 200) {
            const blob = this.response;
            const url = URL.createObjectURL(blob);
            document.getElementById('outputImage').src = url;
            document.getElementById('result').classList.remove('hidden');
            document.getElementById('loading').classList.add('hidden');
        } else {
            alert('An error occurred while processing the image.');
            document.getElementById('loading').classList.add('hidden');
        }
    };

    request.send(formData);
});
>>>>>>> d38a459604f85f66bc8038dc2656acdb89c737b4
