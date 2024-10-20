string = input()
letter_value = {}
for x in string:
    if x != ' ':
        if x not in letter_value.keys():
            letter_value[x] = 1
        else:
            letter_value[x] = letter_value[x] + 1
maxi = 0
letters = []
for x in letter_value.keys():
    if maxi < letter_value[x]:
        maxi = letter_value[x]
for x in letter_value.keys():
    if letter_value[x] == maxi:
        letters.append(x)
letters.sort()
print(' '.join(letters))
