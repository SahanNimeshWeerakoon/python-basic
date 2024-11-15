name = input("Enter your name: ")
indexNumber = input("Enter your index: ")
numberOfSubjects = input("Enter the number of subjects.")
subjectMarks = []

for i in range(int(numberOfSubjects)):
    subject = input(f"Enter the subject number {i+1}:")
    mark = input(f"Enter {subject} marks:")
    subjectMarks.append({ "subject": subject, "mark": mark })

print("================================================================")
print(f"{name} with index number {indexNumber}, sat for {numberOfSubjects} subject/s.")

for index, subjectMark in enumerate(subjectMarks):
    mark = int(subjectMark["mark"])
    subject = subjectMark['subject']
    if mark >= 90:
        print(f"{index+1}) {subject} - A({mark})")
    elif mark >= 80:
        print(f"{index+1}) {subject} - B({mark})")
    elif mark >= 70:
        print(f"{index+1}) {subject} - C({mark})")
    elif mark >= 60:
        print(f"{index+1}) {subject} - S({mark})")
    else:
        print(f"{index+1}) {subject} - S({mark})")


customers = { "name": "Customer name", "age": 20 }