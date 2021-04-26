define bully = Character('Angry Guy', color="#eb343a")

label cena4:
    scene bg engarrafamento
    with fade


    # "\"Honk hooonk\" \n\"Beep beeeeeep\""



    "Barely a few minutes on the road and the sound of car horns are making me crazy."

    window hide

    play sound "audio/buzina 2.ogg" volume 0.4

    pause

    window show

    "I discovered I can actually drive, by the way."

    "I don't know what I expected from the uterus"

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

    "To find the OVUM."

    "Whatever an ovum is."

    "The traffic calms down a little around me. It starts to flow again."

    #---- START OF TRAFFIC INCIDENT

    stop music fadeout 1.0

    "Until a m-floater cuts me off."

    "I honk my horn."


    play sound "audio/buzina 3.ogg" volume 0.4

    pause

    # "BEEEEEEEEEEEEEEEEEEEEEEEP"

    "I'm still pressing the horn when the car in front of mine suddenly brakes."

    play sound "audio/tires.ogg" volume 0.4

    "{i}Screeeeeeeeeeeeeeeech{/i}"

    "I desperately reach for the brake with my tail."

    play sound "audio/tires.ogg" volume 0.4

    "{i}Screeeeeeeeeeeeeeeech{/i}"

    stop music fadeout 1.0

    #show bg traffic jam with vpunch
    with vpunch

    #show bg traffic jam with vpunch

    play sound "audio/batida do carro.ogg" volume 0.4

    "{b}CRASH!{/b}"


    "Oh gosh, we crashed."

    "The driver comes out of the car. He's marching angrily towards me."

    play music "audio/musica da luta.ogg" fadein 1.0

    show halfblack
    show punk
    with dissolve

    "Shakily, I manage to get out of my car and face him."

menu:

    "Apologize":
        jump apologize

    "Yell at him":
        jump yell

label apologize:

    show punk at right with move
    show spitz at left
    with dissolve

    spitz "I’m so sorry, man. I didn’t mean to- {p=2}{nw} "

    bully "YOU DIDN’T MEAN TO F-ING CRASH INTO MY CAR?"

    jump aposmenu

label yell:

    show punk at right with move
    show spitz at left

    spitz "GO CUT OFF YOUR GRANDMA, YOU MOTHER FLOATING SON OF A - {p=2.5}{nw} "

    # show punk at right

    jump aposmenu

label aposmenu:

    bully "MY GRANDMA IS IN THE BACKSEAT, YOU MONSTER!"
    bully "YOU ALMOST KILLED HER."

    spitz "But… but… why did you cut me off with your grandma in the backseat?"

    spitz "It’s dangerous, you know."

    #stop music

    $ renpy.music.set_pause(True)

    bully "My grandma has but a few minutes to live."

    bully "Her dying wish is for me to achieve what she never could."

    bully "For me to reach the OVUM."

    bully "AND I’M NOT LETTING A MOTHERFLOATING WIMP GET IN MY WAY."

    $ renpy.music.set_pause(False)

    "He seems about to jump at me."

menu:
    "I think I saw an iron bar lying around by the roadside.":
         jump cena5a

    "I’d better run.":
         jump cena5b
