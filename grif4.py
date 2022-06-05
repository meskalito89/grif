from typing import Literal, Tuple, Dict


Note = str

class Grif:
    def __init__(self, tune=('e', 'b', 'g', 'd', 'a', 'e')):
        self.tune = tune
        self.chord_color: Dict[Note, str] = {}

    def add_chord(self, chord: Tuple[Note, ...], color: str):
        'added chord and color into object chord_color field'
        for note in chord:
            self.chord_color[note] = color


if __name__ == '__main__':
    grif = Grif()
    grif.add_chord(('c'), 'RED')
    print(grif.chord_color)

