const clockTitle = document.querySelector(".js-clock");
const countDate = new Date('dec 25, 2021 00:00:00').getTime();

function christmasHandler(){
    const now = new Date().getTime();
    gap = countDate - now;

    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour *24;

    const d = Math.floor(gap / (day));
    const h = Math.floor((gap % (day)) / (hour));
    const m = Math.floor((gap % (hour)) / (minute));
    const s = Math.floor((gap % (minute)) / (second));

    clockTitle.innerText = `${d}d ${h}h ${m}m ${s}s`;
}

christmasHandler();
setInterval(christmasHandler, 1000);