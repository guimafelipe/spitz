label cena5b:
    "I’d better run."

    "Violence isn’t worthy it."

    "Or at least I don’t think I stand a chance against this guy."

    "I break into a run."

    "My tail flaps rapidly on the roadside as I put distance between us."

    "For several seconds, I don't know if he's going to follow."

    "I hear steps behind me and look back."

    # MOSTRAR BULLY COM A BARRA DE FERRO

    show ironbar at right:
        xzoom -1.0

    spitz "Oh no!"

    "That was an understatement."

    bully "YOU'RE GONNA PAY FOR STARTLING MY POOR GRANDMA!"

    "He lunged at me with the iron bar."

    show ironbar at left:
        xzoom -1.0
    show punk at left
    with move
    show ironbar at right:
        xzoom -1.0
    show punk at right

    "It connected with my head."

    show spitz pain at left

    play sound "audio/thud.ogg" volume 0.4

    "He did it again."

    show ironbar at left:
        xzoom -1.0
    show punk at left
    with move
    show ironbar at right:
        xzoom -1.0
    show punk at right

    with hpunch

    play sound "audio/thud.ogg" volume 0.4

    play sound "audio/splash.ogg" volume 0.4

    "I heard my celular membrane tearing and felt"

    "my cytoplasm... oozing... out..."

    spitz "..."

    show spitz dead

    return
