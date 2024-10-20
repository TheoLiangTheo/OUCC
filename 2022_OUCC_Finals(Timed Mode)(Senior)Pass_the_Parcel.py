n = int(input())
players = []
for x in range(n):
  players.append(0)
presents = input().split('x')
for x in range(len(presents)):
  if presents[x] == '1':
    players[x%n] += 1
print(max(players))