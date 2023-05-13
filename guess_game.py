secret_number = 9
guess_count = 0   
guess_limit = 3                                    
while guess_count < guess_limit:
    guess = int(input("Guess number "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats! you picked up the right one")
        break
else:
        print("You failed, you can only guess thrice")
    


