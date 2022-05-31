'''what is module docstring?'''
from typing import Literal
from typing import Tuple, List

Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
NOTE_SEQUENCE: Tuple[Note, ...] = ('a', 'a#', 'b', 'c', 'c#', 'd',
                                   'd#', 'e', 'f', 'f#', 'g', 'g#')

Tune = Tuple[Note, ...]
STANDART_TUNE: Tune = ('e', 'b', 'g', 'd', 'a', 'e')


def _generate_sequence_of_notes_len_n(sequence: Tuple[Note, ...],
                                     length: int) -> List[Note]:
    '''generate sequence of notes of len (n)'''
    pass



class Grif:
    'this class represents grif of guitar and print notes on it'
    def __init__(self, tune: Tune = STANDART_TUNE) -> None:
        self.tune = tune
        self._text_view = ''

    def _generate_all_notes(self) -> List[List[Note]]:
        """"""
        pass

    def __str__(self) -> str:
        return self._text_view


grif = Grif(('e', 'g', 'c'))

print(grif)

