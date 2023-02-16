const initForm = document.getElementById("init-form");
const exelBtn = initForm["exel-btn"];
const exelFile = initForm["exel-file"];
const exelInput = initForm["exel-input"];
const reportBtn = initForm["report-btn"];
const reportModal = document.getElementById("report-modal");


exelBtn.onclick = () => getFolder();
exelFile.onchange = () => exelInput.value = exelFile.files[0].path;
// exelFile.onchange = () => exelInput.value = exelFile.value;

reportBtn.onclick = () => reportModal.showModal();


// // Onclick of the button  
// document.querySelector("#genbutton").onclick = function () {    
// 	// Call python's random_python function  
// 	eel.random_python()(function(number){                        
// 		// Update the div with a random number returned by python  
// 		document.querySelector(".random_number").innerHTML = number;  
// 	});
// };  

document.querySelector("#genbutton").onclick = () => getFolder();

async function getFolder() {
var dosya_path = await eel.btn_ResimyoluClick()();
	if (dosya_path) {
		console.log(dosya_path);
		exelInput.value = dosya_path;
	}
}


// const { dialog } = require('electron')

// // Open a file selection dialog
// dialog.showOpenDialog({ properties: ['openFile'] }, (filePaths) => {
//   // filePaths is an array that contains the file path(s) of the selected file(s)
//   if (filePaths) {
//     // If a file was selected, do something with the file path
//     console.log(filePaths[0])
//   }
// })
