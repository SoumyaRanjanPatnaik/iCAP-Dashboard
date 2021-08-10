let logs__worker=document.querySelectorAll(".logs__worker");
logs__worker.forEach(item=>{
	item.addEventListener("click",e=>{
		let worker_name_block = item.querySelector(".logs__worker__name");
		if(e.target!=worker_name_block&&e.target!=worker_name_block.querySelector(".logs__worker__name__icon")){
			return
		}
		else{
			logs__worker.forEach(item_=>{
				let logs = item_.querySelector('.table-container');
				let icon = item_.querySelector('.logs__worker__name__icon')
				if(item_===item){
					logs.classList.toggle("no_height");
					item.classList.toggle("shadow")
					setTimeout(()=>{
						logs.classList.toggle("scrollbar")
					},610);
					if(icon.innerHTML==="+"){
						icon.innerHTML = "-";
						icon.style.left = "3.5px";
					}
					else{
						icon.innerHTML = "+";
						icon.style.left = "0px";
					}
					return;
				}
				logs.classList.add("no_height");
				logs.classList.remove("shadow")
				logs.classList.remove("scrollbar")
				icon.innerHTML = "+";
				icon.style.left = "0px";
			})	
			let logs = item.querySelector('.table-container');
		}
	})
});