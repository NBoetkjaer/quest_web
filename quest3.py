from quest_base import quest_base
import typing
import random as rnd
from utils import *

class quest3(quest_base):
    def __init__(self):
        super().__init__()

    def get_new_quest(self) -> dict:
        values = []
        for i in range (rnd.randrange(10, 20)):
            values.append(rnd.randrange(-100, 100))
        questdata = {
            'Hint': 'Beregn gennemsnittet.',
            'inputData': values
        }
        return questdata

    def check_answer(self, input: dict, output: dict) -> bool:
        indata = input['inputData']
        result = sum(indata)/len(indata)
        answer = safe_cast(output['outputData'], float)
        if answer is not None:
            return abs(result - answer) < 0.001
        return False

    def get_description(self) -> str:
        return r'''
<h2 class="center brown-text"><i class="material-icons">Opgave 3</i></h2>
<h5 class="center">Beregn gennemsnittet af tal</h5>

<p class="flow-text light">
  Nu skal du prøve at benytte Python til at beregne gennemsnitsværdien af en række tal.
  Hvis du ikke ved hvordan man beregner et gennemsnit - Så spørg din sidemand eller en anden hjælper, måske de ved det &#129488;.
  Ligesom i de forrige opgaver skal du sende en data pakke, hvor serveren bliver spurgt om input-data.
  I svaret fra serveren kan du læse listen med de tal som gennemsnittet skal beregnes udfra.
</p>
<p class="flow-text light">
<b>Hint:</b> Måske får du brug for at lave en løkke.<br>
I Python er der flere måder at lave løkker på. Nedenfor er vist en simple tælle-løkke som tæller fra 0 til og med 99 (bemærk at 100 ikke er med).
samt en løkke der løber gennem en liste.<br>
</p>
<p class="codeblock flow-text">#Simple for-løkke
for i in range(100):
    print(i) # 'i' tæller fra 0 til og med 99

# for-Løkke hen over en liste
minListe = [1, 12, 123, 1234]
for tal in minListe:
    print(tal)
</p>
<p class="flow-text light">
Prøv evt. at skrive flg. linier i en Python commando-linie og se hvad resultatet bliver.
</p>
<p class="codeblock flow-text">print(*range(10))
print(*range(10,20))
print(*range(20,10,-1))
</p>

<p class="flow-text light">
  Send nu nedenstående pakke til webserveren.
</p>
<p class="codeblock flow-text">questGet =
    {
        'cmd'     : 'get',
        'questNo' : 3,
        'user'    : 'Super koder', # Find selv på et navn eller brug dit eget.
    }</p>

<p class="codeblock flow-text">r = requests.post('http://webquest.local', data=questGet)</p>
<p class="flow-text light">
  Læs JSON pakken som du modtager fra servern, ligesom du gjorde i <a href="/?quest=1">opgave 1</a>.<br>
  (hint: feltet 'inputData' i dictionary'et indeholder listen med tal)
</p>

<p class="flow-text light">
  Når du har fundet tallene i listen, skal du beregne gennemsnittet og sende svaret til serveren.
  Svaret skal pakkes i et 'dictionary' som vist nedenfor (udskift '%UniqueID' med det ID du modtog fra serveren og %Answer med den værdi du har regnet ud).<br>
  Held og lykke med at lave løkker og pas godt på at de ikke bliver til uendelige "uløkker" &#128514;
</p>

<p class="codeblock flow-text">questAnswer =
    {
        'cmd'        : 'answer',
        'ID'         : %UniqueID # Det samme ID som vi modtog fra serveren.
        'outputData' : %Answer # Gennemsnittet af tallene
    }
</p>


<p class="flow-text light">
  Send pakken til serveren og se om du har svaret rigtig.
</p>
'''