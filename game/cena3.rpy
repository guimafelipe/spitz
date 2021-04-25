define vendor = Character("Salesman", color = "#000000")

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
    with dissolve

    "…"

    "It’s finally my turn. Someone stares up at me from a little cabin."

    vendor "“Hey, buddy. Can you drive?”"

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

    vendor "You'll get the hang of it."
    jump apospergunta

    label apospergunta:

    vendor "“Here are your keys. Don’t worry, the ovulum is making all the investment.”"

    spitz "“The ovol-”"

    vendor "“Neeeeeext!”"

    "The person seems busy. I’d better get going."

    jump cena4
