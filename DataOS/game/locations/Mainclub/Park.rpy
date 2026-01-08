label opening_park:
    stop music
    scene park_morning_evening with dissolve  
    ""
    play music park loop  
    "so this is gonna where i choose my OS"
    "i've been meaning to to find one for so long"
    "but ugh touching grass"
    "i feel nervious for some reason"
    w " haii" with dissolve
    w "You're that new guy!"
    w "im Windows"
    w "who are you?"
    mc "um Hello"
    mc "I'm Avery"
    w "oooo hai Avery"
    w "im windows"
    mc "you've said..."
    w "i did?"
    w "sorry my memory isnt great"
    mc "its fine"
    w "so are you new here?"
    mc "yeah. i've been meaning to see the plave before school begins"
    w "!"
    
    menu windows_letsgo: 
        w "i gotta tour you the place!" 
        "hell yeah!":
            w "LETS GOOO"
            $ affection += 1
        "okay":
            w "a little cold..."
            w "but ill show you"

    
    w "wow"
    jump tour
    
    label late_evening1: