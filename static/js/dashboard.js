let ProgressBar = require('progressbar.js')
const number_of_workers = 9;
const bar_parameters = {
  strokeWidth: 6,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  easing: 'easeInOut',
  duration: 1400,
  svgStyle: null,
  text: {
    value: '',
    alignToBottom: false
  },
from: {color: '#5bc605'},
  to: {color: '#ff6500'},
  // Set default step function for all animate calls
  step: (state, bar) => {
    bar.path.setAttribute('stroke', state.color);
    var value = Math.round(bar.value() * 200);
    if (value === 600) {
      bar.setText('N/A');
    } else {
      bar.setText(value);
    }

    bar.text.style.color = state.color;
  }
}

let bpm_curr = [];
let bpm_avg = [];
let worker_data = document.getElementsByClassName("worker-data");k 
for(let i =0; i<number_of_workers; i++){
  let container_curr = '#bpm_curr'+String(i+1)
  let container_avg = '#bpm_avg'+String(i+1)
  bpm_curr.push(new ProgressBar.SemiCircle(container_curr, bar_parameters));
  bpm_avg.push(new ProgressBar.SemiCircle(container_avg, bar_parameters));
}
bpm_curr.forEach(bar=>{
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '1rem';
  bar.set(3);  // Number from 0.0 to 1.0
})
bpm_avg.forEach(bar=>{
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '1rem';
  bar.set(3);  // Number from 0.0 to 1.0
})

function setAvgBpm(val, worker){
  val = val/200;
  if(bpm_avg[worker].value()>1){
    bpm_avg[worker].set(1);
  }
  bpm_avg[worker].animate(val);
}

function setCurrBpm(val, worker){
  val = val/200;
  if(bpm_curr[worker].value()>1){
    bpm_curr[worker].set(1);
  }
  bpm_curr[worker].animate(val);
}