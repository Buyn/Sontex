const initForm = document.getElementById("init-form");
const cookies = document.cookie.split("; ").map(str => str.split("=")).reduce((obj, [key, value]) => ({...obj, [key]:value}), {});

const logArea = document.getElementById("log");

const exelBtn = initForm["exel-btn"];
const exelInput = initForm["exel-input"];

const currCounter = initForm["curr-count"];

const csvBtn = initForm["csv-btn"];
const csvInput = initForm["csv-input"];

const mzkInput = initForm["mzk-cof"];
const fsoInput = initForm["fso-cof"];

const outputBtn = initForm["output-btn"];
const outputInput = initForm["output-input"];

const rereadBtn = initForm["reread-btn"];
const prevSelect = initForm["prev-date"];
const currSelect = initForm["curr-date"];

const reportBtn = initForm["report-btn"];

var gdataslist = []

exelInput.value = cookies.exel || "";
csvInput.value = cookies.csv || "";
outputInput.value = cookies.output || "";

exelBtn.onclick = () => getExel(  exelInput,
                                  ["excel files","*.xlsx"],
                                  "Вибрати файл вхідного звіту");

csvBtn.onclick = () => getDBfile( csvInput,
                                  [["csv files", "*.csv"], ["rlv files", "*.rlv"]],
                                  "Обрати файл показників пристроїв .csv або .rlv");

rereadBtn.onclick = () => readDBfile(csvInput);

outputBtn.onclick = () => saveAs( outputInput,
                                  ["excel files","*.xlsx"],
                                  "Зберегти звіт як");

reportBtn.onclick = () => start_calc_params();

refreshLog();
setInterval(refreshLog, 3000);

async function getExel(input, filetype, title) {
    var dosya_path = await eel.btn_ask_open_exel_file(input.value, filetype, title)();
    if (dosya_path) {
        console.log(dosya_path);
        input.value = dosya_path;
        document.cookie = input.name + "=" + dosya_path;
        }
    refreshLog();
    }

async function getDBfile(input, filetype, title) {
    var dosya_path = await eel.btn_ask_open_DBfiles(input.value, filetype, title)();
    if (dosya_path) {
        console.log(dosya_path);
        input.value = dosya_path;
        document.cookie = input.name + "=" + dosya_path;
        }
    readDBfile(csvInput);
    refreshLog();
    }

function fillSelect(select, strings) {
    const options = [select.firstElementChild, ...strings.map(str => new Option(str))];
    select.replaceChildren(...options);
    }

async function readDBfile(input) {
    gdataslist = await eel.get_dates_from_filename_string(input.value)();
    if (gdataslist) {
        console.log(gdataslist);
        fillSelect(currSelect, gdataslist);
        fillSelect(prevSelect, gdataslist);
        }
    refreshLog();
    }

async function saveAs(input, filetype, title) {
    var dosya_path = await eel.btn_asksaveasfile(input.value, filetype, title)();
    if (dosya_path) {
        console.log(dosya_path);
        input.value = dosya_path;
        document.cookie = input.name + "=" + dosya_path;
        }
    refreshLog();
    }

function sendToLog(text) {
    logArea.value = text + "\n" + logArea.value;
    }

async function refreshLog() {
    var log_strings= await eel.pull_log()();
    log_strings.reverse();
    log_strings.forEach(string => sendToLog(string));
    }

async function start_calc() {
    if(!exelInput.value){
        sendToLog("не заповнено поле вхідного файлу ексель");
        return;
    }
    if(!outputInput.value){
        sendToLog("не заповнено поле вихідного файлу звіту ексель");
        return;
    }
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
    const counterValues = currCounter.value && [currCounter.value, 0] || null; 
    console.log(counterValues);
    var r = await eel.start_calc(exelInput.value, csvInput.value, outputInput.value, counterValues)();
    refreshLog();
    console.log(exelInput.value);
    console.log(csvInput.value);
    console.log(outputInput.value);
    console.log("result of calc =", r);
    // refreshLog();
    await pause(1000);
    // refreshLog();
    await pause(1000);
    // refreshLog();
    sendToLog("Розрахунок показників завершився успішно");
    sendToLog("Результат розрахунку збережено у файлі " + outputInput.value);
    // sendToLog(new Date().toISOString().replace("T", " ").slice(0,16));
    sendToLog(new Date());
    sendToLog("==================================================");
    sendToLog(" ");
  }

async function start_calc_params() {
    if(!exelInput.value){
        sendToLog("не заповнено поле вхідного файлу ексель");
        return;
    }
    if(!outputInput.value){
        sendToLog("не заповнено поле вихідного файлу звіту ексель");
        return;
    }
    console.log("start calculations ...");
    sendToLog(" ");
    sendToLog(" ");
    sendToLog(new Date());
    sendToLog("--------------------------------------------------");
    // sendToLog(new Date().toISOString().replace("T", " ").slice(0,16));
    sendToLog("Почато розрахунок показників");
    document.cookie = exelInput.name + "=" + exelInput.value;
    document.cookie = csvInput.name + "=" + csvInput.value;
    document.cookie = outputInput.name + "=" + outputInput.value;
    const counterValues = currCounter.value && [currCounter.value, 0] || [0, 0]; 
    console.log(counterValues);
    var params ={
                "dates":[prevSelect.value, currSelect.value],
                "filenamestring":csvInput.value,
                "homecounter":counterValues,
                "coefficients":[mzkInput.value/100, fsoInput.value/100],
                "inputexel":exelInput.value,
                "outputexel":outputInput.value,
                "dateslist":gdataslist,};
    console.log(params);
    var r = await eel.start_calc_params(params)();
    refreshLog();
    console.log(exelInput.value);
    console.log(csvInput.value);
    console.log(outputInput.value);
    console.log("result of calc =", r);
    // refreshLog();
    await pause(1000);
    // refreshLog();
    await pause(1000);
    // refreshLog();
    sendToLog("Розрахунок показників завершився успішно");
    sendToLog("Результат розрахунку збережено у файлі " + outputInput.value);
    // sendToLog(new Date().toISOString().replace("T", " ").slice(0,16));
    sendToLog(new Date());
    sendToLog("==================================================");
    sendToLog(" ");
  }

function pause(delay){
    refreshLog();
    return new Promise(resolve => setTimeout(resolve, delay));
    refreshLog();
}
