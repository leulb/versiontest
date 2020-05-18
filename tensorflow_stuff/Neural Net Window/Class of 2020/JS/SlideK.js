var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'k/k1.jpg';
images[1] = 'k/k2.jpg';
images[2] = 'k/k3.jpg';
images[3] = 'k/k4.jpg';
images[4] = 'k/k5.jpg';
images[5] = 'k/k6.jpg';
images[6] = 'k/k7.jpg';
// Change Image
function changeImg() {
  document.slide.src = images[i];

  if (i < images.length - 1) {
    i++;
  } else {
    i = 0;
  }

  setTimeout("changeImg()", time);
}

window.onload = changeImg;
