# ifelse.py

score = int(input("Enter scores:"))

if 90<= score <= 100:
    grade = "A"
elif 80<= score < 90:
    grade = "B"
else:
    grade = "C"

print("Grade is ", grade)
