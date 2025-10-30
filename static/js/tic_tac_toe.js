const squares = document.getElementsByClassName('square')
const game_message = document.getElementById('game_message')
game_message.textContent = `Tryk på knappen for at starte et nyt spil`

let board = [0,0,0, 0,0,0, 0,0,0]
const opponentPlayer = 2; // Set to player 1 or 2
let currentPlayer = 2
let removedIndex = -1
for(let i = 0; i < squares.length; i++){
  // Add click events to all squares.
  squares[i].addEventListener('click', () => {
    if (currentPlayer == opponentPlayer){
      return
    }
    if(findItems(currentPlayer, board).length === 3){
      if(board[i] === currentPlayer){
        board[i] = 0; // Remove the piece
        drawBoard();
      }
      removedIndex = i;
      return;
    }
    else{
      if(board[i] === 0 && i != removedIndex){
        board[i] = currentPlayer; // Set piece
        removedIndex = -1;
        currentPlayer = otherPlayer(currentPlayer); // take turn
        drawBoard();
        sendBoard();
      }
    }
  })
}

function setMessage(msg){
  game_message.textContent = msg;
}
function sendBoard(){
  fetch_post({'cmd': 'answer', 'outputData': board})
}

function drawBoard(){
  if(board.length != 9){
    console.log('Invalid board:', board);
    return;
  }
  for(let i = 0; i< board.length; i++)
  {
    switch(board[i])
    {
      case 0: squares[i].textContent = ''; break;
      case 1: squares[i].textContent = 'X'; break;
      case 2: squares[i].textContent = 'O'; break;
    }
  }
}

function otherPlayer(player){
  const other = [0,2,1];
  return other[player];
}

function findItems(item){
  let itemPos = []
  board.forEach((elem, pos) => {
    if(elem === item){
      itemPos.push(pos)
    }
  });
  return itemPos;
}

function newGameButton(){
  currentPlayer = opponentPlayer
  fetch_post({ 'cmd'    : 'get', 'questNo'  : 100, 'user'   : 'Magnus Carlsen' });
}

async function fetch_post(jsonData){
  console.log('post to server:', jsonData)
  try {
    const response = await fetch("/", {
      method: "POST",
      mode: "same-origin",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(jsonData)
    });
    const contentType = response.headers.get("content-type");
    if (!contentType || !contentType.includes("application/json")) {
      throw new TypeError("JSON response was expected!");
    }
    jsonRespons = await response.json()
    console.log('received from server', jsonRespons)
    if(Object.hasOwn(jsonRespons, 'inputData')){
      newBoard = jsonRespons['inputData']
      if( Array.isArray(newBoard) && newBoard.length === 9){
        board = newBoard
        currentPlayer = otherPlayer(currentPlayer)
        drawBoard()
      }
    }
    if(Object.hasOwn(jsonRespons, 'hint')){
      setMessage(jsonRespons['hint'])
    }
    if(Object.hasOwn(jsonRespons, 'evaluation')){
      setMessage(jsonRespons['evaluation'])
    }
  } catch (error) {
    console.error("Error:", error);
  }
}
