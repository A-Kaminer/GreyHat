print('welcome to the super secure flag checker!')
print('give me a flag, and I will say if it is correct.')

flag = input('flag: ')

print('correct!' if len(flag) == 3 << 3 and all(s[::-1] in flag for s in [
    'alf',
    'hcu',
    'um_',
    '{ga',
    'wow',
    'rev',
    'r_h',
    'cum',
    '_hc',
    '_wo',
    'gni',
    'gal',
    'w{g',
    '}gn',
    'isr',
    'ow{',
    'nis',
    'm_w',
    'er_',
    'eve',
    'sre',
    'ver',
]) else 'incorrect.')
