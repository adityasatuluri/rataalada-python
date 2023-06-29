import time
import sys
import random

inp = 1
riddle = {
    "justice": "It Can Be Cruel, Poetic, Or Blind...",
    "he lies still": "What Does A Liar Do When He’s Dead?",
    "orphan": "I Grew Up From A Seed, As Tough As A Weed",
    "batman": "What’s black and blue and dead all over?",
    "friends": "The Less Of Them You Have, The More One Is Worth",
    "confusion": "I Am First A Fraud Or A Trick. Or Perhaps A Blend Of The Two",
    "mask": "Fear He Who Hides Behind One",
    "ha": "It's not a joke, but sometimes you need to shout twice to really mean it",
    "joker": "A wildcard in the truest sense"
}

l1 = [
    "It Can Be Cruel, Poetic, Or Blind...",
    "What Does A Liar Do When He’s Dead?",
    "I Grew Up From A Seed, As Tough As A Weed",
    "What’s black and blue and dead all over?",
    "The Less Of Them You Have, The More One Is Worth",
    "I Am First A Fraud Or A Trick. Or Perhaps A Blend Of The Two",
    "Fear He Who Hides Behind One",
    "It's not a joke, but sometimes you need to shout twice to really mean it",
    "A wildcard in the truest sense"
]

response_right = [
    "You're close to the truth.",
    "You're quite the thinker. Now, think about this one.",
    "Good job on this one.",
    "Nice vengeance",
    "Your mind works in exceedingly intelligent ways. Here's another one."
]

response_wrong = [
    "You're trying to unmask the truth, but you're not there yet.",
    "Try harder vengeance.",
    "When you guess wrong, I guess you try again.",
    "You scour the internet for the truth, but you still need to answer me.",
    "Don't sweat it 'V', you can quit any time",
    "You're close. Right on the edge of the answer. I'll give you another shot.",
    "I feel like you're not even trying.",
    "You're not as smart as I thought you were. Try again.",
    "If you want real power, you need the truth. Try again.",
    "That was a wild guess. If you want to win, you must try a little harder."
]

def clear_screen():
    sys.stdout.write("\033[2J\033[1;1H")

def print_prompt():
    print("\033[92m$\033[0m", end=" ")

def cmd():
    time.sleep(1)
    print("\033[92m   POS-0@-3-0-0-CRO1.ARKHAM.GOTHAMDATA.NET     [27.05.19.39]")
    time.sleep(0.75)
    print("   TBR2.N54GHTM.IP.GOTHAMISP2.NET              [01.03.19.40]")
    time.sleep(0.75)
    print("   CR2.N54GTHM.IP.GOTHAMISP2.NET               [58.12.19.41]")
    time.sleep(0.75)
    print("   CR2.GTHMX.IP.GOTHAMISP2.NET                 [140.10.19.48]")
    print("   CR3.GTHMX.IP.GOTHAMISP3.NET                 [405.03.19.87]")
    time.sleep(0.75)
    print("   CORRECTIONS. ARKHAM.GOV                     [258.10.19.74]")
    time.sleep(0.75)
    print("   03.04.20.22                                 [03.04.20.22]")
    time.sleep(1.5)
    print()
    print(">> REROUTING...")
    time.sleep(1.5)
    print()
    print(">> SSH UPSTANDING-CITIZEN@RATAALADA.COM")
    time.sleep(3)
    clear_screen()
    print_prompt()
    print("\033[92m>> I HAVE BEEN EXPECTING YOU. WANT TO PLAY A GAME?")
    time.sleep(1)
    print_prompt()
    print("\033[92m>> PROCEED? [Y/N] - ", end='')
    g = input("\033[92m")
    if g.lower() == 'y':
        riddles()
    elif g.lower() == 'n':
        print_prompt()
        print("\033[92m>> WELL...")
        time.sleep(0.5)
        print("LOOKS LIKE YOU DON'T HAVE WHAT IT TAKES TO PLAY THE GAME...")
        time.sleep(1)
        print("BUT I'LL BE WAITING FOR YOU")
        time.sleep(3)
    else:
        print_prompt()
        print("\033[92mUGH. I know you're too dumb for this.")

def riddles():
    for r in l1:
        c = r
        print()
        print_prompt()
        time.sleep(0.75)
        print("\033[92m" + r)
        q = 1
        while q:
            print_prompt()
            d = input("\033[92m")
            if d in riddle:
                e = riddle.get(d)
                if c == e:
                    print_prompt()
                    print("\033[92m" + random.choice(response_right))
                    q = 0
            else:
                print_prompt()
                print("\033[92m" + random.choice(response_wrong))
    time.sleep(2)
    clear_screen()
    print()
    print_prompt()
    print("\033[92m>> You have solved all my riddles and now a new truth is revealed")
    print_prompt()
    print("\033[92m>> [PRESS ENTER TO COLLECT THE REWARD]", end='')
    qqq = input()
    clear_screen()
    print_prompt()
    print("\033[92m>> shorturl.at/lMU48")
    print_prompt()
    print("\033[92m>> HERE'S A LINK FOR YOU.")
    print()
    print()
    time.sleep(2)
    print("\033[92mYou have reached the end of the game, but some games never end...")

while inp:
    clear_screen()
    print_prompt()
    ssh = input("\033[92m")
    if ssh == "traceroute rataalada.com":
        inp = 0
        cmd()
    else:
        time.sleep(2)
        print_prompt()
        print("\033[92m   traceroute incomplete")
        inp = 1
