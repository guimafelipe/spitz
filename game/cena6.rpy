define ovum = Character("Ovum")
define msegg = Character("Ms. Egg")

init:
    transform flip:
        xzoom -1.0

label cena6:
    scene bg ovarium empty
    with fade

    "In my short hours as a sperm cell I never thought"

    " that I was going to be chased down through traffic by an old lady."

    "But boy, was I wrong."

    "Drivers honk angrily at us."

    play sound "audio/buzina 1.ogg" volume 0.4

    "Some pull over. Afraid of the grandma, perharps?"

    "I realize I still got the iron bar. I hold on it for my dear life."

    "Should I use it against the old lady?"

    "I look back."

    show halfblack
    show spitz at right:
        xzoom -1.0
    show old serious at left:
        xzoom -1.0
    with dissolve

    grandma "Come back here you little mother floating piece of s-! {p=3}{nw} "

    hide halfblack
    hide spitz
    hide old
    with dissolve

    "I'm too scared to face her anger. Or her cane."

    "I keep running."

    "We go down one of the ovarian tubes. I have no idea if it's the right one."

    "At this point, I just want to survive."

    #scene bg ovarium empty
    #with fade

    "The ovarian tube is a much better running track."

    "It's soon too narrow for the cars and the few sperm people scramble to the sides when they see our approach."

    "It would be so easy to keep going, but I start to feel my tail faltering."

    "Am I going out of energy?"

    show halfblack
    show spitz at right:
        xzoom -1.0
    show old serious at left:
        xzoom -1.0
    with dissolve

    spitz "How are you alive for 10 days straight, you horrid woman?"

    grandma "I ATE MY GRANDSON'S MITHOCHONDRIA. AND MY CHILDREN'S BEFORE."

    hide halfblack
    hide spitz
    hide old
    with dissolve

    "I find it in me to keep running out of sheer horror."

    "Then I see her, plump and rich."

    scene bg ovarium
    with dissolve

    "I come to a halt, just as the old woman behind me."

    "I can't help but to blurt out aloud:"

    show halfblack
    show spitz at left:
        xalign 0.25
    show old contempt at left
    show ovulo at right:
        zoom 0.7
    with dissolve

    spitz "Could that be the OVUM!?"

    ovum "It's actualy secondary oocyte."

    ovum "That's a common mistake."

    msegg "But you may call me Ms. Egg."

    grandma "My dream"

    grandma "My dream has finally come true."

    grandma "It's an honour, Ms. Egg."

    msegg "You're not the first to come to me. But are you worthy of my rich cytoplasm?"

    spitz "What is it all about anyway?"

    grandma "..."

    msegg "..."

    spitz "Alright, alright. I don't know what it is, but I'm still in."

    msegg "What shall you offer me, then?"

    spitz "Well, I crashed into this fleshy hellhole barehanded."

    spitz "And I kinda killed this one guy..."

    grandma "KINDA?!"

    msegg "Hmm... I do like the violent ones."

    "Let's she think it was on purpose, then."

    "I realize I've dropped the iron bar somewhere along the way."

    "But my face is still covered in another's sperm cytoplasm."

    spitz "And I ran all the way here from the uterus with this psychotic old lady after me."

    grandma "PSYCHOTIC YOUR A- {p=1.5}{nw}"

    spitz "Argh!"

    "I feel an intense pain at the base of my tail."

    "Could it be my mithochondria failing?"

    show spitz at left:
        xalign 0.25
        yalign 1.15
    with move

    "I fall on my knees."

    grandma "Well, the little guy doesn't seem to have much time left."

    grandma "But I'm alright to continue this conversation."

    grandma "I've just run the same distance, you know."

    grandma "After this little punk brutally killed my grandson."

    msegg "It's not like I condemn kill- {p=1.5}{nw}"

    grandma "But I carried on."

    grandma "I consumed my grandson's mithochondria."

    grandma "Just as I did with my children before him."

    grandma "All who died on my arms after days of fighting for the honor of meeting you, my lady."

    spitz "Argh"

    "My vision starts to blur. I'd be short-breathed if I had lungs."

    "But I just feel my tail stoping to move and the burning pain at its base."

    grandma "I've been alive for 10 days!"

    msegg "It's not unheard of..."

    msegg "Although I reckon it might do."

    show spitz at left:
        yalign 1.1
    show old contempt at left:
        xalign 0.4
    with move

    "Ms. Egg beckoned that abhorrent woman forward and embraced her."

    "I felt a pang of an unknown sentiment within my trembling body."


    # "Then I saw the most horrific"

    "Then I saw the most horrific {p}and at the same time the most beautiful thing."
     
    show ovulo big mouth at right:
        zoom 0.7

    "Ms. Egg ripped the old woman's head off."

    "And ate it whole."

    hide old
    with dissolve

    msegg "NOM NOM NOM NOM NOM"

    spitz "!"

    show ovulo at right:
        zoom 0.7
    with dissolve

    msegg "Oh gosh, I was forgetting about the implantation at the uterus."

    msegg "I'm going to have to call a cab."
    
    show ovulo at offscreenright:
        zoom 0.7
    with move

    "I guess she's going to get caught in that ridiculous traffic jam."

    "It was my last thought before everything went blank."

    scene bg darkness
    with dissolve

    spitz "..."

    return
