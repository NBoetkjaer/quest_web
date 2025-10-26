from flask import (Flask, render_template, request, session)
from markupsafe import Markup

import json
import quest_manager as quest_manager
from  utils import (safe_cast)

questApp = quest_manager.quest_manager()
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.get('/getting_started')
def get_getting_started():
  return render_template('getting_started.html')

@app.get('/')
def get_quest_descriptiont():
  print ("quest_get")
  questNo = safe_cast(request.args.get('quest', -1), int, -1)
  quest = questApp.get_quest(questNo)

  if quest == None:
    return render_template('index.html')
  return render_template(quest.get_html_template(), description = Markup(quest.get_description()))

@app.post('/')
def quest_api():
  if 'json' in request.headers['Content-Type']:
    args = request.json
    if not 'cmd' in args:
      return error_response('"cmd" not found i json')
    # Get quest 
    if args['cmd'] == 'get':
      return get_quest(args)
    # Answer quest
    if args['cmd'] == 'answer':
      return answer_quest(args)
    return error_response('Unhandled command: ' + args['cmd'])
  else:
    return error_response('Expected json data')

def error_response(message):
  return {'err': message}

def get_quest(args):
  session.pop('quest', None)
  if not 'questNo' in args:
    return { 'err': "cmd=get: Missing questNo."}
  if not 'user' in args:
    return { 'err': "cmd=get: Missing user."}

  questNo = safe_cast(args['questNo'], int, -1)
  print(f'Quest number {questNo} requested.')
  quest = questApp.get_quest(questNo)
  if quest == None:
    return { 'err': "cmd=get: Invalid quest number."}
  # Get a new quest and add questNo to the dictonary.
  retVal = quest.get_new_quest()
  retVal['questNo'] = questNo
  userSession = { 'user'    : str(args['user']) }
  userSession.update(retVal)
  session['quest'] = userSession # Save the user a session cookie.
  return retVal

def answer_quest(args):
  if not 'quest' in session:
    return error_response('No active quest session - get quest first')
  questData = session['quest']
  if not 'outputData' in args:
    return error_response('cmd=answer: Missing field "outputData"')
  questNo = safe_cast(questData['questNo'], int, -1)
  quest = questApp.get_quest(questNo)
  if quest == None:
    return  error_response('cmd=answer: Invalid quest number.')
  return  quest.get_evaluation_message(questData, args)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80, threaded=True)