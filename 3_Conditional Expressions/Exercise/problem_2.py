# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

# marks1 = int(input('Enter Marks 1: '))
# marks2 = int(input('Enter Marks 2: '))
# marks3 = int(input('Enter Marks 3: '))

# # Check for total percentage.

# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
#     print(f'Congratulation! You have passed this class, and your total percentage is {total_percentage}')

# else:
#     print(f"You failed, try again next year, your percentage is {total_percentage}")


# More concise code

marks = [float(input(f"Enter your marks {i+1}: ")) for i in range(3)]

# Calculate total percentage.
total_percentage = sum(marks) / 3

# Check if student passed or failed.

if total_percentage >= 40 and all(mark>=33 for mark in marks):
    print(f"The studnet has passed with {total_percentage} percentage.")

else:
    print(f"Student failed with {total_percentage} percentage.")