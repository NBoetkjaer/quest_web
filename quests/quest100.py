from flask import (session)
from quests.quest_base import (quest_base)
from quests.tic_tac_toe import (player_has_won, get_next_board, find_items)
class quest(quest_base):
  PLAYER1 = 1
  PLAYER2 = 2
  def __init__(self):
    super().__init__()

  def get_html_template(self) -> str:
        return "quest100.html"
  def get_new_quest(self) -> dict:
    questdata = {
      'hint': 'Du skal tage det første træk.',
      'inputData': [0]*9
    }
    return questdata

  def get_evaluation(self, input: dict, output: dict) -> dict:
    user = input['user']
    lastBoard = input['inputData']
    currentBoard = output['outputData']
    validMove, msg = self.check_move(lastBoard, currentBoard)
    if not validMove:
      return {
        'evaluation': msg,
        'inputData' : lastBoard
      }
    else:
      if player_has_won(1, currentBoard):
        return {
          'evaluation': f'Du vandt! Du er jo en mester spiller, {user}',
          'inputData' : currentBoard
          }
      newBoard = get_next_board(2, currentBoard)
      session['quest']['inputData'] = newBoard # Update the cookie information.
      session.modified = True
      if player_has_won(2, newBoard):
        return {
          'evaluation': f'Nu har du tabt! {user}',
          'inputData' : newBoard
          }

      return {
        'evaluation': f'{msg}. Det er din tur {user}',
        'inputData' : newBoard
      }

  def check_move(self, lastBoard, board):
    print(f'check_move - lastBoard:{lastBoard}, board:{board}')
    if not isinstance(board, list) or len(board) != 9:
      return False, 'Der skal være ni elementer i listen'
    prev1 = find_items(quest.PLAYER1, lastBoard)
    prev2 = find_items(quest.PLAYER2, lastBoard)
    empty = find_items(0, board)
    current1 = find_items(quest.PLAYER1, board)
    current2 = find_items(quest.PLAYER2, board)
    if len(empty) + len(current1) + len(current2) != 9:
      return False, 'Der må kun være 0, 1 og 2 i listen.'
    if prev1 == current1:
      return False, 'Du har ikke lavet et træk'
    if prev2 != current2:
      return False, 'Du må ikke flytte på mine brikker'
    count = 0
    for i in current1:
      if i in prev1:
        count += 1
    if (len(current1) - count) != 1:
        print(current1)
        print(prev1)
        return False, 'Du må kun lave et træk'
    return True, 'ok'

  def drawBoard(self, brd):
    print(brd[0:3])
    print(brd[3:6])
    print(brd[6:9])

  def get_description(self) -> str:
      return r'''
<h2 class="center brown-text"><i>Opgave 100</i> </h2>
<h5 class="center">Tic-Tac-Toe</h5>
<p class="flow-text light">
I denne opgave kan du spille kryds og bolle mod serveren. Server sender en liste med 9 tal, hvor hvert tal repræsenterer
et felt i et kryds og bolle brætspil. De første tre tal svarer til den øverste række, de næste tre tal er den miderste række og
de sidste tre tal repræsenterer den nederste række. <br>
En talværdi på 1 betyder at du har sat en brik i dette felt. Er talværdien 2, er det serveren der har sat en brik i dette felt og er værdien
0, er feltet tomt. <br>
Nedenfor er vist en liste med ni tal, der repræsenterer en stilling i et kryds og bolle spil. Det er et's (1) tur til at trække
 - og han kan vinde spillet i næste træk!
</p>
<p class="codeblock flow-text">
board = [2, 0, 0,
         0, 2, 0,
         1, 1, 0]
</p>
<p class="flow-text light">
For at starte spillet skal du sende en 'get' commando til serveren
</p>
<p class="codeblock flow-text">questGet = {
  'cmd'     : 'get',
  'questNo' : 100,
  'user'    : 'TheTicTacMan',
}</p>

<p class="flow-text light">
Serveren vil svare tilbage ved at sende et nyt spil, hvor alle felter er tomme. Nedenfor er vist den besked som serveren sender:
</p>
<p class="codeblock flow-text">questdata = {
  'hint': 'Du skal tage det første træk.',
  'inputData': [0,0,0, 0,0,0, 0,0,0]
}</p>
<p class="flow-text light">
Find et godt træk og send dit træk til serveren. Hvis du f.eks. sætter en brik midt i spilbrættet, skal din besked se sådan ud:
</p>
<p class="codeblock flow-text">questAnswer = {
  'cmd'        : 'answer',
  'outputData' : [0,0,0, 0,1,0, 0,0,0]
}</p>

<p class="flow-text light">
Serveren vil herefter finde et modtræk til dit træk og sende det som svar på din forrige pakke.
</p>
<p class="codeblock flow-text">questdata = {
  'evaluation' : 'Det er din tur igen',
  'inputData'  : [2,0,0, 0,1,0, 0,0,0]
}</p>

<p class="flow-text light">
På denne måde skiftes du og serveren til at flytte brikkerne rundt på kryds og bolle brætspillet.<br>
Prøv at skrive et program, der på denne måde kan spille helt automatisk mod serveren.
</p>
'''