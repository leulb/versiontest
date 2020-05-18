var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'h/h1.jpg';
images[1] = 'h/h2.jpg';
images[2] = 'h/h3.jpg';
images[3] = 'h/h4.jpg';
images[4] = 'h/h5.jpg';

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
