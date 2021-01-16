import date
import get

from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['GET'])
def post():
    name = request.args.get('name')
    school = request.args.get('school')
    y = request.args.get('y')
    m = request.args.get('m')
    d = request.args.get('d')
    birth = date.birth(y,m,d)
    y = birth[0]
    m = birth[1]
    d = birth[2]
    birth = y+m+d
    seq = get.memberSeq(name, birth, school)
    if(seq == None):
        msg = "결과가 없습니다"
        return render_template('index.html', msg=msg)
    url = get.mailUrl(name, birth, seq, school)
    return redirect(url)

if __name__ == "__main__" :
    app.run(host = '0.0.0.0', port = 80)