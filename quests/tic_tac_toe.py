def get_next_board(player:int, currentBoard:list) -> list:
  if player_has_won(player, currentBoard):
    return currentBoard
  if player_has_won(other_player, currentBoard):
    return currentBoard

  board = currentBoard.copy()
  move = find_best_move(player, board)
  make_move(move, player, board)
  return board

def find_items(item:int, board:list):
  itemsPos = []
  pos = 0
  for i in board:
    if i == item:
      itemsPos.append(pos)
    pos += 1
  return itemsPos

def get_possible_moves(player:int, board:list):
  validMoves = []
  pieces = find_items(player, board) # Find player locations
  holes = find_items(0, board) # Empty/free locations
  if len(pieces) == 3: # when player has three pieces on the board one piece is moved.
    for take in pieces:
      for put in holes:
        validMoves.append( (take, put) )
  else: # Place a new piece
    for put in holes:
      validMoves.append( (put, put) )
  return validMoves

def find_best_move(player, board):
  bestScore = -MAX_SCORE
  bestMove = None
  for move in get_possible_moves(player, board):
    make_move(move, player, board)
    score = minimax( other_player(player), board, 3, False)
    undo_move(move, player, board)
    if score > bestScore:
      bestScore = score
      bestMove = move
  return bestMove

def minimax(player, board, depth, maximize):
  score = evaluate_player(player, board)
  if depth == 0 or score >= MAX_SCORE:
    if not maximize:
      score = -score
    return score

  if maximize == True:
    score = -MAX_SCORE
    validMoves = get_possible_moves(player, board)
    for move in validMoves:
      make_move(move, player, board)
      score = max(score, minimax( other_player(player), board, depth - 1, not maximize))
      undo_move(move, player, board)
  else:
    score = MAX_SCORE
    validMoves = get_possible_moves(player, board)
    for move in validMoves:
      make_move(move, player, board)
      score = min(score, minimax( other_player(player), board, depth - 1, not maximize))
      undo_move(move, player, board)
  return score

def make_move(move, player, board):
  board[ move[0] ] = 0
  board[ move[1] ] = player

def undo_move(move, player, board):
  board[ move[0] ] = player
  board[ move[1] ] = 0

def other_player(player:int) -> int: 
  other = [0, 2, 1]
  return other[player]

MAX_SCORE = 100
def score_func(inLine:int)->int:
  score_map = [0, MAX_SCORE//100, MAX_SCORE//10, MAX_SCORE]
  return score_map[inLine]

def evaluate_player(player:int, brd:list) -> int:
  score = 0
  # Rows
  score += score_func( brd[0:3].count(player) )
  score += score_func( brd[3:6].count(player) )
  score += score_func( brd[6:9].count(player) )
  # Columns
  score += score_func( [brd[0], brd[3], brd[6]].count(player) )
  score += score_func( [brd[1], brd[4], brd[7]].count(player) )
  score += score_func( [brd[2], brd[5], brd[8]].count(player) )
  # Diagonals
  score += score_func( [brd[0], brd[4], brd[8]].count(player) )
  score += score_func( [brd[2], brd[4], brd[6]].count(player) )
  return score

def player_has_won(player:int, board:list):
  return evaluate_player(player, board) >= MAX_SCORE
