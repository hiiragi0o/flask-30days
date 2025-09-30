// ポモドーロタイマーの基本的なスクリプト
document.addEventListener("DOMContentLoaded", () => {
    console.log("Pomodoro Timer Loaded!");

    let timer;              // setInterval の ID を格納
    let isRunning = false;  // 動作中かどうか
    let timeLeft = 25 * 60; // 残り時間（秒） 25分 = 1500秒

    const timerDisplay = document.getElementById("timer")
    const statusDisplay = document.getElementById("status")

    const startBtn = document.getElementById("start")
    const pauseBtn = document.getElementById("pause")
    const resetBtn = document.getElementById("reset")

    // 残り時間を "MM:SS" 形式に変換
    function updateDisplay() {
        let minuts = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        timerDisplay.textContent = `${minuts.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
    }

    // カウントダウン開始
    function startTimer() {
        if (!isRunning) {
            isRunning = true;
            timer = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateDisplay();
                } else {
                    clearInterval(timer);
                    isRunning = false;
                    statusDisplay.textContent = "終了！";
                }
            }, 1000);
        }
    }

    // 一時停止
    function pauseTimer() {
        clearInterval(timer);
        isRunning = false;
    }

    // リセット
    function resetTimer() {
        clearInterval(timer);
        isRunning = false;
        timeLeft = 25 * 60; // 初期値に戻す
        updateDisplay();
        statusDisplay.textContent = "作業時間";
    }

    // イベント登録
    startBtn.addEventListener("click", startTimer);
    pauseBtn.addEventListener("click", pauseTimer);
    resetBtn.addEventListener("click", resetTimer);

    // 初期表示を反映
    updateDisplay();
});