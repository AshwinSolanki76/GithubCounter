from flask import Flask,render_template,make_response,request
import Back
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    count=Back.IncrementAndgetCount(request)
    response = make_response(render_template('badge.html',count=count))
    response.headers['Content-Type'] = 'image/svg+xml; charset=utf-8'
    return response

if __name__=="__main__":
    # app.debug=True
    app.run()