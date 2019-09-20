import json
import os
from solcx import compile_files
from web3 import Web3
class Greeter():
   net_url = "HTTP://127.0.0.1:7545"
   web3 = Web3(Web3.HTTPProvider(net_url))
   abi = ''
   bytecode = ''
   data = {'abi': abi}
   @classmethod
   def compile_contract(cls, sol_path, contract_name):
       if sol_path.split('/')[-1].split('.')[-1] != 'sol':
           raise ValueError('You must input .sol file path')
       compiled_sol = compile_files([sol_path])
       contract_key = sol_path + ":" + contract_name
       abi = compiled_sol[contract_key]['abi']
       bytecode = compiled_sol[contract_key]['bin']
       cls.abi = abi
       cls.bytecode = bytecode
       cls.data['abi'] = abi
   @classmethod
   def deploy_contract(cls):
       sol_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'greeter.sol')
       cls.compile_contract(sol_path, "Greeter")
       abi = cls.abi
       bytecode = cls.bytecode
       w3 = cls.web3
       w3.eth.defaultAccount = w3.eth.accounts[0]
       contract = w3.eth.contract(abi=abi, bytecode=bytecode)
       tx_hash = contract.constructor().transact()
       tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
       cls.data['contract_address'] = tx_receipt['contractAddress']
       cls.save_data()
   @classmethod
   def save_data(cls, path='data.json'):
       with open(path, 'w') as outfile:
           json.dump(cls.data, outfile, indent=4, sort_keys=True)
if __name__ == "__main__":
   Greeter.deploy_contract()