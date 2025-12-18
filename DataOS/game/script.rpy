
# Declare characters used by this game. The color argument colorizes the
# name of the character.
init -100:
    default gender = None
    $ import random

# these are the charecters speaking. the first letter of their name will be used to indicate the charecter. 
# and the gender will be shown by the first letter. so say male Windows would be: wb.
# if a names begining letter overlaps with an existing name. than add the letter next to it. 
# males:


#NDC aka none dateable charecters
define data = Character("DataOS")

# charecter gender by players choice 1 = female whilest 0 equals male while 2 = mix


# affection defualts
default love = 0
default friendship = 0
default respect = 0
default affection = 0
default trust = 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    stop music 

    scene ice

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

  

    # These display lines of dialogue.

    play sound openos
    data "welcome to DataOS" with dissolve 
    play music maintheme2 loop
    data "the biggest collection of dateable OS'es."
    data "before we begin"
    data "you must configure what you want your OS'es dateables to look like"
   
    menu pick_gender:
        data "male or female or mixed?" with dissolve

        "all female":
            data "good choice"
            $ gender = 1
            $ win_gen = 1
            $ lin_gen = 1
            $ gcolor = "#e2a8ff"
        "all male":
            data "great choice"
            $ gender = 0
            $ win_gen = 0
            $ lin_gen = 0
            $ gcolor = "#57bcff"
        "mix":
            data "nice choice"
            $ from a import reset
            $ reset()
            $ win_gen = random.randint(0,1)
            $ lin_gen = random.randint(0,1)

    data "gender is [gender]"
    
    
        

    # show windowsi at truecenter
    # if win_gen:
    #     w "wow i look pretty"
    # else:
    #     w "wow Handsome"
     
    # show linuxi at truecenter
    # if lin_gen:
    #     l "girl"
    # else:
    #     l "boy"

    data "if this is your first time playing"
    data "than here is some simple questions, you'll get answers to"

    menu ask_question:
        data "Any questions before we begin?" with dissolve

        "game mechanics?":
            data "you can find out by going to the 'instrcutions' menu" with dissolve 
            jump ask_question    
        "charecters":
            data "the list pf datable OS'es include:"
            data "Windows" with dissolve 
            data "Linux" with dissolve 
            data "MacOS" with dissolve 
            data "Android" with dissolve 
            data "Amiga" with dissolve 
            data "Unix" with dissolve 
            data "Redstar" with dissolve 
            data "TempleOS" with dissolve 
            data "DOS" with dissolve 
            data "BSD" with dissolve 
            data "BEOS" with dissolve 
            data "Haiku" with dissolve 
            jump ask_question 
        "Begin game": 
            play audio startgame
            jump opening_park
    


    
    