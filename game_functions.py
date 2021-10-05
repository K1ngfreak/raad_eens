from math import e
import random
import time
import os
from slowprint.slowprint import*

def clear():
    command = 'cls'
    os.system(command)

def quit():
    time.sleep(1)
    clear()
    print('--------------------------------------------------------------------')
    slowprint('Thank you for playing this game.', 1)
    slowprint('Made by, Jesse van Vianen', 1)
    slowprint('And Noah Zonneveld, 04-10-2021.', 1)
    slowprint('Signing off...', 1)
    print('--------------------------------------------------------------------')
    time.sleep(1)
    clear()
    exit()

def died():
    time.sleep(3)
    slowprint('You died', 1)
    time.sleep(1)
    slowprint('Do you want to try again?', 1)
    choise1 = input('Y/N: ')
    clear()
    if choise1 == 'Y':
        restart()
    elif choise1 == 'N':
        quit()

def won():
    time.sleep(3)
    slowprint('You won the game!', 1)
    print('')
    time.sleep(1)
    slowprint('press enter to continue', 1)
    input('')
    clear()
    slowprint('There are 4 good endings (wins)', 1)
    slowprint('And there are 6 bad endings (losses)', 1)
    slowprint('Do you want to try again for a different ending?', 1)
    tryAgain = input('Y/N: ')
    if tryAgain == 'Y':
        restart()
    elif tryAgain == 'N':
        quit()

def restart():
    time.sleep(1)
    slowprint('The game will restart', 1)
    time.sleep(1)
    clear()
    main()

clear()

print('=======================================================================')
slowprint('Welcome to the game......', 1)
print('=======================================================================')

print('')
slowprint('press enter to continue', 1)
input('')
clear()

slowprint('First of all, this game is about saving a prisoner from his cell. ', 1)
slowprint('You get a few choices and have to pick one,', 1)
slowprint('If you survive the choices you\'ve made,', 1)
slowprint('You win the game.', 1)
slowprint('If you die along the choices you\'ve made...', 1)
slowprint('You lose!', 1)
slowprint('If you want to restart the game, type: restart', 1)
slowprint('If you want to quit the game, type: quit', 1)
slowprint('Goodluck...', 1)
print('========================================================================')
time.sleep(1)
clear()

for n in range(0,5):
    if n == 0:
        print('--------')
    elif n == 1:
        print('------')
    elif n == 2:
        print('----')
    elif n == 3:
        print('--')
    time.sleep(1)

slowprint('Lets begin the game!', 1)
time.sleep(1)

