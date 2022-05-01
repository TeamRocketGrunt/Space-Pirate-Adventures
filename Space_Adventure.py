# Input Section:
name = input("What is your name? ")
nicknameAdj = input("Name an adjective that starts with the same letter as your name, i.e. Angry Avery, Timid Tom. ")
bodyPart = input("What is your favorite body part? It can be an organ that humans don't usually have. ")
faveColor = input("What is your favorite color? ")
weaponPref = input("Laser guns or swords? ")
favePlanet = input("What is your favorite planet? ")


# Output Section:
# The breaks denote paragraphs even though it doesn't effect the output
def main():
    print("You watch as the sun sets behind the horizon of", favePlanet, ". You're the famous spacefaring pirate", nicknameAdj, name, "adorned in your", faveColor, "armored space suit.",
    "You're known well throughout the solar system, made all the more recognizeable by your synthetic", bodyPart, ". Despite fame, or perhaps because of it, you've fallen on hard times.",
    "Your crew is small, your ship is rickety. She's a modified mining shuttle, a bow covered in grabbers to harvest asteroids and guns tucked under false pannels.",
    "Between scrapes and patches she's painted the same", faveColor, "as your armor.")

    print("\nBy some stroke of luck your radar pings, two transponders were detected on orbits similar to yours. It's just what you needed.",
    "Skipper Henry reads off the ship details: 'There's a freelance freighter, no manifest available, and a Junker Scout Ship. She's a mean lookin' one too.'",
    "You feel the weight of your", weaponPref, "on your hips as your anticipation rises. You feel your age as wounds around your", bodyPart, "ache.",
    "The freighter is a gamble, if they're hauling a load of hydrogen chips you could fuel an escape and live on the profits for a year.",
    "Of course, they could be shipping helium and you'd be lucky to have lunch money next week.")

    print("\nThe Junker Scout Ship is dangerous, guns aplenty line their hull. If they can't find junk they make it.",
    "Junker ships always have lots of supplies though. If you successfully raid these guys you'd get more than a full hydrogen tank.",
    "You have to raid one of these ships. You can't raid both, their orbits are diverging, drifting further away from each other- and you.",
    "You'll be dead in water if you can't get some cargo tonight.")
          
    bridge_command()


def bridge_command():
    nextStep = input("You can choose to raid a ship or talk to your crew. What do you do? ")
    if ("elp" in nextStep):
        print("Type a command like 'Talk to crew' or 'raid freighter'")
        bridge_command()

    # If talk is typed:     
    elif ("alk" in nextStep):
        crew_chat()

    # If raid is typed
    elif ("aid" in nextStep):
        raid_who(nextStep)
        
    else:
        print("Sorry, I don't understand")
        print("Type 'help' for assistance")
        bridge_command()
        

# This will give crew dialogue about who they want to attack, how and why...
def crew_chat():
    print("\nHenry turns to look at you. 'I don't like our chances in a fight with the junkers, we should scan them and see if there's any way to sneak up on them.'"
          "\nThe gunner, Daisy, cracks her knuckles. 'If we get the drop on them we could take either one, I can take out the engines and as long as Henry keeps us in "
          "their blind spot they shouldn't get a chance to shoot back. The freighter is easy to disable, they'll be sitting ducks.")
    print("\n'I don't know what these two are thinking, we're in no condition to fight. We should take our chances with the freighter and not risk our asses,' the engineer, Roland, says. "
          "\n'I dunno, they're just doing an honest days work. Junkers can be pretty mean, for all we know the scout's gonna grab the colony to take out that freighter. Hell, they're worse than us.")
    step2 = input("The scanner station is to your left, displaying a readout of both ships. To your right Sarah is scanning the radio. (Type 'help' for options)")


# This is called if the user types any string containing "raid" and checks for ship names:
# Parameter target_ship: the string the user typed
def raid_who(target_ship):
    if ("unker" in target_ship):
        print("This will be the junker raid prompt")
    elif ("reight" in target_ship):
        print("this will be the freighter raid prompt")
    else:
        whichShip = input("Which ship? The Junkers or the Freighter? ")
        if ("unk" in whichShip):
            print("this will be the junker raid prompt")
        elif ("reig" in whichShip):
            print("this will be the freighter raid prompt")
        else:
            print("Sorry, I don't understand.")
            targetShip = input("Which ship do you want to raid?")
            raid_who(targetShip)
    



main()
