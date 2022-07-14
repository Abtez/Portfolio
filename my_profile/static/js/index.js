var i = 0;
var images = [];
var slideTime = 3000; // 3 seconds

images[0] = '../image/burn.jpg';
images[1] = '../image/vivid.jpg';
images[2] = '../image/punch.jpg';

function changePicture() {
    document.body.style.backgroundImage = "url(" + images[i] + ")";

    if (i < images.length - 1) {
        i++;
    } else {
        i = 0;
    }
    setTimeout(changePicture, slideTime);
}

window.onload = changePicture;