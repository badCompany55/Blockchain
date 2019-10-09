import hashlib
import requests
import json
from uuid import uuid4

import sys


# TODO: Implement functionality to search for a proof 

coins_mined = 0
node_identifier = str(uuid4()).replace('-', '')
get_u_r_l = "http://0.0.0.0:5000/last_block"
post_u_r_l = "http://0.0.0.0:5000/mine"

def find_proof(block):
    block_string = json.dumps(block, sort_keys=True)
    proof = 0
    while valid_proof(block_string, proof) is False:
        proof += 1
    # return proof
    print(proof)
    return proof

def valid_proof(block_string, proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param block_string: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    if guess_hash[:6] == "000000":
        return True
    else:
        return False
    # TODO
    # return True or False

while True:
    r = requests.get(url = get_u_r_l)

    print("Finding Proof")
    proof = find_proof(r.json())
    print("Found Proof")
    print("Sending to Mine")
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    dat = {"proof": proof, "node_identifier": node_identifier}
    rp = requests.post(url = post_u_r_l, data = json.dumps(dat), headers=headers)
    if rp.status_code == 200:
        coins_mined += 1
        print(f'Coin Count = {coins_mined}')







if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # Run forever until interrupted
    # while True:
    #     # TODO: Get the last proof from the server and look for a new one
    #     # TODO: When found, POST it to the server {"proof": new_proof}
    #     # TODO: We're going to have to research how to do a POST in Python
    #     # HINT: Research `requests` and remember we're sending our data as JSON
    #     # TODO: If the server responds with 'New Block Forged'
    #     # add 1 to the number of coins mined and print it.  Otherwise,
    #     # print the message from the server.
    #     pass
