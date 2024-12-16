from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def func1():
    return f'Hello world'

@app.route("/gettest",methods=['GET'])
def get_test():
    val1 = request.args.getlist("val1",type = int )
    val2 = request.args.getlist("val2", type=int)
    return f'Вернулось {val1=}, {val2=}'

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/gettest?val1=11&val1=22


