define grandma = Character("Grandma")

label cena5a:

    "I think I saw an iron bar lying around by the roadside."

    "I make a run for it."

    bully "What are you doing?!"

    "It seems he hasn’t seen it yet."

    show ironbar at left

    "He tries to grab at me."

    show spitz angry at right
    show ironbar at right
    with move

    show spitz angry at left
    show ironbar at left

    "I swing the iron bar."

    with hpunch

    "The piece of metal connects with his head."

    play sound "audio/thud.ogg" volume 0.6

    "It makes an awful sound for what was suposed to be a celular membrane."

    show spitz angry at right
    show ironbar at right
    with move

    show spitz angry at left
    show ironbar at left

    "I swing the metal bar again."

    with hpunch

    play sound "audio/thud.ogg" volume 0.6

    "{b}SPLASH{/b}"

    play sound "audio/splash.ogg" volume 0.7

    "The man before me slumps to the ground."

    # rotate punk sprite

    # hide punk
    show punk:

        easeout 1.0 rotate(90) yalign 2.0

    bully "..."

    show spitz pain

    spitz "WHAT HAVE I DONE?!"

    show spitz

    "My face is covered in blood."

    "Cytoplasm, actually."

    "I face the dead cell at my feet and try to remember the rules."

    "There are probably rules, right?"

    "Have I broken any law?"

    "I hear someone approaching and look up"

    show spitz at left

    "in time to see the murderous look this old woman is giving me, mere micrometers away."

    "She snarls when we make eye contact."

    hide punk
    with dissolve

    show old snarl at right
    with dissolve

    play music "audio/musica da luta.ogg"

    grandma "WHAT HAVE YOU DONE YOU LITTLE PUNK!?"

    show cane at right:
        zoom 0.5
    with dissolve

    "Is it a cane she’s swinging at me?"

    grandma "My grandson was a very good boy."

    grandma "He always wrote on Christmas."

    "What the float is even Christmas?"

    grandma "Of course it was only once, I’ve been here for 10 days."

    grandma "And more important:"

    grandma "HE WAS MY LAST CHANCE OF MEETING THE OVUM."

    grandma "I chose the wrong uterine tube when I was younger."

    grandma "I got married, had kids. Then my kids had kids."

    spitz "Is it even possible?"

    grandma "Shut up!"

    grandma "You killed my grandson."

    grandma "PREPARE TO DIE!"

    with hpunch

    with vpunch

    "The old woman brandishes her cane at me one more time."

    "And starts limping in my direction."

    "I run."

    show old snarl at left
    show cane at left
    show spitz at offscreenleft
    show ironbar at offscreenleft
    with move


    jump cena6
