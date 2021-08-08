document.querySelectorAll(".logs__worker").forEach(item=>{
	let max_height=getComputedStyle(item.querySelector("table"),null).getPropertyValue("max-height");
	let table_container = item.querySelector(".table-container")
	table_container.style.max_height=max_height;
	item.addEventListener("click",e=>{
		if(e.target!=item.querySelector(".logs__worker__name")){
			return
		}
		else{
			let logs = item.querySelector('.table-container');
			logs.classList.toggle("no_height");
			console.log("Valid event");
		}
	})
});