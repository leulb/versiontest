var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'Art/A1.jpg';
images[1] = 'Art/A2.jpg';
images[2] = 'Art/A3.jpg';
images[3] = 'Art/A4.jpg';
images[4] = 'Art/A5.jpg';
images[5] = 'Art/A6.jpg';
images[6] = 'Art/A7.jpg';
images[7] = 'Art/A1.jpg';


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
