// ポモドーロタイマーの基本的なスクリプト
document.addEventListener("DOMContentLoaded", () => {
    console.log("Pomodoro Timer Loaded!");

    let timer;              // setInterval の ID を格納
    let isRunning = false;  // 動作中かどうか
    let timeLeft = 25 * 60; // 残り時間（秒） 25分 = 1500秒
    let sessionCount = 0;   // 作業回数
    let mode = "work";      // "work" または "break"

    const timerDisplay = document.getElementById("timer")
    const statusDisplay = document.getElementById("status")

    const startBtn = document.getElementById("start")
    const pauseBtn = document.getElementById("pause")
    const resetBtn = document.getElementById("reset")

    // アラーム音を読み込み
    const alarmSound = new Audio("/static/春の山.mp3");

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
                    alarmSound.play(); // 終了時に音を鳴らす
                    switchMode(); // 0になったら次のモードに切り替え
                }
            }, 1000);
        }
    }

    // 一時停止
    function pauseTimer() {
        clearInterval(timer);
        isRunning = false;
        // 再生中のアラームを止める
        alarmSound.pause();
        alarmSound.currentTime = 0;
    }

    // リセット
    function resetTimer() {
        clearInterval(timer);
        isRunning = false;
        sessionCount = 0;
        mode = "work";
        timeLeft = 25 * 60; // 初期値に戻す
        updateDisplay();
        statusDisplay.textContent = "作業時間";
        // 再生中のアラームを止める
        alarmSound.pause();
        alarmSound.currentTime = 0;
    }

    // モード切替
    function switchMode() {
        if (mode === "work") {
            sessionCount++;
            if (sessionCount % 4 === 0) {
                // 長い休憩
                mode = "break";
                timeLeft = 15 * 60;
                statusDisplay.textContent = "長い休憩";
            } else {
                // 短い休憩
                mode = "break";
                timeLeft = 5 * 60;
                statusDisplay.textContent = "休憩"
            }
        } else {
            // 休憩 → 作業
            mode = "work";
            timeLeft = 25 * 60;
            statusDisplay.textContent = "作業時間";
        }
        updateDisplay();
    }

    // ボタン処理
    startBtn.addEventListener("click", startTimer);
    pauseBtn.addEventListener("click", pauseTimer);
    resetBtn.addEventListener("click", resetTimer);

    // 初期表示を反映
    updateDisplay();
});