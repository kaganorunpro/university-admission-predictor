gpa = float(input("Enter GPA: "))
ielts = float(input("Enter IELTS Score: "))
sat = float(input("Enter SAT Score: "))

score = (gpa * 0.4) + (ielts * 5) + (sat * 0.02)

chance = min(score, 100)

print(f"Admission Chance: {chance:.1f}%")