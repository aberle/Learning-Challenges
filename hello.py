from flask import Flask, request
app = Flask(__name__)

@app.route('/find', methods=['GET'])
def find():
    courseNumber = request.args.get('course')
    if courseNumber == None:
        return 'No course specified, please try again'

    content = 'Find the classroom for ' + courseNumber + '...'
    if courseNumber == 'CSCI1300':
        roomNum = 'ATLAS 100'
    elif courseNumber == 'CSCI2240':
        roomNum = 'ITLL 1B50'
    else:
        roomNum = 'Sorry. No result for ' + courseNumber

    return content+roomNum

@app.route('/notification')
def notification():
    return 'Get a notification. To be implemented'

if __name__ == '__main__':
    app.run(debug=True)