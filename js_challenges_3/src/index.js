const randomForm = document.getElementById("random-form");
const numberInput = randomForm.querySelectorAll("input");
const result = document.getElementById("result")
randomForm.addEventListener("submit", handleRandom);

function handleRandom(event){
    event.preventDefault();
    const num = numberInput[0].value;
    const guess = numberInput[1].value;
    
    if(isNaN(num) || isNaN(guess)){
        alert("숫자를 입력하세요.");
        return;
    }
    const random = Math.floor(Math.random() * num);

    document.getElementById("choseNum").innerHTML=guess;
    document.getElementById("machine").innerHTML=random;
    document.getElementById("comparison").classList.remove("hidden");

    if(random === parseInt(guess)){
        result.innerHTML="You won!";
    }else{
        result.innerHTML="You lost!";
    }
}