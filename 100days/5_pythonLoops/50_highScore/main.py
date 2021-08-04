student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


highest_score = 0
for score in student_scores:
    if score > highest_score: #checks if current is higher than before
        highest_score = score   #eventually will stop when highest is set
print(f"the highest score is {highest_score}")
    

