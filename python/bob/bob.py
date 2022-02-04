def response(hey_bob):

    hey_bob = str(hey_bob).strip()

    if hey_bob.isupper() and hey_bob.endswith('?'):
        return 'Calm down, I know what I\'m doing!'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.endswith('?'):
        return 'Sure.'
    elif hey_bob == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
