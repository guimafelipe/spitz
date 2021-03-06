define vendor = Character("Salesman", color = "#444444")

label cena3:
    scene bg rent a car 1
    with fade

    "I follow the voice and start walking deeper into the tunnel."

    "There’s a building near the end. Before it, a line of waiting sperm people."

    "I take my place at the end of the line."

    "How am I supposed to pay for car rental?"

    "Do I need a credit card?"

    "Do I even have a license?"

    scene bg rent a car 2
    with squares

    "…"

    "It’s finally my turn. Someone stares up at me from a little cabin."

    show halfblack
    show spitz at left
    show salesperson at right
    with dissolve

    vendor "\"Hey, buddy. Can you drive?\""

    menu:

        "Sure.":
            jump candrive

        "I don't think so.":
            jump cantdrive


label candrive:
    spitz "Sure."

    vendor "You're a lucky one. Most of these folks don't."

    jump apospergunta

label cantdrive:
    spitz "Er... I don't think so."

    vendor "I'm sure you'll get the hang of it."
    jump apospergunta

label apospergunta:

    vendor "Here are your keys. Don’t worry, the OVUM is paying for everything."

    vendor "You know she makes pretty much all of the investment here."

    spitz "\"The ov-\"{p=0.7}{nw} "

    vendor "\"Neeeeeext!\""

    hide spitz
    hide salesperson
    hide halfblack
    with dissolve

    "The man seems busy. I’d better get going."

    jump cena4
