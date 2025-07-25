# 1. Create a variable to store the score
# 2. Check whether score is in range between 90 - 100 (). If yes the student got 'A'
# 3. If notcheck whether score is in range between 80 - 89. If yes the student got 'B'
# 4. same approach for 70-79 and 60 - 69 for grades 'C' and 'D' respectively
# 5. If student scrore is less than 60 then student is failed - 'F'

score = 90
if score <= 90 and score >= 100 :
    print('A')
elif score >= 80 and score <= 90:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
else:
    print('F')