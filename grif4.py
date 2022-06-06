from typing import Literal, Tuple, Dict, List, Callable
from colorama import Fore


Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e',
               'f', 'f#', 'g', 'g#', '-']
NOTE_SEQUENCE: Tuple[Note] = ('a', 'a#', 'b', 'c', 'c#', 'd',
                                   'd#', 'e', 'f', 'f#', 'g', 'g#')


def generate_string_array(note1: Note, n_of_lads: int) -> List[Note]:
    'generate only 1 string [note1, note2, note3 ... note(n_of_lads)]'
    index_of_note1 = NOTE_SEQUENCE.index(note1)
    string = []
    for i in range(n_of_lads):
        index_of_next_note = i + index_of_note1 + 1
        string.append(NOTE_SEQUENCE[index_of_next_note % len(NOTE_SEQUENCE)])
    return string


def generate_all_strings(tune: Tuple[Note],  n_of_lads: int) -> List[List[Note]]:
    """Return list of lists with notes
    tune is tuple of notes"""
    grid_of_notes = []
    for note1 in tune:
        string = generate_string_array(note1, n_of_lads)
        grid_of_notes.append(string)
    return grid_of_notes





class Grif:
    def __init__(self, tune=('e', 'b', 'g', 'd', 'a', 'e'), n_of_lads=15):
        self.tune = tune
        self.chord_color: Dict[Note, str] = {}
        self.grid = generate_all_strings(tune, n_of_lads)
        self.grid_for_printer = []

    def add_chord(self, chord: Tuple[Note, ...], color: str = Fore.WHITE) -> None:
        'added chord and color into object chord_color field'
        for note in chord:
            self.chord_color[note] = color

    def colorize_note(self):

        def paint(note, color):
            if note in self.chord_color:
                return Fore.__dict__[color] + note + Fore.WHITE
            return Fore.WHITE + note + Fore.WHITE

        for note, color in self.chord_color.items():
            self.for_each(self.grid, paint)

            
            
    def for_each(self, array: List[List[Note]], func: Callable) -> List[List[Note]]:
        new_array = []
        for string in array:
            new_string = []
            for note in string:
                new_string.append(func(note))
            new_array.append(new_string)
        return new_array
            



if __name__ == '__main__':
    grif = Grif()
    grif.add_chord(('c'), 'RED')
    print(generate_all_strings(grif.tune, 15))

