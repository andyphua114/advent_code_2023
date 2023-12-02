import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

# Part 1

all_calibration = []

for line in lines:
    calibration = [i for i in line if i.isdigit()]  # store in list if the string element is digit
    all_calibration.append(calibration)  # append each line of digits into a list

final_value = 0

for val in all_calibration:
    if len(val) == 1:
        code = int(val[0] + val[0])
        final_value += code
    else:
        code = int(val[0] + val[-1])
        final_value += code

print("Answer for Part 1: {}".format(final_value))

# Part 2

digit_list = ["one","two","three","four","five","six","seven","eight","nine"]

help_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

processed = []

for code in lines:
    a = re.split(r'([0-9])', code)
    b = [i for i in a if i != ""]

    new_b = []

    for c in b:
        if c.isdigit():
            new_b.append(c)
        else:
            for d in digit_list:
                if c.find(d) >= 0:
                    new_b.append(c)
                    break

    processed.append((new_b[0], new_b[-1]))

final = []

for i in processed:
    digit_store = [0,""]

    inter = []

    # first "digit"
    if i[0].isdigit():
        inter.append(i[0])
    else:
        for d in digit_list:
            if digit_store[1] == "" and i[0].find(d) >= 0:
                digit_store[0] =  i[0].find(d)
                digit_store[1] = help_dict[d]
            elif i[0].find(d) <= digit_store[0] and i[0].find(d) >= 0:
                digit_store[0] =  i[0].find(d)
                digit_store[1] = help_dict[d]

        inter.append(digit_store[1])

    digit_store = [0,""]

    # second "digit"
    if i[1].isdigit():
        inter.append(i[1])
    else:
        for d in digit_list:
            if len([m.start() for m in re.finditer(d, i[1])]) > 0:
                max_index = max([m.start() for m in re.finditer(d, i[1])])
                if max_index >= digit_store[0] and max_index >= 0:
                    digit_store[0] =  max_index
                    digit_store[1] = help_dict[d]

        inter.append(digit_store[1])

    final.append(inter)

final_value = 0

for val in final:
    code = int(val[0] + val[1])
    final_value += code

print("Answer for Part 2: {}".format(final_value))