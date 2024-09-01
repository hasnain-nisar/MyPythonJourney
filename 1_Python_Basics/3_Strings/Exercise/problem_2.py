# 2. Write a program to fill in a letter template given below with name and date.

letter = '''
            Dear <|Name|>, 
            You are selected! 
            <|Date|> '''

print(letter.replace("<|Name|>", "Hasnain").replace("<|Date|>", "8/10/2024"))