function play(userChoice) {
    const choices = ['Rock', 'Scissors', 'Paper'];
    const cpuChoice = choices[Math.floor(Math.random() * 3)];

    let result = "";

    if (userChoice === cpuChoice) {
        result = "あいこ！";
    } else if (
        (userChoice === "Rock" && cpuChoice === "Scissors") ||
        (userChoice === "Scissors" && cpuChoice === "Paper") ||
        (userChoice === "Paper" && cpuChoice === "Rock")
    ){
        result = "あなたの勝ち！";
    } else {
        result = "コンピュータの勝ち！";
    }

    document.getElementById("result").innerText = 
        `あなた: ${userChoice} ／ CPU: ${cpuChoice} → ${result}`;
    
}