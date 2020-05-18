var i = 0; // Start point
var images = [];
var time = 4000;

// Image List

images[0] = 'sci/sci1.jpg';
images[1] = 'sci/sci2.jpg';
images[2] = 'sci/sci3.jpg';
images[3] = 'sci/sci4.jpg';
images[4] = 'sci/sci5.jpg';
images[5] = 'sci/sci6.jpg';
images[6] = 'sci/sci7.jpg';
images[7] = 'sci/sci8.jpg';

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
