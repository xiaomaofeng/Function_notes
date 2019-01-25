#number_writer.py
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

#number_reader.py
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

#if you want to process the string instead of the file,you can use the json.dumps() to process the string.
import json

data = {'name' : 'ACME', 'shares' : 100, 'price' : 534.12}
json_str = json.dumps(data)