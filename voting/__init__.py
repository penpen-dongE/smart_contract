import os
import json
from flask import (Flask, 
                    render_template,
                    redirect,
                    url_for,
                    request)
from web3 import Web3

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
CONTRACT_DATA_JSON = 'Voting_data.json' 
data_path = os.path.join(ROOT_DIR, CONTRACT_DATA_JSON) 
with open(data_path, 'r') as json_file: 
    json_data = json.load(json_file) 
abi = json_data['abi'] 
address = json_data['contract_address'] 
ganeche_url = "HTTP://127.0.0.1:7545" 
w3 = Web3(Web3.HTTPProvider(ganeche_url)) 
w3.eth.defaultAccount = w3.eth.accounts[1] 
voting = w3.eth.contract( abi =abi, address =address)

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    info = []
    number_of_candidates = voting.functions.get_number_of_candidates().call()
    for i in range(number_of_candidates):
        info.append(votinf.functions.get_candidate_indp(i).call())

    return render_template('index.html', info=info)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return redirect(url_for('index'))
    elif request.method == 'POST':
        address = request.form['address']
        name = request.form['name']
        tx_hash = voting.functions.add_candidate(
            name).transact({'form': address})
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        return redirect(url_for('index'))