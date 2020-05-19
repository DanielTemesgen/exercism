def convert(number):
    raindrops={
        3:'Pling',
        5:'Plang',
        7:'Plong'
    }
    list_of_sounds = [v if number % k == 0 else '' for k, v in raindrops.items()]
    sound = ''.join(list_of_sounds)
    if not sound:
        return str(number)

    return sound
