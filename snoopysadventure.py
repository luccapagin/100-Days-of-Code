print('''
*******************************************************************************
          .o.
          |  |    _   ,
        .',  L.-'` `\ ||
      __\___,|__--,__`_|__
     |    %     `=`       |
     | ___%_______________|
     |    `               |
     | -------------------|
     |____________________|
       |~~~~~~~~~~~~~~~~|
       | ---------------|  ,
   \|  | _______________| / /
\. \,\\|, .   .   /,  / |///, /
*******************************************************************************
''')
print("You're Snoopy.")
print("You're bored. Find Woodstock!")

left_right = input(
    "Where could that bird be? Do you want to go left or right? Type L for Left and R for Right.\n"
)
if left_right == "L":
    swim_or_wait = input(
        "You are in front of a lake. Should you Swim (type S) or Wait for a boat(type W)?\n"
    )
    if swim_or_wait == "S":
        print(
            "You were bitten in the butt by an angry trout and ran home crying. Game Over."
        )
    else:
        friends = input(
            "You got to the park. You see three friends: Charlie Brown is looking bummed, Linus lost his favorite blanket and Schroeder is playing some tunes. Which one do you want to ask about Woodstock? Type C for Charlie Brown, L for Linus and S for Schroeder."
        )
        if friends == "C":
            print(
                "Charlie Brown is looking bummed because Woodstock wouldn't stop talking in his ear! You found your friend! Actually, you found two of them! You win!"
            )
        elif friends == "L":
            print(
                "Linus is looking for his favorite blanket and dragged you to look with him. You can't say no! Now you're even more bored. Game Over. "
            )
            print("")
        else:
            print(
                "Schroeder made you listen to one of his long piano pieces. Sounds nice, but you couldn't find Woodstock. Game Over!"
            )
else:
    print("You fell into a hole. Ouch! Game Over.")
