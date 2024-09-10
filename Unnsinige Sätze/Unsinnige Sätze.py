from random import randint

name = ['Otto', 'Andras', 'Lea', 'Nico', 'Manu', 'Tina']
verb = ['kocht', 'reitet', 'fickt', 'staunt', 'fällt']
ende = ['der Kirche', 'dem Meer', 'Berlin']


def pickV1(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked


print(pickV1(name), pickV1(verb), 'in', pickV1(ende), end='.\n')

# Endloser Unsinn!
name = ['Otto', 'Andras', 'Lea', 'Nico', 'Manu', 'Tina']
verb = ['kocht', 'reitet', 'fickt', 'staunt', 'fällt']
ende = ['der Kirche', 'dem Meer', 'Berlin']


def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked


while True:
    print(pick(name), pick(verb), 'in', pick(ende), end='.\n')
    input()
