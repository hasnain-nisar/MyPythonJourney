# Break Statement:

# break statement is used to exit the loop prematurely i.e. loop stop running before it has completed all of its iterations.

for i in range(1, 6):
    if i == 3:
        break # Exit the loop here.
    print(i)

# Continue statement:

# The continue statement skips the current iteration of a loop and moves to the next iteration. The loop doesnot terminate but continue with the next cycle.

for i in range(1, 10):
    if i == 6: # Skip this iteration.
        continue
    print(i) 

# pass statement

# The pas statement do nothing an dis used as a placeholdere. It's useful in situation where the syntax requires a statement but you don't want to execute any code.

for i in range(1, 10):
    if i == 3:
        pass  # When i is 3, the pass statement is executed, which does nothing. 
    print(i) # The loop continues as usual
