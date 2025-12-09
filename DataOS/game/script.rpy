# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# these are the charecters speaking. the first letter of their name will be used to indicate the charecter. 
# and the gender will be shown by the first letter. so say male Windows would be: wb.
# if a names begining letter overlaps with an existing name. than add the letter next to it.

# males:
define wb = Character("Windows")
define lb = Character("Linux")
define mb = Character("Mac")
define rb = Character("Redstar")
define ab = Character("Android") 
define Amb = Character("Amiga") 
define ub = Character("Unix")

# females:
define wg = Character("Windows")
define lg = Character("Linux")
define mg = Character("Mac")
define rg = Character("Redstar")
define ag = Character("Android") 
define Amg = Character("Amiga") 
define ug = Character("Unix")

#NDC aka none dateable charecters
define data = Character("DataOS")





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    stop music 

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

  

    # These display lines of dialogue.

 
    play sound openos
    data "welcome to DataOS."
    play music maintheme2 loop
    data "the biggest collection of dateable OS'es."
    data "before we begin"
    data "you must configure what you want your OS'es dateables to look like"
    # This ends the game.

    return
