userNumber = int(input("Enter a natural number:"))
counter = 0
while userNumber > 1:
        if userNumber % 2 == 0:
            userNumber = userNumber // 2
            print(userNumber)
    
        else:
            userNumber = 3 * userNumber + 1
            print(userNumber)
        counter += 1
print(counter, "steps to reach 1")