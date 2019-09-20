import json
from web3 import Web3
from solcx import compile_standard

compiled_sol = compile_standard({ 
    "language": "Solidity", 
    "sources": {"Greeter.sol": { 
        "content": ''' 
            pragma solidity ^0.5.0;
            
            contract Greeter { 
                string public greeting;
                constructor() public { 
                    greeting = 'Hello'; 
                } 
                function setGreeting(string memory _greeting) public { 
                    greeting = _greeting; 
                } 
                function greet() view public returns (string memory) { 
                    return greeting; 
                }
            } 
        '''}
}, 
"settings":  {"outputSelection": {"*": {"*": ["metadata", "evm.bytecode", "evm.bytecode.sourceMap"]}}}
})

ganeche_url = "HTTP://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganeche_url)) 
web3.eth.defaultAccount = web3.eth.accounts[0]

greeter_abi = json.loads( 
    compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi'] 
greeter_bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object'] 
Greeter = web3.eth.contract( abi =greeter_abi, bytecode =greeter_bytecode) 

# deploy contract 
tx_hash = Greeter.constructor().transact() 
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash) 

# connect contract 
greeter = web3.eth.contract( 
    address =tx_receipt.contractAddress, abi =greeter_abi)
print(greeter.functions.greet().call())
tx_hash = greeter.functions.setGreeting("안녕!").transact() 
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash) 
print(greeter.functions.greet().call())