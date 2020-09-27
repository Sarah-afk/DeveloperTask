from database import db, app, cache, Logs
from flask import request, jsonify, render_template, json, Response
import datetime
import time
from fibonacci import Fibonacci
from database import *

#creating an object of the class Fibonacci
fib_obj = Fibonacci(cache)

#render home page
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

#return the logs (input requests, time of requests, and runtime) and cache status
@app.route('/health', methods = ['POST', 'GET'])
def get_health():
    logs = Logs.query.all()
    logs = [{"input": i.input, "time": i.time, "runtime": i.runtime} for i in logs]

    cached = len(cache.cache._cache)-1
    cached = 0 if cached == -1 else cached
    return jsonify({"cached": cached, "logs": logs})

#return the output whose specified id is in the database
@app.route('/long_fib/<int:id>', methods = ['POST', 'GET'])
def get_long_fib(id):
    log = Logs.query.filter(Logs.id == id).first()
    if log:
        output = log.output
        return Response(output, mimetype="text/plain")
    else:
        return jsonify({"error": "ID not found"}), 401

#returns the output of sequences that add up to the input number
@app.route('/fib/<int:n>', methods = ['POST', 'GET'])
def get_fib(n):
    time1 = int(time.time()*1000)

    is_html = False
    if request.method == 'POST':
        is_html = (request.form["is_html"] == '1')

    prev_run = Logs.query.filter(Logs.input == n).first()
    if prev_run:
        resp = json.loads(prev_run.output)
    else:
        resp = fib_obj.calculate(n)

    resp_dump = json.dumps(resp).replace(' ', '')
    time2 = int(time.time()*1000)

    new_log = Logs(input=n, output=resp_dump, time=time1, runtime=time2-time1)
    db.session.add(new_log)
    db.session.commit()
    
    #when RESTFul API is used, the output is returned directly. However, when the frontend is used, above 10,000 characters  
    #the frontend can't display the output. Instead, a url is given linking to the result. This ensures that the API could be 
    #used as part of a bigger application smoothly, while still ensuring that users of the frontend could access results.
    if not is_html:
        return jsonify(resp)
    if len(resp_dump) > 10000:
        return jsonify({"url_response": "/long_fib/"+str(new_log.id)})
    return jsonify({"response": resp})

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0',port=2224, debug=True, threaded=True)
