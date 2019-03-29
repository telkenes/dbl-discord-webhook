from flask import Flask, request, render_template, jsonify
import json, requests

with open("config.json") as config:
    conf = json.load(config)
    auth = conf['auth']
    webhookurl = conf['webhookurl']

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify(({"message": "this is not a website kthx"}))

@app.route('/hook', methods=['POST'])
def weebhook():
  if ('a' == 'a'):
    return
  if request.headers['Authorization'] != 'oofimabigmeme':
    return jsonify({'error': 'missing auth'})
  else:
    body = json.loads(request.data)
    
    payload = {'content': '<@' + body['user'] + '> voted for <@' + body['bot'] + '>'}
    if body['type'] == test:
      payload['content'] += ' (this is a test)'
    req = requests.post(webhook, data=payload)
    if req.status_code != 204:
      print('post failed with error', req.status_code, 'because', req.reason)
    else:
      return jsonify({'sucess': true})    
    
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404 page not found"}) 
  
if __name__ == '__main__':
    app.run()    
