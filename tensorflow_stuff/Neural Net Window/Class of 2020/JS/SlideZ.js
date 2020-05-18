var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'z/z1.jpg';
images[1] = 'z/z2.jpg';
images[2] = 'z/z3.jpg';
images[3] = 'z/z4.jpg';
images[4] = 'z/z5.jpg';

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
