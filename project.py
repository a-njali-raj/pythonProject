answer_yes = ["Yes", "yes", ]
answer_no = ["No",  "no"]

print("""
   >>>>WELCOME! LET'S START THE ADVENTURE<<<

You are standing in a bustop and you see a old women can't able to cross the road and asking for help.
Suddenly a stranger try to steal her bag.

Will you help her. (Yes / No)
""")

ans1 = input(" ")

if ans1 in answer_yes:
    print("\nYou faced a fight with stranger .will you defeat him? (Yes / No)\n")

    ans2 = input("")

    if ans2 in answer_yes:
        print("\nYou are appreciable and the theif was arrested by police.you won the game.GAME OVER")

    elif ans2 in answer_no:
        print("\nThe theif rescued and you fail. GAME OVER")

    else:
        print("oopsss!!! you are a fool!")

elif ans1 in answer_no:
    print("\nshe fall down and theif rescued.The people around there blamed at you.And you are "
          "arrested by the police.Can you convince them?(Yes / No)\n")

    ans3 = input("")

    if ans3 in answer_yes:
        print("\nyou can release from station with a great moral.GAME OVER")

    elif ans3 in answer_no:
        print("\nOpss...... The officers arrest you by considering you as the companion of "
              "theif.!!!!!GAME OVER")

    else:
        print("\noopsss!!! you are a fool!")

else:
    print("\noopsss!!! you are a fool!")