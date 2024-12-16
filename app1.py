from flask import Flask,request,jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def func1():
    return f'Hello world'

def toDate(dateString):
     return datetime.strptime(dateString, "%Y-%m-%d").date()



@app.route("/gettest",methods=['GET'])
def get_test():
    val1 = request.args.getlist("val1",type = int )
    val2 = request.args.getlist("val2", type=str)
    # dateval = request.args.get('start', type=toDate)

    start = request.args.get('start')

    # Check if the start parameter is provided and is in the correct format
    if start is None:
        return jsonify({"error": "start parameter is required"}), 400

    try:
        # Convert start parameter to a date object
        start_date = datetime.strptime(start, '%Y%m%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYYMMDD."}), 400


    return f'Вернулось {val1=}, {val2=}, {start_date.date()}'

if __name__ == '__main__':
    app.run(debug=True)

#
# def toDate(dateString):
#     return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()
#default=datetime.now()#
# @app.route()
# def event():
#     ektempo = request.args.get('start', default = datetime.date.today(), type = toDate)
#     ...


# http://127.0.0.1:5000/gettest?val1=11&val1=22


