// Check if the browser supports getUserMedia
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Access the user's camera
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
        // Assign the camera stream to the video element
        var video = document.getElementById('camera-feed');
        video.srcObject = stream;
    })
        .catch(function (error) {
            console.error('Error accessing the camera: ', error);
        });
    } else {
        alert('getUserMedia is not supported in this browser');
    }
