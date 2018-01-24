# http://localhost:8000/getreply?key=xxxx&lang=en&input=hola
import tornado.ioloop
import tornado.web
import argparse
import sys
import os
import tensorflow as tf
import time
import logging

from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.basicConfig(level=logging.INFO)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global predictor
        try:
            start = time.time()
            question = self.get_argument('input').strip()
            answer = predictor.predict(question, html_format=False)
            end = time.time()
            res = {'answer':answer,
                   'response time':str((end-start)*1000)+"ms"}
            self.finish(res)
        except Exception as e:
            self.write("Error: %s" % e)

    def post(self):
        print(self.request.remote_ip)
        context = self.get_argument('context')
        self.write("you say: " + context)

def make_app():
    return tornado.web.Application([(r"/getreply",MainHandler)])

if __name__=="__main__":

    model_name = "basic-30000"
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',nargs='?',type=int,default=8000,help='port')

    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')

    sess = tf.Session()
    predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, result_file=model_name)
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    arg = parser.parse_args(sys.argv[1:])
    server.bind(arg.port)
    server.start() # forks one process per cpu   
    print("Web service started.")
    tornado.ioloop.IOLoop.instance().start()