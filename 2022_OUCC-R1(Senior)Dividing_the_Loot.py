n = int(input())
answer = 0
necklaces = {}
for x in range(n):
  necklace = input().split(' ')
  necklaces[necklace[0]] = necklace[1]
for x in range(n):
  if x%2 == 0:
    necklaces.pop(max(necklaces.keys()))
  else:
    answer += int(max(necklaces.values()))
    necklaces.pop(list(necklaces.keys())[list(necklaces.values()).index(max(necklaces.values()))])
print(answer)