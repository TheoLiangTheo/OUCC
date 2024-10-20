def encoded(strinput):
    letters = {}
    ans = ''
    for x in range(len(strinput)):
        l = strinput[x]
        if l in letters:
            letters[l] = letters[l] + 1
        else:
            letters[l] = 1
    for keys in letters:
        ans = ans + keys + str(letters[keys])
    return ans

strinput = sorted(list(input()))
answer = encoded(strinput)
print(answer)