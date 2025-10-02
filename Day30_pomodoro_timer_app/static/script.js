// ポモドーロタイマーの基本的なスクリプト
document.addEventListener("DOMContentLoaded", () => {
    console.log("Pomodoro Timer Loaded!");

    // ===== テスト用フラグ =====
    const TEST_MODE = true; // ← false にすると本番時間に戻る

    // 作業時間・休憩時間の定数を設定　テストモード：本番
    const WORK_TIME     = TEST_MODE ? 5 : 25 * 60;   // 5秒 or 25分
    const SHORT_BREAK   = TEST_MODE ? 3 : 5 * 60;    // 3秒 or 5分
    const LONG_BREAK    = TEST_MODE ? 6 : 15 * 60;    // 6秒 or 15分

    // 変数を定義
    let timer;              // setInterval の ID を格納
    let isRunning = false;  // 動作中かどうか
    let timeLeft = WORK_TIME; // 残り時間（秒）
    let sessionCount = 0;   // 作業回数
    let mode = "work";      // "work" または "break"

    const timerDisplay = document.getElementById("timer")
    const statusDisplay = document.getElementById("status")

    const startBtn = document.getElementById("start")
    const pauseBtn = document.getElementById("pause")
    const resetBtn = document.getElementById("reset")

    const historyList = document.getElementById("history");

    // アラーム音を読み込み
    const alarmSound = new Audio("/static/春の山.mp3");

    // 履歴を追加する関数
    function addHistoryEntry(modeText) {
        const li = document.createElement("li");
        const now = new Date();
        const timeStr = now.toLocaleTimeString([], { hour: "2-digit", minute:"2-digit" });
        li.textContent = `${timeStr} - ${modeText} 完了`;
        historyList.prepend(li); // 最新が上にくるように
    }

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

                    // カウントダウン終了時
                    if (timeLeft === 0) {
                        clearInterval(timer);
                        isRunning = false;
                        alarmSound.play();

                        // 今のモードを履歴に記録
                        if (mode === "work") {
                            addHistoryEntry("作業");
                        } else {
                            addHistoryEntry("休憩");
                        }
                    }

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
        timeLeft = WORK_TIME; // 初期値に戻す
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
                // 長い休憩（4回作業するごとに）
                mode = "break";
                timeLeft = LONG_BREAK;
                statusDisplay.textContent = "長い休憩";
            } else {
                // 短い休憩
                mode = "break";
                timeLeft = SHORT_BREAK;
                statusDisplay.textContent = "休憩"
            }
        } else {
            // 休憩 → 作業
            mode = "work";
            timeLeft = WORK_TIME;
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