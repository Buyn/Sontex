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

// * onchange : 
useCounterBox.onchange = () => {
		prevCounter.disabled = !useCounterBox.checked;
		currCounter.disabled = !useCounterBox.checked;
}

// * onclick : 
exelBtn.onclick = () => getExel(	exelInput,
																	["excel files","*.xlsx"],
																	"Вибрати файл вхідного звіту");

csvBtn.onclick = () => getDBfile( csvInput,
																	[["csv files", "*.csv"], ["rlv files", "*.rlv"]],
																	"Обрати файл показників пристроїв .csv або .rlv");

outputBtn.onclick = () => saveAs( outputInput,
																	["excel files","*.xlsx"],
																	"Зберегти звіт як");

reportBtn.onclick = () => start_calc();

refreshLog();
setInterval(refreshLog, 3000);

// * function getExel :
async function getExel(input, filetype, title) {
		var dosya_path = await eel.btn_ask_open_exel_file(input.value, filetype, title)();
		if (dosya_path) {
				console.log(dosya_path);
				input.value = dosya_path;
				document.cookie = input.name + "=" + dosya_path;
				}
		refreshLog();
		}

// * function getDBfile :
async function getDBfile(input, filetype, title) {
		var dosya_path = await eel.btn_ask_open_DBfiles(input.value, filetype, title)();
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
		var log_strings= await eel.pull_log()();
		log_strings.reverse();
		log_strings.forEach(string => sendToLog(string));
		}


// * function start_calc() : 
async function start_calc() {
		console.log("statr calc");
		sendToLog(" ");
		sendToLog(" ");
		sendToLog("--------------------------------------------------");
		// sendToLog(new Date().toISOString().replace("T", " ").slice(0,16));
		sendToLog(new Date());
		sendToLog("Почато розрахунок показників");
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
		await pause(2000);
		sendToLog("Розрахунок показників завершився успішно");
		sendToLog("Результат розрахунку збережено у файлі " + outputInput.value);
		refreshLog();
		// sendToLog(new Date().toISOString().replace("T", " ").slice(0,16));
		sendToLog(new Date());
		sendToLog("==================================================");
		sendToLog(" ");
	}
function pause(delay){
		return new Promise(resolve => setTimeout(resolve, delay));
}
