/* 画面にオセロ盤 + 初期配置（中央に黒白）を表示 */
const board = document.getElementById("board");

// 盤面データ（0=空, 1=黒, 2=白）
let boardState = Array(8).fill().map(() => Array(8).fill(0)) ;

// 初期配置
boardState[3][3] = 2;
boardState[3][4] = 1;
boardState[4][3] = 1;
boardState[4][4] = 2;

function renderBoard() {
    board.innerHTML = "";
    for (let y = 0; y < 8; y++) {
        for (let x = 0; x < 8; x++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cell.dataset.x = x;
            cell.dataset.y = y;

            if (boardState[y][x] === 1) {
                const stone = document.createElement("div");
                stone.className = "stone black";
                cell.appendChild(stone);
            } else if (boardState[y][x] === 2) {
                const stone = document.createElement("div");
                stone.className = "stone white";
                cell.appendChild(stone);
            }

            cell.addEventListener("click", placeStone);
            board.appendChild(cell);
        }
    }
}

renderBoard();


/* クリックしたマスに交互に黒白の石を置く処理 */
let currentPlayer = 1; // 1=黒, 2=白

function placeStone(e) {
    const x = parseInt(e.target.dataset.x);
    const y = parseInt(e.target.dataset.y);

    if (boardState[y][x] !== 0) return; // すでに石がある場合は無効

    boardState[y][x] = currentPlayer;

    // ターン交代
    currentPlayer = (currentPlayer === 1) ? 2 : 1;
    renderBoard();
}