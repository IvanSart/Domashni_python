grades = [95, 82, 67, 54, 100, 73, 88, 42]
excellent = []
good = []
pas = []
fail = []
for i in grades:
    if int(i) >= 90:
        excellent.append(i)
    elif int(i) >= 70 and int(i) <= 89:
        good.append(i)
    elif int(i) >= 50 and int(i) <= 69:
        pas.append(i)
    else:
        fail.append(i)
print("Excellent grades: ", excellent)
print("Good grades: ", good)
print("Pass grades: ", pas)
print("Fail grades: ", fail)