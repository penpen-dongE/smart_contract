from web3 import Web3

ganeche_url = "HTTP://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganeche_url)) 
from_account = "0x044bc7f8CBb7aF97E0aCb964Aa0E890Fa8a4f406" 
to_account = "0xE3E7566f48d0D407a222ff6eA46cc1C926FC2500"
from_private_key = "7d0b79b5853fc7f538e68335d0a584c4d786475141b1e0a2d7c0036949781cd4"

# get the nonce 
nonce = web3.eth.getTransactionCount(from_account)

# build taransaction 
tx = {
    'nonce': nonce,
    'to': to_account,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000, #0.2m,
    'gasPrice': web3.toWei(50, 'gwei')
}

# sign transaction  이 트랜젝션이 유효한지 
signed_tx = web3.eth.account.signTransaction(tx, from_private_key) 

# send transaction 
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction) 

# get transaction hash  트랜젝션이 이루어졌을때 결과 확인
print(web3.toHex(tx_hash))
