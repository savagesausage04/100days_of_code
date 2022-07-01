import art
print(art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("So now's your time to shine. Choose, would u like to go left or right?\n")
lower_left_or_right = left_or_right.lower()
if lower_left_or_right == "left":
    swim_or_wait = input("Your stranded! Would you like to wait for a boat or swim across?\n")
    lower_swim_or_wait = swim_or_wait.lower()
    if lower_swim_or_wait == "wait":
        rby = input("Now you are faced with three doors. Choose a door: red, yellow, or blue?\n")
        lower_rby = rby.lower()
        if lower_rby == "yellow":
            print("Wow, you made it! You captured the treasure!")
        else:
            print("Womp, womp. You die, game over!")
    else:
        print("Womp, womp. You die, game over!")

else:
    print("Womp, womp. You die, game over!")
