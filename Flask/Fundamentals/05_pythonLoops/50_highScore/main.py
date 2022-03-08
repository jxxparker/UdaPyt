#High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for scores in student_scores:
  if high_score < scores:
    high_score = scores
    # print(high_score)
  
print(f"the highest score in the class is {high_score}")
