
temp = raw_input('Which Day?')

input_file = open(temp + 'input', 'r')

array = []

for line in input_file:
    array.append(line.strip('\n'))


print array