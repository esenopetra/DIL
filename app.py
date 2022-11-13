from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__ , static_url_path='/static')
from daytoday import daylived

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def calculate():
    f=''
    s=""
    md=31
    mm=12
    z=0
    bd=int(request.form.get("BD"))
    bm=int(request.form.get("BM"))
    by=int(request.form.get("BY"))
    if bd > md or bm > mm or bd == z or bm==z or by==z:
        s="Check Input"
        return render_template('index2.html',output=s)
    else :
        f=daylived(bd,bm,by)
        return render_template('index2.html',output=str(f))








if __name__ == '__main__':
        app.run(debug=True)
