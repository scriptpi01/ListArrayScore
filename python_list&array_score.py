#Lab5_1650700238_Manopakorn

#Tables
print("="*46)
print('| %s %s %s |'%('***', 'Welcome Manopakorn Kooharueangrong', '***'))
print('| %s %28s %9s |'%('***', 'Computer Programming I', '***'))
print("="*46)

#Input
list_score = []
list_score_pass = []
for i in range(10):
  score = eval(input("Please enter score#%2d : "%(i+1)))
  score = score/1
  if score >= 0 :
    list_score.append(score)
  if score >= 50:
    list_score_pass.append(score)
  else:
    pass

#AVG
total = 0
for i in range(len(list_score)):
  total += list_score[i]
avg = total / len(list_score)

#AVG_PASSED
total_passed = 0
for i in range(len(list_score_pass)):
  total_passed += list_score_pass[i]
avg_passed = total_passed / len(list_score_pass)

#SORTED_LIST
list_score.sort(reverse=True)
list_score_sorted = list_score

#Ouput
print("="*46)
print('| %17s %s %-17s |'%('***', 'Result', '***'))
print("="*46)
print("Amount of scores : %d"%len(list_score))
print("Average Score : %.2f"%avg)
print("Height Score  : %.2f"%max(list_score))
print("Lowest Score  : %.2f"%min(list_score))
print("="*20)
print("Total Passes Student : %d"%len(list_score_pass))
print("Average Passed score : %.2f"%avg_passed)
print("="*20)
print("Scores list: %s"%list_score_sorted)