arr_a = [456, 361, 424, 67, 661]


arr = { 'one': 'Hello', 'two': 'Hi', 'three': arr_a }

import _pickle

import json

fw = 't.dat'
with open(fw, 'wb') as outfile:
    _pickle.dump(arr, outfile)


with open(fw, 'rb') as infile:
    out_arr = _pickle.load(infile)
    print('Got arr from file: ' + str(out_arr))


fw = 't.json'
with open(fw, 'w') as outfile:
    json.dump(arr, outfile)


with open(fw, 'r') as infile:
    out_arr = json.load(infile)
    print('Got arr from json file: ' + str(out_arr))
