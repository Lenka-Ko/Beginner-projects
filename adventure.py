while True:
    print("You are in a dark room.\n"
          "There is a door to your right and left.\n"
          "Which one do you choose ? (right/left)")
    answer = input("> ")

    if answer.lower().strip() == "right":
        print("You find your self in another room.\n"
              "There are two weapons, hammer and a bow.\n"
              "Which do you take ? (hammer/bow)")
        answer = input("> ").lower().strip()

        if answer.lower().strip() == "hammer":
            print("Right behind you there is shaping a dark shadow. Darker than a night in the room!\n"
                  "The shadow is reaching his long skinny fingers around your shoulders "
                  "and digging his sharp rotting nails into your flesh.\n"
                  "Will you stay still or will you attack ? (stay still/attack)")
            answer = input("> ").lower().strip()

            if answer.lower().strip() == "stay still":
                print(
                    "The shadow´s head is calmly reaching your ear and barely moving his lips, "
                    "he whispers: dig deeper.\n"
                    "When you turn around to face the shadow, you see nothing but darkness.\n"
                    "Would you rather continue a next door, or search the room? (continue/search)")
                answer = input("> ").lower().strip()

                if answer.lower().strip() == "search":
                    print("You are examining the walls hopping you find a secret chamber.\n"
                          "When you walk towards the last wall to investigate, the floor rumbles.\n"
                          "You stoop to the spot and through floor cleft you feel an air on your face. \n"
                          "There it is. Tha way out.\n"
                          "You swing the hammer and crash the floor till you see ground.\n"
                          "You pull yourself through the hole and reach freedom! Congratulations! You survived!")
                else:
                    print("You enter to a new room. Ouch ! Something tweaked your neck.\n"
                          "Ouch! Again!\n"
                          "You touch the spot on your neck, there is something in the wound.\n"
                          "You pull it out. It is a small arrow.\n"
                          "Your t-shirt is soaking blood running from your neck. You feel dizzy and tired\n"
                          "You try to do one more step but you fall on the floor. "
                          "Close your eyes. You do not need to fight anymore.\n"
                          "You died. Game over.")

            elif answer.lower().strip() == "attack":
                print("You rinse the hammer to the left exactly where you expect the shadow has his head.\n"
                      "But you hit only empty air.\n"
                      "Suddenly you feel something heavy is pushing on your shoulders.\n"
                      "You try to resist, but it so heavy so you bend down on your knees.\n"
                      "You raise your head to the ceiling to see, what you wrestle with. "
                      "But only thing you can see is throat of a dark shadow.\n"
                      "You died. Game over.")

        elif answer.lower().strip() == "bow":
            print("You hear a caw. Is it from a next room?\n"
                  "You press your ear on a wall. The cackle is echoing the walls. You cannot say which direction. \n"
                  "It is here! It is in the room!\n"
                  "Black crows are filling the room. You cannot see the walls.\n"
                  "Ten, fifty, hundreds of crows! Fear. Cut your skin! Peck your eyes!\n"
                  "You fight or you die! (fight/die)")
            answer = input("> ").lower().strip()

            if answer.lower().strip() == "die":
                print("Sharp beaks are cutting your skin like hundreds of scalpels.\n"
                      "By every pinch you are weightless and thinner, "
                      "every bite of your flesh makes you disappeared of this world.\n"
                      "You cover your eyes by your hands. You hope they keep your eyes as last.\n"
                      "In complete submission you lay down to floor to let the crows to finish their job.\n"
                      "Silence. The croaking stopped. You hear rustling trees in the wind. "
                      "You feel warm air on your wounded skin.\n"
                      "You open your eyes and see a dark sky and moon. Where is the room?\n "
                      "You look around yourself but do not see any building\n"
                      "Congratulations! You survived! Game over.")
            else:
                print("You shoot an arrow by arrow. You kill one crow, two crows...maybe ten crows.\n"
                      "Beaks are still cutting your skin. You feel exhausted."
                      "Your last arrow. You cannot win.\n"
                      "Your body is heavy, you kneel on the floor. Then you lie down.\n"
                      "You are dying. Feast for the crows. Game over!")

    elif answer.lower().strip() == "left":
        print("You find yourself in another room.\n"
              "There is sitting terrified lonely girl on the floor in the corner. She is crying.\n"
              "Will you talk to her, or continue to next door? (talk/continue)")
        answer = input("> ").lower().strip()

        if answer.lower().strip() == "talk":
            print("You are silently reaching towards the trembling girl.\n"
                  "To comfort the girl, you try to move your hand on her shoulder.\n"
                  "Suddenly a darkness and blast pierced your left eye.\n"
                  "Pain. You feel your hands are covered with a warm liquid. Agony. "
                  "You touch your eye lid, but find only empty hole.\n"
                  "Your last eye concentrates on your hands. Blood.\n"
                  "Then you focus on the girl standing in front of you.\n"
                  "Red and white on her dress. Scalpel in her hand. And on its spike your eye ball.\n"
                  "Game over!")
        elif answer.lower().strip() == "continue":
            print("You open the door and leave the girl behind.\n"
                  "You find yourself in the light room there are no door. But on the floor, there is a phone.\n"
                  "What will you do? (call help/come back)")
            answer = input("> ").lower().strip()

            if answer.lower().strip() == "call help":
                print(
                    "'Fibonacci is sending his regards! Please dial first 6 numbers!' saying the voice in the phone.\n")
                answer = input("Please enter the sequence > ")

                if answer != "0,1,1,2,3,5":
                    print("Fail. Suddenly you feel somebody tapping on you shoulder. The girl.\n"
                          "'0, 1, 1, 2, 3, 5' she says")
                    answer = input("Please enter the sequence separated with comma  > ")

                    if answer != "0,1,1,2,3,5":
                        print("Boooom! The phone exploited in your hand!\n"
                              "You died. Game over!")
                    else:
                        print("Success! Suddenly out from nowhere, there is forming something on the wall.\n"
                              "It is the door!\n"
                              "You try open the door. It is locked!\n"
                              "The girl is tapping on your shoulder. She is holding the key!\n"
                              "You rush towards to door. You are free!\n"
                              "Congratulations. You survived!")
                else:
                    print("Success! Suddenly out from nowhere, there is forming something on the wall.\n"
                          "It is the door!\n"
                          "You try open the door. It is locked!\n"
                          "You feel lost! \n"
                          "Suddenly somebody is tapping on your shoulder. The girl. And she is holding the key!\n"
                          "You rush towards to door. You are free!\n"
                          "Congratulations. You survived!")

            else:
                print("You turn around to walk away. Suddenly the door has disappeared.\n"
                      "There is no way to go.\n"
                      "Suddenly, from the ceiling there are dropping sharp blades piercing every inch of the floor.\n"
                      "You cannot run. You cannot hide.\n"
                      "You died. Game over!")

    break
