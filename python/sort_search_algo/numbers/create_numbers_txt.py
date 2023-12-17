from random import randint

def create_n(lines):
    for _ in range(lines):
        with open(f'{lines}.txt', 'a') as file_:
            file_.write(f'{randint(1, lines)}\n')

create_n(1000000)
