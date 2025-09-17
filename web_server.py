# from operator import ge
import os
# from webbrowser import get
import tornado.httpserver
import tornado.ioloop
import tornado.web
import json

import quest_manager as quest_manager
from  utils import (safe_cast)
questApp = quest_manager.quest_manager()
questMap = {}


#Tornado Folder Paths
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    )

#Tonado server port
PORT = 80

class MainHandler(tornado.web.RequestHandler):

  IDcounter = 0

  def get(self):
    questNo = safe_cast(self.get_query_argument('quest', '0'), int, -1)
    quest = questApp.get_quest(questNo)
    if quest == None:
      self.render('index.html')
      return
    self.render(quest.get_html_template(), description=quest.get_description())

  def get_quest(self, args):
    if not 'questNo' in args:
      return { 'err': "cmd=get: Missing questNo."}
    if not 'user' in args:
      return { 'err': "cmd=get: Missing user."}

    questNo = safe_cast(args['questNo'], int, -1)
    print(f'Quest number {questNo} requested.')
    quest = questApp.get_quest(questNo)
    if quest == None:
      return { 'err': "cmd=get: Invalid quest number."}


    id = MainHandler.IDcounter
    MainHandler.IDcounter += 1
    # Get a new quest and a ID and questNo to the dictonary.
    retVal = quest.get_new_quest()
    retVal['ID'] = id
    retVal['questNo'] = questNo
    args.update(retVal)
    questMap[id] = args
    return retVal

  def answer_quest(self, args):
    if not 'ID' in args:
      return { 'err': "cmd=answer: Missing ID."}
    if not 'outputData' in args:
      return { 'err': "cmd=answer: Missing outputData."}
    id = safe_cast(args['ID'], int, -1)
    if not id in questMap:
      return { 'err': "cmd=answer: Invalid ID."}
    questData = questMap[id]
    del questMap[id]
    questNo = safe_cast(questData['questNo'], int, -1)
    quest = questApp.get_quest(questNo)
    if quest == None:
      return { 'err': "cmd=answer: Invalid quest number."}

    return  quest.get_evaluation_message(questData, args)

  def post(self):
    if 'json' in self.request.headers['Content-Type']:
      args = json.loads(self.request.body)
      if not 'cmd' in args:
        return

      if args['cmd'] == 'get':
        response = self.get_quest(args)
        self.write(response)
        return

      if args['cmd'] == 'answer':
        response = self.answer_quest(args)
        self.write(response)
        return

application = tornado.web.Application([
  (r'/', MainHandler),
  ], **settings)

main_loop = None

if __name__ == "__main__":
    try:
      http_server = tornado.httpserver.HTTPServer(application)
      http_server.listen(PORT)
      main_loop = tornado.ioloop.IOLoop.current()

      print ("Tornado Server started")
      main_loop.start()
    except:
      print ("Exception triggered - Tornado Server stopped.")

