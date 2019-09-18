from web3 import Web3

ganeche_url = 'HTTP://127.0.0.1:7545' 
web3 = Web3(Web3.HTTPProvider(ganeche_url)) 
print(web3.isConnected()) 
print(web3.eth.blockNumber) 
balance = web3.eth.getBalance('0x044bc7f8CBb7aF97E0aCb964Aa0E890Fa8a4f406') 
print(balance) 
ether = web3.fromWei(balance, 'ether') 
print(ether)