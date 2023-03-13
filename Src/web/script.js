// * const : 
const initForm = document.getElementById("init-form");
const cookies = document.cookie.split("; ").map(str => str.split("=")).reduce((obj, [key, value]) => ({...obj, [key]:value}), {});

const logArea = document.getElementById("log");

const useCounterBox = initForm["use-count"];
const prevCounter = initForm["prev-count"];
const currCounter = initForm["curr-count"];

const exelBtn = initForm["exel-btn"];
// const exelFile = initForm["exel-file"];
const exelInput = initForm["exel-input"];

const csvBtn = initForm["csv-btn"];
// const csvFile =	initForm["csv-file"];
const csvInput = initForm["csv-input"];
// console.log(document.cookie);

const outputBtn = initForm[  "output-btn"];
// const outputFile =	initForm["output-file"];
const outputInput = initForm["output-input"];

const reportBtn = initForm["report-btn"];
// const reportModal = document.getElementById("report-modal");

// * cookies : 
exelInput.value = cookies.exel || "";
csvInput.value = cookies.csv || "";
outputInput.value = cookies.output || "";

// * onclick : 
exelBtn.onclick = () => getFolder(exelInput,
																	["excel files","*.xlsx"],
																	"Выбрать фаил входящего отчёта");
csvBtn.onclick = () => getFolder( csvInput,
																 ["csv files", "*.csv"],
																	"Выбрать фаил показания устройств");
outputBtn.onclick = () => saveAs( outputInput,
																	["excel files","*.xlsx"],
																	"Сохранить отчёт как");

reportBtn.onclick = () => start_calc();


// * function getFolder :
async function getFolder(input, filetype, title) {
		var dosya_path = await eel.btn_ResimyoluClick(input.value, filetype, title)();
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

// * function saveAs :
async function saveAs(input, filetype, title) {
		var dosya_path = await eel.btn_asksaveasfile(input.value, filetype, title)();
		if (dosya_path) {
				console.log(dosya_path);
				input.value = dosya_path;
				document.cookie = input.name + "=" + dosya_path;
				}
		}

// * function sendToLog :
function sendToLog(text) {
		logArea.value = text + "\n" + logArea.value;
		}

// * function start_calc() : 
async function start_calc() {
		console.log("statr calc");
		sendToLog("statr calc");
		document.cookie = exelInput.name + "=" + exelInput.value;
		document.cookie = csvInput.name + "=" + csvInput.value;
		document.cookie = outputInput.name + "=" + outputInput.value;
		const counterValues = useCounterBox.checked && [currCounter.value, prevCounter.value] || null;
		console.log(counterValues);
		var r = await eel.start_calc(exelInput.value, csvInput.value, outputInput.value, counterValues)();
		console.log(exelInput.value);
		console.log(csvInput.value);
		console.log(outputInput.value);
		console.log("reult of calc =", r);
		sendToLog("end calc =");
		sendToLog("reult of calc =");
		sendToLog("report saved in = ", outputInput.value);
		sendToLog(r);
	}

