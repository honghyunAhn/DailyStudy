const colors = [
    "#ef5777",
    "#575fcf",
    "#4bcffa",
    "#34e7e4",
    "#0be881",
    "#f53b57",
    "#3c40c6",
    "#0fbcf9",
    "#00d8d6",
    "#05c46b",
    "#ffc048",
    "#ffdd59",
    "#ff5e57",
    "#d2dae2",
    "#485460",
    "#ffa801",
    "#ffd32a",
    "#ff3f34"
];

const color_btn = document.querySelector("button");

function handleColor(){
    const fir_color = colors[Math.floor(Math.random() * colors.length)];
    const sec_color = colors[Math.floor(Math.random() * colors.length)];
    
    document.body.style.background = "linear-gradient(" + fir_color + "," + sec_color + ")";
}

color_btn.addEventListener("click",handleColor);