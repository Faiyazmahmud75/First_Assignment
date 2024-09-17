import random
num = random.randint(1, 100)
user_input = None
iterCount = 0
while num != user_input:
    try:
        user_input = int(input("Enter Your Guess"))
        if user_input > num:
            if user_input > 100:
                print("Guess under 100")
            else:
                print("Too high!")
            iterCount += 1
        elif user_input < num:
            if user_input < 1:
                print("Guess at least above 1")
            else:
                print("Too low!")
            iterCount += 1
        elif user_input == num:
            iterCount += 1
            if iterCount == 1:
                print("Congratulations! You've guessed the number in First attempt! \nBe proud of yourself!")
            else:
                print("Congratulations! You've guessed the number in", iterCount, "attempts" )
        else:
            print('Please input a valid number')
    except ValueError:
        print('Please input a valid Number')