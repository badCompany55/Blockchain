import json
import hashlib

first_transaction = {
    # if time loses 10 dollars, someone somewhere else should gain 10 dollars
    "tim": -10,
    "steve": 10
}

# need to hash this transaction
# cant hash an object, need to turn it to a string first

first_hash = hash(json.dumps(first_transaction))

#how to find a hash that starts with 00?
#make lots of guesses/hash until we find the pattern we want

proof = 0
guess = str(first_hash) + str(proof)
# hashlib.sha256(guess.endcode()) -> .hexdigest() #provides a way to see the hashed object
while hashlib.sha256(guess.encode()).hexdigest()[:2] != "00":
# while hashlib.sha256(f'{first_hash}{proof}').hexdigest()[:2] != "00":
    proof += 1
    guess = str(first_hash) + str(proof)
print(f'proof = {proof}')


# combine proof with the hash

second_transaction = {
    "javier": -20,
    "zach": 20,
    "proof": proof,
    "previous_hash": first_hash
    #contains the first transaction
}

second_hash = hash(json.dumps(second_transaction))

# second_proof = ...
# third_transaction = {
#     "josh": -30,
#     "john": 30,
#     "proof": second_proof,
#     "previous_hash": second_hash
#     # now contains the second hash
# }

# third_hash = hash(json.dumps(third_transaction))


