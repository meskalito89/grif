from typing import Literal
from colorama import Fore

note_sequence = Literal['c', 'c#', 'd', 'd#', 'e', 'f', 'f#',
                        'g', 'g#', 'a', 'a#', 'b']



def colorize_note(char, color=Fore.WHITE):
    """this function get_schar and wrap it in Fore.color"""
    return Fore.__dict__[color.upper()] + char + Fore.WHITE


class Grif:

    """This is class that show notes on griff of the guitar"""
    def __init__(self,
                 tune=('e',  'b', 'g', 'd', 'a', 'e'),
                 lad_width=3,
                 n_of_lads=15
                 ) -> None:
        self.lad_width = lad_width
        self.n_of_lads = n_of_lads
        self.tune = tune
        self._colors: dict[str, str] = {}
        self._text = ''


    def get_strings(self):
        strings = []
        for open_string_note in self.tune:
            string = []
            index = note_sequence.index(open_string_note)
            for i in range(1, self.n_of_lads + 1):
                note = note_sequence[(index + i) % len(note_sequence)]
                string.append(note)
            strings.append(string)
        return strings

    def update_text(self):
        self._text = ''
        strings = self.get_strings()
        lad_width_extension_for_color = 10
        for string in strings:
            for note in string:
                if note in self._colors:
                    color = self._colors.get(note, 'WHITE')
                    note = colorize_note(note, color)
                else:
                    note = colorize_note('-', "white")
                self._text += note.center(
                    self.lad_width +
                    lad_width_extension_for_color, '-') + '|'
            self._text += '\n'
        self.add_lad_numbers()

    def add_lad_numbers(self):
        lad_numbers = ('', '', 'III', '', 'V', '', 'VII', '',
                       'IX', '', '', 'XII', '', '', 'XV')
        lad_numbers_string = ''
        for lad_number in lad_numbers:
            lad_numbers_string += lad_number.center(self.lad_width + 1, ' ')
        self._text += lad_numbers_string

    def add_chord(self, chord: tuple, color: str):
        for note in chord:
            self._colors[note] = color
        self.update_text()

    def __str__(self) -> str:
        return '\n' + self._text + '\n'


if __name__ == "__main__":
    grif = Grif(tune=('g', 'd', 'a', 'e'))
    grif.add_chord(('c', 'e', 'g', 'a#'), 'green')
    grif.add_chord(('g', 'b', 'd', 'f'), 'yellow')
    print(grif)