def main():
    time.sleep(1)
    clear()

    slowprint('You are a person who is captured by the army...', 1)
    slowprint('They tell you to save a soldier who is imprisoned, ', 1)
    slowprint('You dont know what to expect...', 1)
    slowprint('All you know is that you have to survive for your freedom.', 1)
    slowprint('They send you to the place and you end up at a big castle!', 1)
    slowprint('Your first thought is, should I enter this castle?', 1)
    print('--------------------------------------------------------------------')

    slowprint('Do you enter the castle?', 1)
    enterCastle = input('yes / no: ')
    clear()
                                        # entering the castle
    if enterCastle == 'yes':
        slowprint('You have entered the castle', 1)
        slowprint('You see two large metal doors', 1)
        
        slowprint('Which one do you go through?', 1)
        enterDoor = input('door 1 / door 2: ')
        clear()
                                        # entering door 1
        if enterDoor == 'door 1':
            slowprint('You open door 1', 1)
            slowprint('When you enter into the room the door closes behind you', 1)
            slowprint('When the lights go on you see a room full of giant spiders', 1)
            slowprint('You battle the spiders and...', 1)

            time.sleep(1)
            slowprint('You won the battle', 1)
            print('')
            slowprint('Press enter to continue', 1)
            input('')
            clear()

            slowprint('You continue walking and fall through a trapdoor', 1)
            slowprint('You\'re stuck', 1)
            slowprint('You need to think of a way to get out of the pit', 1)
            slowprint('There are a few options on the ground to help you escape', 1)
            
            slowprint('What will you choose', 1)
            choise2 = input('rope / ladder: ')
            clear()
                                        # choosing the rope
            if choise2 == 'rope':
                slowprint('You see a rope, can you use this rope to climb up?', 1)
                slowprint('You somehow get the rope around some wood and start climbing', 1)
                slowprint('But for some reason the rope breaks', 1)
                slowprint('You can barely hold on to something', 1)
                slowprint('you\'re half way up', 1)
                slowprint('You can continue climbing or let yourself drop so you might try again', 1)
                
                slowprint('What will you do?', 1)
                climbDrop = input('climb / drop: ')
                clear()
                                        # you continue climbing
                if climbDrop == 'climb':
                    slowprint('You continue climbing', 1)
                    slowprint('You reach the top', 1)
                    slowprint('You decide to continue looking for the prisoner', 1)
                    slowprint('You continue on and reach a room with a boss', 1)
                    slowprint('You see two weapons lying on the floor', 1)
                    slowprint('One is a sword imbedded with magic', 1)
                    slowprint('The other one is a minigun with 3000 rounds', 1)
                    slowprint('You have enough time to run to one of them and grab it', 1)
                    
                    slowprint('Which weapon do you choose?', 1)
                    weaponChoise = input('minigun / sword: ')
                    clear()
                                        # you choose the minigun
                    if weaponChoise == 'minigun':
                        slowprint('You pick the minigun and start shooting the boss', 1)
                        slowprint('After shooting about half the bullets your weapon overheats', 1)
                        slowprint('You are vulnerable and the boss is charging you', 1)
                        slowprint('You are smart and run away from the boss', 1)
                        slowprint('After circling around the room you run back to the minigun', 1)
                        slowprint('The weapon cooled down and you shoot the boss', 1)
                        slowprint('The boss dies and falls over', 1)
                        time.sleep(1)
                        
                        print('')
                        slowprint('Press enter to continue', 1)
                        input('')
                        clear()

                        slowprint('As you continue walking to look for the prisoner', 1)
                        slowprint('You notice you got stabbed and you\'re slowly losing blood', 1)
                        slowprint('After looking for 5 more minutes you collapse', 1)
                        died()
                            
                                        # you choose the sword
                    elif weaponChoise == 'sword':
                        slowprint('You pick up the sword', 1)
                        slowprint('The boss charges at you and you cut him', 1)
                        slowprint('After one cut the boss explodes and leaves a black mist behind', 1)
                        slowprint('You see the boss dropped some loot and you go and take a look', 1)
                        slowprint('You see boots that give you super speed when you put them on', 1)
                        slowprint('You also see a pair of gloves', 1)
                        slowprint('There is note that says: \'These gloves give you super strength,', 1)
                        slowprint('but once you put them on you can never take them off', 1)
                        time.sleep(1)
                        
                        print('')
                        slowprint('Press enter to continue', 1)
                        input('')
                        clear()

                        slowprint('You use the super speed to quickly search the castle', 1)
                        slowprint('You find the prisoner and try to break the jailcell by using your super speed', 1)
                        slowprint('Unfortunately that doesn\'t work', 1)
                        slowprint('You doubt for a bit if you should put on the gloves and decide it is the best option', 1)
                        slowprint('You put them on and break the bars of the cell easily', 1)
                        slowprint('You and the prisoner walk out of the castle', 1)
                        won()

                    elif weaponChoise == 'restart':
                        restart()
                    elif weaponChoise == 'quit':
                        quit()
                                    # you let yourself drop
                elif climbDrop == 'drop':
                    slowprint('You break your leg and get eaten by the monster that lives inside the pit', 1)
                    died()
                elif climbDrop == 'restart':
                    restart()
                elif climbDrop == 'quit':
                    quit()
                                        # choosing the ladder
            elif choise2 == 'ladder':
                slowprint('You put the ladder down and start climbing', 1)
                slowprint('Because you want to hurry you fall down and break your leg', 1)
                slowprint('Luckily there is a man who heard you and gives you a potion', 1)
                slowprint('You drink the potion and your leg is healed', 1)
                slowprint('You climb out of the pit, more carefully this time', 1)
                slowprint('You continue to the next room', 1)
                slowprint('When you enter the room you see a strong looking alien', 1)
                slowprint('You stare at each other', 1)
                slowprint('After a few seconds the alien attacks you', 1)
                slowprint('You go unconscious', 1)
                time.sleep(1)
                
                print('')
                slowprint('Press enter to continue', 1)
                input('')
                clear()

                slowprint('When you wake up you\'re in the alien\'s ship', 1)
                slowprint('The alien is taking you to his home planet, Ognuturn', 1)
                slowprint('When you arrive you\'re being searched by his superiors', 1)
                slowprint('They see potential in you and think for some reason you\'re their ruler', 1)
                slowprint('If you stay you\'ll rule over Ognuturn, but you\'ll never be able to go back to earth', 1)
                slowprint('If you leave and go back to earth you can finish your mission', 1)
                
                slowprint('What will you do?', 1)
                worldChoice = input('stay / leave: ')
                clear()

                                        # you stay on Ognuturn
                if worldChoice == 'stay':
                    slowprint('You stay on Ognuturn', 1)
                    slowprint('You become the ruler', 1)
                    slowprint('As ruler you get access to eternal life', 1)
                    slowprint('You get everything you ever wanted and more', 1)
                    slowprint('You forget of you life on earth', 1)
                    slowprint('You continue living, far past the prisoner you were supposed to save', 1)
                    slowprint('Mission failed?', 1)
                    won()

                                        # you go back to earth
                elif worldChoice == 'leave':
                    slowprint('You return to earth', 1)
                    slowprint('You find the prisoner with the help of the aliens', 1)
                    slowprint('You continue living your life on earth', 1)
                    slowprint('Nothing special happens and eventually you die of old age', 1)
                    slowprint('Mission complete', 1)
                    won()

                elif worldChoice == 'restart':
                    restart()
                elif worldChoice == 'quit':
                    quit()

            elif choise2 == 'restart':
                restart()
            elif choise2== 'quit':
                quit()

                                        # entering door 2
        elif enterDoor == 'door 2':
            
            def encounter():

                slowprint('You open door 2', 1)
                slowprint('You walk in and as the door falls shut', 1)
                slowprint('You see two armed guards', 1)
                slowprint('You attack the guards', 1)

                print('')
                slowprint('Press enter to continue', 1)
                input('')
                clear()

                randomEncounter = int(random.randint(1,2))
                print('Encounter: ' + str(randomEncounter))

                print('Do you want to continue this encounter?', 1)
                print('If you don\'t continue, you get a different random encounter', 1)
                continueEncounter = input('yes / no: ')
                clear()

                                            # you continue the encounter
                if continueEncounter == 'yes':

                                            # if you get the first encounter (you win the battle)
                    if randomEncounter == 1:
                        slowprint('You win from the guards and you loot them', 1)
                        slowprint('You find a few different coins and a key', 1)
                        slowprint('When you continue you come across a woman', 1)
                        slowprint('You ask her if she knows where the prisoners are being kept', 1)
                        slowprint('She takes you to the prison, but you got set up and put in jail yourself', 1)
                        slowprint('If you don\'t escape quickly you\'ll die', 1)
                        time.sleep(1)

                        print('')
                        slowprint('Press enter to continue', 1)
                        input('')
                        clear()

                        slowprint('You see a steel pipe and you use it as a lever', 1)
                        slowprint('The door drops out of its socket and you walk out', 1)
                        slowprint('You see two guards running towords you and you have to fight them', 1)
                        slowprint('In a corner you see a few supplies you can use', 1)
                        
                        slowprint('You see a gas grenade filled with poisonous gas and a shotgun', 1)
                        fight = input('grenade / shotgun: ')
                        clear()

                                        # you choose bomb with poisonous gas
                        if fight == 'grenade':
                            slowprint('You take the gas grenade and trow it at the guards', 1)
                            slowprint('The grenade releases the gas and you wait from a distance until it is save', 1)
                            slowprint('What you didn\'t know is that there was a mutation poison mixed within the gas', 1)
                            slowprint('The guards turned into reptiles and charged at you', 1)
                            slowprint('The reptile guards end up killing you', 1)
                            died()

                                        # you choose the shotgun
                        elif fight == 'shotgun':
                            slowprint('You take the shotgun and shoot the guards', 1)
                            slowprint('You take the shotgun with you and keep moving forward', 1)
                            slowprint('You come across a boss and start shooting your shotgun', 1)
                            slowprint('The boss goes down and you walk up to it to see if it dropped any good loot', 1)
                            slowprint('The boss played dead and stabs you really quickly when you are close', 1)
                            slowprint('You jump back and finish him off, but you\'re already stabbed', 1)
                            slowprint('The boss stuck a knife in your chest', 1)
                            slowprint('You can pull the knife out or leave it in', 1)
                            
                            slowprint('Will you leave it in or pull it out?', 1)
                            knife = input('leave it / pull out: ')
                            clear()
                            
                                        # you leave the knife in your chest and continue
                            if knife == 'leave it':
                                slowprint('You leave the knife where it is and continue onto the next room', 1)
                                slowprint('You arrive in the prison and see the prisoner', 1)
                                slowprint('You remind yourself that you had found the key and open the door', 1)
                                slowprint('You take the prisoner with you', 1)
                                time.sleep(1)

                                print('')
                                slowprint('Press enter to continue', 1)
                                input('')
                                clear()

                                slowprint('You notice the pain in your chest getting worse and you look down', 1)
                                slowprint('You see that you lost a lot more blood than you expected', 1)
                                slowprint('You tell the prisoner he has to run and save himself', 1)
                                slowprint('The prisoner panicks and runs away, leaving you to die', 1)
                                slowprint('The prisoner tries to leave the castle, but gets caught', 1)
                                slowprint('He gets the death sentence for trying to escape', 1)
                                died()

                                        # you pull out the knife
                            elif knife == 'pull out':
                                slowprint('You take out the knife and you bleed to death', 1)
                                died()

                            elif knife == 'restart':
                                restart()
                            elif knife == 'quit':
                                quit()
                        
                        elif fight == 'restart':
                            restart()
                        elif fight == 'quit':
                            quit()

                                            # if you get the second encounter (you lose the battle)
                    elif randomEncounter == 2:
                        slowprint('The guards win and you are being tortured', 1)
                        slowprint('They want to know where the army is located', 1)
                        slowprint('You can stay silent or tell them', 1)

                        slowprint('What do you do?', 1)
                        torture = input('talk / keep quiet: ')
                        clear()

                        if torture == 'talk':
                            slowprint('You tell the location of the army and you get locked away', 1)
                            slowprint('They forgot to strip you of your supplies before they locked you away', 1)
                            slowprint('You look around if you can find something in the cell', 1)
                            slowprint('Together with your own supplies you make a bomb of sorts', 1)
                            slowprint('It is not very strong though', 1)
                            slowprint('You place the bomb against the wall and let it blow up', 1)
                            slowprint('You notice, with relieve, that there has been blown a hole in the wall', 1)
                            slowprint('Even if it is just barely', 1)
                            slowprint('You walk through the wall and leave the jailcell', 1)
                            time.sleep(1)

                            print('')
                            slowprint('Press enter to continue', 1)
                            input('')
                            clear()

                            slowprint('You are so happy that you\'re free and don\'t notice the guards surrounding you', 1)
                            slowprint('You panic and get ready for another fight', 1)
                            slowprint('Out of nowhere a ninja appears and takes out most of the guards for you', 1)
                            slowprint('You finish off the rest', 1)
                            slowprint('You approach the ninja and ask what he is doing in the castle', 1)
                            slowprint('He answers: \'That is my business, but if you want I can assist you for a little bit', 1)
                            slowprint('It seems we\'re fighting the same enemy after all\'', 1)
                            slowprint('You team up with the ninja and proceed to search for the prisoner', 1)
                            time.sleep(1)

                            print('')
                            slowprint('Press enter to continue', 1)
                            input('')
                            clear()

                            slowprint('When you enter the next room you two come across an extremely strong boss', 1)
                            slowprint('You fight hard with the ninja, but the ninja gets knocked down', 1)
                            slowprint('Now it is up to you to finish off the boss and save the ninja', 1)
                            slowprint('Because of your passion to save the ninja you awaken a strenth inside of you', 1)
                            slowprint('You have never experienced something like it', 1)
                            slowprint('It turnes out you had super powers dormant inside of you', 1)
                            slowprint('You get super strength and the ability to fly', 1)
                            slowprint('You combine these powers to defeat the boss without being able to get hit', 1)
                            slowprint('Once you take down the boss you hurry over to the ninja', 1)
                            slowprint('Unfortunately the ninja is badly hurt and is about to die', 1)
                            slowprint('The ninja tells you to finish your mission', 1)

                            print('')
                            slowprint('Press enter to continue', 1)
                            input('')
                            clear()

                            slowprint('In honor of his wish you release the prisoner and fly back to the army', 1)
                            slowprint('You tell the commander that a legion from the castle is comming to their base', 1)
                            slowprint('Thanks to that the army places an ambush and they take out the guards easily', 1)
                            slowprint('You get released and are now a free man, you continue living with the super powers', 1)
                            won()

                        elif torture == 'keep quiet':
                            slowprint('You keep quiet and they keep torturing you', 1)
                            slowprint('Until, out of nowhere a ninja shows', 1)
                            slowprint('The ninja rescues you and you walk out of the room', 1)
                            time.sleep(1)
                            clear()

                            slowprint('You and the ninja come across a boss', 1)
                            slowprint('Together you go and fight the boss, but he is really strong', 1)
                            slowprint('You notice you don\'t have the strength to fight because of the torture', 1)
                            slowprint('The ninja has no choice but to fight alone and loses', 1)
                            slowprint('The boss defeats you both', 1)
                            died()

                        elif torture == 'restart':
                            restart()
                        elif torture == 'quit':
                            quit()

                                            # you restart the game for a different encounter
                elif continueEncounter == 'no':
                    encounter()
                elif continueEncounter == 'restart':
                    restart()
                elif continueEncounter == 'quit':
                    quit()
            
            encounter()

        elif enterDoor == 'restart':
            restart()
        elif enterDoor == 'quit':
            quit()

                                        # not entering the castle
    elif enterCastle == 'no':
        slowprint('The Guards have shot you.', 1)
        died()
    elif enterCastle == 'restart':
        restart()
    elif enterCastle == 'quit':
        quit()

main()