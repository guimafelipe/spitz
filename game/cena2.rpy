define tc = Character("Sperm 1")
define th = Character("Sperm 2")

label cena2:
    show bg scattered sperm
    with fade

    play music "audio/musica neutra.ogg"

    "\"Ouch!\""

    "\"Get out of my tail!\""

    show halfblack
    show 2caudas at truecenter
    with dissolve

    tc "\"Look, I’ve got two tails!\""

    hide halfblack
    hide 2caudas
    with dissolve

    "All around, sperm cells fall scattered on the ground."

    "We’re on some kind of tunnel. Everything is pinkish in color."

    show halfblack
    show 2head at truecenter
    with dissolve

    th "\"I’ve got two heads!\" \"No, I have two heads!\""

    hide halfblack
    hide 2head
    with dissolve

    "\"Get up or you’re gonna be left behind, you morons.\" Someone yells."

    "The floor is squishy when I manage to get up on my tail."

    scene bg scattered pe
    with dissolve

    "\"Com'on!\""

    jump cena3
