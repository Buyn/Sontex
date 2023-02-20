// * const : 
const initForm = document.getElementById("init-form");
const cookies = document.cookie.split("; ").map(str => str.split("=")).reduce((obj, [key, value]) => ({...obj, [key]:value}), {});

const exelBtn = initForm["exel-btn"];
const exelFile = initForm["exel-file"];
const exelInput = initForm["exel-input"];
exelInput.value = cookies.exel || "";

const csvBtn = initForm["csv-btn"];
const csvFile =	initForm["csv-file"];
const csvInput = initForm["csv-input"];
// console.log(document.cookie);
csvInput.value = cookies.csv || "";

const reportBtn = initForm["report-btn"];
const reportModal = document.getElementById("report-modal");

// * onclick : 
exelBtn.onclick = () => getFolder(exelInput);
csvBtn.onclick = () => getFolder(csvInput);
reportBtn.onclick = () => start_calc();


// * function getFolder(input) :
async function getFolder(input) {
	var dosya_path = await eel.btn_ResimyoluClick(input.value)();
		if (dosya_path) {
				console.log(dosya_path);
				input.value = dosya_path;
				document.cookie = input.name + "=" + dosya_path;
				}
		}
// async function getFolder() {
// var dosya_path = await eel.btn_ResimyoluClick()();
// 	if (dosya_path) {
// 		console.log(dosya_path);
// 		exelInput.value = dosya_path;
// 	}
// }

// * function start_calc() : 
async function start_calc() {
		console.log("statr calc");
		document.cookie = exelInput.name + "=" + exelInput.value;
		document.cookie = csvInput.name + "=" + csvInput.value;
		var r = await eel.start_calc(exelInput.value, csvInput.value)();
		console.log(exelInput.value);
		console.log(csvInput.value);
		console.log("reult of calc =", r);
	}

