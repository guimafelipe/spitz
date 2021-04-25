define bully = Character('Bully', color="#eb343a")

label cena4:
    scene bg engarrafamento
    with fade

    
    # "\"Honk hooonk\" \n\"Beep beeeeeep\""
    
    

    "Barely a few minutes on the road and the sound of car horns are making me crazy."
    
    window hide

    play sound "audio/buzina 2.ogg"

    pause

    window show

    "I discovered I can actually drive, by the way."

    "I don't know what I expected from the uterus, but it certainly wasn't this f-ing traffic jam."

    "The tension is palpable in the air."

    "\"Get outta my way! \""

    " \"You inseminating mother floater! \""

    "I try to keep calm, maybe remember some peaceful moment from my childhood."

    "Nothing comes to mind."

    "What was I doing last week?"

    "Nothing at all that I can remember."

    "I focus on my objective."

    "The sole reason I came here in the first place."

    "To find the OVULUM."

    "Whatever an ovulum is."

    "The traffic calms down a little around me. It starts to flow again."

    "Until a m-floater cuts me off."

    "I honk my horn."


    play sound "audio/buzina 3.ogg"
    "BEEEEEEEEEEEEEEEEEEEEEEEP"

    "I'm still pressing the horn when the car in front of mine suddenly brakes."

    "{i}Screeeeeeeeeeeeeeeech{/i}"

    "I desperately reach for the brake with my tail."

    "{i}Screeeeeeeeeeeeeeeech{/i}"

    #show bg traffic jam with vpunch
    with vpunch

    "{b}BAM!{/b}"
    with vpunch

    #show bg traffic jam with vpunch

    "{b}CRASH!{/b}"
    

    "Oh gosh, we crashed."

    "The driver comes out of the car. He's marching angrily towards me."

    play music "audio/musica da luta.ogg"

    show bully on the right

    "Shakily, I manage to get out of my car and face him."

menu:

    "Apologize":
        jump apologize

    "Yell at him":
        jump yell

label apologize:

    spitz "I’m so sorry, man. I didn’t mean to-"
    bully "YOU DIDN’T MEAN TO F-ING CRASH INTO MY CAR?"

    jump aposmenu

label yell:

    spitz "GO CUT OFF YOUR GRANDMA, YOU MOTHER FLOATING SON OF A -"

    jump aposmenu

label aposmenu:

    bully "MY GRANDMA IS IN THE BACKSEAT, YOU MONSTER!"
    bully "YOU ALMOST KILLED HER."

    spitz "But… but… why did you cut me off with your grandma in the backseat?"

    spitz "It’s dangerous, you know."
    return
