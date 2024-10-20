wins = input().split(' ')
scores = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0}
last_letter = 123
highest_points = 0
for x in range(len(wins)):
  current_letter = wins[x]
  scores[current_letter] += 1
  if current_letter == last_letter:
    scores[current_letter] += 1
  if scores[current_letter] > highest_points:
    highest_points = scores[current_letter]
  last_letter = current_letter
print(highest_points)
