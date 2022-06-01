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


class Grif:
    'this class represents grif of guitar and print notes on it'
    def __init__(self, tune: Tune = STANDARD_TUNE,
                 n_of_lads: int = 15) -> None:
        self.tune = tune
        self.n_of_lads = n_of_lads
        self._notes = self._generate_all_notes(tune)
        self._text_view = ''
        self._chord = dict[Note, Fore]

    def _generate_all_notes(self, tune: Tune) -> List[List[Note]]:
        """generates array with shape(len(tune), n_of_lads)"""
        strings = []
        for note in tune:
            strings.append(
                _generate_sequence_of_notes_len_n(note, self.n_of_lads))
        return strings

    def __str__(self) -> str:
        return self._text_view


if __name__ == '__main__':
    pass


