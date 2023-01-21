def countLetters(output):
    counter = []
    for x in output:
        counter.append(x)
    return len(counter)
        
    
output = input("Please enter a string to HASH: ")    
print(countLetters(output))