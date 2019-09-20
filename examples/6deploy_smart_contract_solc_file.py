import os
from web3 import Web3
from solcx import compile_files

dir_path = os.path.dirname(os.path.realpath(__file__)) 
greeter_path = os.path.join(dir_path, 'greeter.sol') 
# complie 
complied_greeter = compile_files([greeter_path])

greeter_key = greeter_path + ":Greeter" 
greeter_abi = complied_greeter[greeter_key]['abi'] 
greeter_bytecode = complied_greeter[greeter_key]['bin']

ganeche_url = "HTTP://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganeche_url)) 
web3.eth.defaultAccount = web3.eth.accounts[0] 

# deploy contract 
Greeter = web3.eth.contract( abi =greeter_abi, bytecode =greeter_bytecode) 
tx_hash = Greeter.constructor().transact() 
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash) 

# interact contract 
greeter = web3.eth.contract( address =tx_receipt.contractAddress, abi =greeter_abi) 
print(greeter.functions.greet().call()) 
tx_hash = greeter.functions.setGreeting("안녕!").transact() 
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(greeter.functions.greet().call())