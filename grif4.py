import argparse
from typing import Literal, Tuple, Dict, List, Callable, Any


Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e',
               'f', 'f#', 'g', 'g#', '-']
NOTE_SEQUENCE: List[Note] = ['a', 'a#', 'b', 'c', 'c#', 'd',
                             'd#', 'e', 'f', 'f#', 'g', 'g#']


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
    def __init__(self,
                 tune=('e', 'b', 'g', 'd', 'a', 'e'),
                 n_of_lads: int = 15,
                 lad_width: int = 5):
        self.tune = tune
        self.lad_width = lad_width
        self.chord: List[Note] = []
        self.grid = generate_all_strings(tune, n_of_lads)
        self.grid_for_printer: List = []
        self.str: str = ''
        self.n_of_lads = n_of_lads
        
    def add_chord(self, chord) -> None:
        'added chord into object chord field'
        if isinstance(chord, list):
            self.chord += chord
        else:
            self.chord.append(chord)


    def for_each(self, array: List[List[Note]], func: Callable) -> List[List[Note]]:
        new_array = []
        for string in array:
            new_string = []
            for note in string:
                new_string.append(func(note))
            new_array.append(new_string)
        return new_array

    def get_grif_of_oly_chords_note(self):
        copy_grid = []
        for string in self.grid:
            new_string = []
            for note in string:
                if note not in self.chord:
                    note = '-'
                new_string.append(note)
            copy_grid.append(new_string)
        return copy_grid

    def get_lad_numbers_string(self):
        lad_string = ''
        for lad_number in ('', '', 'III', '', 'V', '', 'VII', '', 'IX', '', '', 'XII'):
            lad_string += lad_number.center(self.lad_width + 1, ' ')
        return lad_string

    def __str__(self):
        for string in self.get_grif_of_oly_chords_note():
            for note in string:
                self.str += note.center(self.lad_width, '-') + '|'
            self.str += '\n'
        self.str += self.get_lad_numbers_string()
        return self.str


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-c', '--chord', help='notes of chord separate by space')
    argparser.add_argument('-t', '--tune', help='tune of guitar separate by space')
    args = argparser.parse_args()

    tune = args.tune.split()
    chord = args.chord.split()
    
    grif = Grif()
    if tune:
        grif = Grif(tune=tune)
    grif.add_chord(chord)
    print(grif)

