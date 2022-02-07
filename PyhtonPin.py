pin = 1234
attempts = 3

while attempts > 0:
    attempts = attempts - 1
    supplied_pin = int(input("Enter your PIN: "))
    if supplied_pin == pin:
        print("Access Granted ")
        break

    print("Incorrect Pin, Try Again")
    print(attempts, "attempts left")
    if attempts == 0:
        print('You have entered your PIN incorrectly too many times')
