function indexOfMax(arr) {
  if(arr.length == 0) {
    return -1;
  }
  var max = arr[0];
  var maxIndex = 0;

  for (var i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      maxIndex = i;
      max = arr[i];
    }
  }
  return maxIndex;
}
  async function app() {
      document.getElementById('console').innerHTML= 'Loading model..';

      // Load the model.
        const net = await tf.loadLayersModel('https://cdn.jsdelivr.net/gh/leulb/versiontest@master/tensorflow_stuff/Neural Net Window/test_tfjs_model/model.json');
      document.getElementById('console').innerHTML = 'Model Successfully Loaded';

      // Make a prediction through the model on our image.
      const poss = ["Blair","Hollenbeck","Koch","Krieg","Science","Synod","Zimmerman"];
      const imgEl = document.getElementById('img');
        const imgTens1 = tf.browser.fromPixels(imgEl);
        const imgTens2 = imgTens1.expandDims();
      const arr = await net.predict(imgTens2).dataSync();
      const guessNum = indexOfMax(arr);
      const guess = poss[guessNum];
      console.log(arr);
      document.getElementById('console').innerHTML = guess;
    }
