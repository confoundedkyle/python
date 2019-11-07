# A student makes honour roll if their average is >= .85
# AND thier lowest grade is not below 70

gpa = float(input('What was your Grade Point Average? '))

# Same result as above, easier to read but more lines of code
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print ('You made the honour roll')