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
    var value = Math.round(40+bar.value() * 120);
    if (value === 400) {
      bar.setText('N/A');
    }
    else if(value>=160){
      bar.setText('160+');
    } 
    else {
      bar.setText(value);
    }

    bar.text.style.color = state.color;
  }
}

let bpm_curr = [];
let bpm_avg = [];
let worker_data = document.getElementsByClassName("worker-data"); 
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
  if(val>=160){
    val=160;
  }
  val = (val-40)/120;
  if(bpm_avg[worker].value()>1){
    bpm_avg[worker].set(1);
  }
  bpm_avg[worker].animate(val);
}

function setCurrBpm(val, worker){
  if(val>=160){
    val=160;
  }
  val = (val-40)/120;
  if(bpm_curr[worker].value()>1){
    bpm_curr[worker].set(1);
  }
  bpm_curr[worker].animate(val);
}

function setWorkerData(h, stat, worker){
  let status = document.getElementById('worker'+String(worker+1)).getElementsByClassName('status');
  let height = document.getElementById('worker'+String(worker+1)).getElementsByClassName('height');
  status[0].innerHTML=stat;
  if(stat=='Online'){
    try{
      status[0].classList.remove('red-text');
      status[0].classList.add('green-text');
    }
    catch{}
  }
  else{
    try{
      status[0].classList.remove('green-text');
      status[0].classList.add('red-text');
    }
    catch{}
  }
  height[0].innerHTML=String(h)+"m";
}

const url = "http://192.168.0.9:8080/get?addr=all";
setInterval(()=>{
  fetch(url)
    .then(res=>{
      if (res.ok) {
        res.json()
          .then(data=>{json=data; return data})
          .then(json=>{
            for(var key in json){
              if(key!='status'){
                setAvgBpm(json[key].pulse.avg,parseInt(key));
                setCurrBpm(json[key].pulse.curr,parseInt(key));
                let stat = "Online";
                if(json[key].fall_detected===true||json[key].pulse.curr>130||json[key].pulse.curr<60||json[key].pulse.avg>130||json[key].pulse.avg<60){
                  stat = "Critical"
                }
                setWorkerData(json[key].height, stat, parseInt(key));
                
              }
            }
          });
      } 
      else {
        alert("HTTP-Error: " + res.status);
      }
    })
}, 750);