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

refreshLog();
setInterval(refreshLog, 5000);

// * function getFolder :
async function getFolder(input, filetype, title) {
		var dosya_path = await eel.btn_ResimyoluClick(input.value, filetype, title)();
		if (dosya_path) {
				console.log(dosya_path);
				input.value = dosya_path;
				document.cookie = input.name + "=" + dosya_path;
				}
		refreshLog();
		}

// * function saveAs :
async function saveAs(input, filetype, title) {
		var dosya_path = await eel.btn_asksaveasfile(input.value, filetype, title)();
		if (dosya_path) {
				console.log(dosya_path);
				input.value = dosya_path;
				document.cookie = input.name + "=" + dosya_path;
				}
		refreshLog();
		}

// * function sendToLog :
function sendToLog(text) {
		logArea.value = text + "\n" + logArea.value;
		}
// * function refreshLog :
async function refreshLog() {
		var log_strigs= await eel.pull_log()();
		log_strigs.reverse();
		log_strigs.forEach(strig => sendToLog(strig));
		}


// * function start_calc() : 
async function start_calc() {
		console.log("statr calc");
		sendToLog("Начат расчёт показателей");
		document.cookie = exelInput.name + "=" + exelInput.value;
		document.cookie = csvInput.name + "=" + csvInput.value;
		document.cookie = outputInput.name + "=" + outputInput.value;
		const counterValues = useCounterBox.checked && [currCounter.value, prevCounter.value] || null;
		console.log(counterValues);
		var r = await eel.start_calc(exelInput.value, csvInput.value, outputInput.value, counterValues)();
		refreshLog();
		console.log(exelInput.value);
		console.log(csvInput.value);
		console.log(outputInput.value);
		console.log("result of calc =", r);
		refreshLog();
		sendToLog("Расчёт показателей завершился успешно");
		sendToLog("Результат расчёта сохранен в файле " + outputInput.value);
		refreshLog();
	}

