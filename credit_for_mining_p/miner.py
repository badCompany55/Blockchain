# Paste your version of miner.py from the communication_gp
# or client_mining_p folder here (we don't make any changes)

import hashlib
import requests
import json
from uuid import uuid4

import sys


# TODO: Implement functionality to search for a proof 

coins_mined = 0
node_identifier = str(uuid4()).replace('-', '')
get_u_r_l = "/last_block"
post_u_r_l = "/mine"
node_u_r_l = "/nodes/register"
data = {}
data['id'] = node_identifier

def test_for_file(file):
    try:
        f = open(file)
        f.close()
        return True
    except FileNotFoundError:
        return False


if test_for_file("../my_data.txt") == True:
    with open("../my_data.txt") as json_file:
        data = json.load(json_file)
        node_identifier = data['id']
else:
    with open("../my_data.txt", 'w') as output_file:
        json.dump(data, output_file)



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

if __name__ == '__main__':
    # What node are we interacting with?
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    if len(sys.argv) > 1:
        node = f'http://localhost:{sys.argv[1]}'
    else:
        node = "http://localhost:5000"

    if node == "http://localhost:5001":
        other_node = "http://localhost:5000"
    else:
        other_node = "http://localhost:5001"

    node_data = {"nodes": [other_node]}
    rn = requests.post(url = node + node_u_r_l, data = json.dumps(node_data), headers=headers)

    while True:
        r = requests.get(url = node + get_u_r_l)

        print("Finding Proof")
        proof = find_proof(r.json())
        print("Found Proof")
        print("Sending to Mine")
        dat = {"proof": proof, "node_identifier": node_identifier}
        rp = requests.post(url = node + post_u_r_l, data = json.dumps(dat), headers=headers)
        if rp.status_code == 200:
            coins_mined += 1
            print(f'Coin Count = {coins_mined}')
