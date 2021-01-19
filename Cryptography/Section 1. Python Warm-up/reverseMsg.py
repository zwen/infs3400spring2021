
# Topics included: 
# 1) input()
# 2) String and boolean data type
# 3) while loop

msg = input("Enter a short sentence: ")

translated = ""
i = len(msg) - 1 

# initial value of i
print(i)

# looping to remapping the phrase
while i >= 0:
    translated += msg[i]

    # to see the intermediate result.
    print(translated)
    i -= 1

print(translated)