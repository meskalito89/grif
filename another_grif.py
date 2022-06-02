'''what is module docstring?'''
from typing import Literal
from typing import Tuple, List, TypeVar, Generic
from colorama import Fore
from enum import Enum

Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
NOTE_SEQUENCE: Tuple[Note, ...] = ('a', 'a#', 'b', 'c', 'c#', 'd',
                                   'd#', 'e', 'f', 'f#', 'g', 'g#')

Tune = Tuple[Note, ...]
STANDARD_TUNE: Tune = ('e', 'b', 'g', 'd', 'a', 'e')


def _generate_sequence_of_notes_len_n(note: Note,
                                      length: int) -> List[Note]:
    '''generate sequence of notes of len (n)'''
    index_of_note = NOTE_SEQUENCE.index(note)
    string = []
    for i in range(length):
        string.append(
            NOTE_SEQUENCE[(i + index_of_note + 1) % len(NOTE_SEQUENCE)]
        )
    return string


def _colorize_note(note: Note, color: str = Fore.WHITE):
    return Fore.__dict__[color] + note + Fore.WHITE


class Grif:
    'this class represents grif of guitar and print notes on it'
    def __init__(self, tune: Tune = STANDARD_TUNE,
                 n_of_lads: int = 15) -> None:
        self.tune = tune
        self.chord: dict[Note, str] = {}
        self.n_of_lads = n_of_lads
        self._notes = self._generate_all_notes(tune)
        self._text_view = ''
        self.printed_notes: list[list[Note]]

    def _generate_all_notes(self, tune: Tune) -> List[List[Note]]:
        """generates array with shape(len(tune), n_of_lads)"""
        strings = []
        for note in tune:
            strings.append(
                _generate_sequence_of_notes_len_n(note, self.n_of_lads))
        return strings

    def _colorize_all_notes(self):
        color_strings = []
        for string in self._notes:
            color_notes = []
            for note in string:
                if note in self.chord:
                    color = self.chord[note]
                    color_note = _colorize_note(note, color)
                    color_notes.append(color_note)
            color_strings.append(color_notes)
        return color_strings

    def add_note(self, note: Note, color: str):
        'add note: color to self.chord dictionary'
        self.chord[note] = color
        self._notes = self._generate_all_notes(self.tune)
        self._notes = self.

    def _filtered_string(self, string: list[Note]) -> list[Note]:
        def filter_func(note):
            return note if note in self.chord.keys() else ''
        return list(map(filter_func, string))

    def _filter_notes(self) -> None:
        new_strings = []
        for string in self._notes:
            filtered_string = self._filtered_string(string)
            new_strings.append(filtered_string)
        self.printed_notes = new_strings

    def _convert_to_string(self):
        for string in self._notes:
            for note in string:
                print(note)

    def __str__(self) -> str:
        return self._text_view


if __name__ == '__main__':
    grif = Grif(n_of_lads=24)
    grif.add_note('e', 'RED')
    grif._filter_notes()
    grif._convert_to_string()
