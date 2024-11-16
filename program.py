#print if 3 student ffails or passes based on if they  get a total percentage of 45percent



subjects = ["hindi", "english", "maths"]
students = []

for i in range(3):
    marks = [int(input(f"Enter marks of student {i+1} in {subject}: ")) for subject in subjects]
    students.append(sum(marks))
    print(marks)
for i,total in  enumerate(students,1):
  if total >= 45:
    print(f"student {i} passes  with {total} marks")
  else:
    print(f"student {i} fails with  {total} marks")




