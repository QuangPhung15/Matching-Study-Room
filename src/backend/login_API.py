from flask import Flask, request, jsonify
from flask_cors import CORS
import mongo_hook as mgh 
import login_config as cf 

app = Flask(__name__)
CORS(app)

@app.route('/create', methods=['POST'])
def createNewAcc():
    data = request.json 
    mgh.insert_one_DB(cf.database, cf.usrInfoCollection, data)

@app.route('/authenticate', methods=['POST'])
def authenticateUsrAcc():
    data = request.json 

    query = mgh.query_document(cf.database, cf.loginCollection, data)

    if (query):
        result = {"auth": True}
    else:
        result = {"auth": False}

    return jsonify(result), 200

@app.route('/forgetPassword', methods=['POST'])
def changePassword():
    data = request.json 

    mgh.update_one_doc()

if __name__ == '__main__':
    app.run(port=5002)
