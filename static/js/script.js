const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const capture = document.getElementById('capture');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  });

capture.onclick = () => {
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, 320, 240);
  canvas.toBlob(blob => {
    const formData = new FormData();
    formData.append('image', blob);
    fetch('/login-face/', {
      method: 'POST',
      body: formData,S
    }).then(res => res.json())
      .then(data => console.log(data));
  }, 'image/jpeg');
};
