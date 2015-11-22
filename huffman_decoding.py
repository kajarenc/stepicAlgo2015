initial_input = input()
array_input_tokens = initial_input.split()
letters_count = int(array_input_tokens[0])
encoded_string_length = int(array_input_tokens[1])
points = []
d = {}
for inp in range(0, letters_count):
    pair_input = input()
    pair_input = pair_input.split(':')
    symbol = pair_input[0]
    code = pair_input[1][1:]
    d[code] = symbol

encoded_string = input()
encoded_string = str(encoded_string)

res = ''

while len(encoded_string):
    for code in d.keys():
        if encoded_string.startswith(code):
            res += d[code]
            encoded_string = encoded_string[len(code):]

print(res)
