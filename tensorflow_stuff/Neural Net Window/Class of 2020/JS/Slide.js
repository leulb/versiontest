var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'backgrounds/img1.jpg';
images[1] = 'backgrounds/img2.jpg';
images[2] = 'backgrounds/img3.jpg';
images[3] = 'backgrounds/img4.jpg';
images[4] = 'backgrounds/img5.jpg';
images[5] = 'backgrounds/img6.jpg';
images[6] = 'backgrounds/img7.jpg';
images[7] = 'backgrounds/img8.jpg';
images[8] = 'backgrounds/img9.jpg';
images[9] = 'backgrounds/img10.jpg';
images[10] = 'backgrounds/img11.jpg';
images[11] = 'backgrounds/img12.jpg';
images[12] = 'backgrounds/main.jpg';

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
