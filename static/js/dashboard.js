let ProgressBar = require('progressbar.js')
const bar_parameters = {
  strokeWidth: 6,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  easing: 'easeInOut',
  duration:950,
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
    var value = Math.round(35+bar.value() * 145);
    if (value >= 240) {
      bar.setText('N/A');
    }
    else if(value>=160){
      bar.setText('180+');
    } 
    else {
      bar.setText(value);
    }

    bar.text.style.color = state.color;
  }
}

for(key in bpm_curr){
    let container_curr = '#bpm_curr'+String(key)
    let container_avg = '#bpm_avg'+String(key)
    bpm_curr[key] = new ProgressBar.SemiCircle(container_curr, bar_parameters);
    bpm_avg[key] = new ProgressBar.SemiCircle(container_avg, bar_parameters);
}
for(bar in bpm_curr){
    bpm_curr[bar].text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
    bpm_curr[bar].text.style.fontSize = '1rem';
    bpm_curr[bar].set(3);  // Number from 0.0 to 1.0
}
for(bar in bpm_avg){
    bpm_avg[bar].text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
    bpm_avg[bar].text.style.fontSize = '1rem';
    bpm_avg[bar].set(3);  // Number from 0.0 to 1.0
}

function setAvgBpm(val, worker){
  if(val>=180){
    val=180;
  }
  val = (val-35)/145;
  if(bpm_avg[worker].value()>1){
    bpm_avg[worker].set(1);
  }
  bpm_avg[worker].animate(val);
}

function setCurrBpm(val, worker){
  if(val>=180){
    val=180;
  }
  val = (val-35)/145;
  if(bpm_curr[worker].value()>1){
    bpm_curr[worker].set(1);
  }
  bpm_curr[worker].animate(val);
}

function setWorkerData(h, stat, worker){
  let status = document.getElementById('worker'+String(worker)).getElementsByClassName('status');
  let height = document.getElementById('worker'+String(worker)).getElementsByClassName('height');
  let worker_element = document.getElementById('worker'+String(worker))
  status[0].innerHTML=stat;
  if(stat==='Offline'){
      status[0].classList.remove('green-text');
      status[0].classList.add('red-text');
      worker_element.classList.add('dull')      
  }
  else if(stat=='Online'){
    try{
      status[0].classList.remove('red-text');
      status[0].classList.add('green-text');
      worker_element.classList.remove('dull')      
    }
    catch{}
  }
  else if(stat=="Critical"){
    try{
      status[0].classList.remove('green-text');
      status[0].classList.add('red-text');
      worker_element.classList.remove('dull')      

    } catch{}

  }
  else if (stat=="Warning"){
    try{

    } catch{}

  }
  if(h!=null){
    height[0].innerHTML=String(h)+"m";
  }
  else{
    height[0].innerHTML="N/A";
  }
}

const url = "http://192.168.0.100:8080/get?addr=all";
setInterval(()=>{
  fetch(url)
    .then(res=>{
      if (res.ok) {
        res.json()
          // .then(data=>{json=data; return data})
          .then(json=>{
            for(var key in json){
              if(key!='status'){
                try{
                  try{
                    setAvgBpm(json[key].pulse.avg,parseInt(key));
                    setCurrBpm(json[key].pulse.curr,parseInt(key));
                  }
                  catch{}
                  let stat = "Online";
                  try {
                    stat = json[key].status

                  } catch (error) {}
                  try{
                    if(json[key].fall_detected===true||json[key].pulse.curr>155||json[key].pulse.curr<45||json[key].pulse.avg>145||json[key].pulse.avg<45){
                      stat = "Critical"
                    }
                  }
                  catch{}
                  setWorkerData(json[key].height, stat, parseInt(key));
                }
                catch{}
              }
            }
          });
      } 
      else {
        alert("HTTP-Error: " + res.status);
      }
    })
}, 1000);