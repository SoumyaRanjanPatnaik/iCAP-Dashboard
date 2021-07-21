let hamburger = document.getElementById("expand-menu");
let toggle =0;

function toggle_menu(){
	toggle++;
	toggle%=2;
	let menu = document.getElementById("menubar-items");
	if(toggle == 1){
		menu.style.flexBasis="197px";
		hamburger.focus();
	}
	else{
		menu.style.flexBasis="0";
		hamburger.focus();
	}
}

hamburger.addEventListener("click", toggle_menu);

function get_data(){

}