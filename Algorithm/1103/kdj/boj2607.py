# word_num = int(input())
# word_list = [input() for _ in range(word_num)]
# first_word = word_list[0]
# answer = 0

# for word in word_list[1:]:
#   points = 0
#   for char in first_word:
#     if char in word:
#       points += 1
#   if points >= len(first_word)-1 and points <= len(first_word)+1:
#     answer += 1

# print(answer)

word_num = int(input())
word_list = [input() for _ in range(word_num)]
first_word = list(word_list[0])
answer = 0

for word in word_list[1:]:
  points = 0
  compare = first_word[:]
  for char in word:
    if char in compare:
      compare.remove(char)
    else:
      points += 1
  if points <= 1 and len(compare) <= 1:
    answer += 1

print(answer)