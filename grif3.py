'''This is my 3 try to write normal grif note drawing'''
from typing import Literal, Tuple, List, Callable, NamedTuple
from colorama import Fore


Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
NOTE_SEQUENCE: Tuple[Note, ...] = ('a', 'a#', 'b', 'c', 'c#', 'd',
                                   'd#', 'e', 'f', 'f#', 'g', 'g#')


class ColorOfNote(NamedTuple):
    color: str
    note: Note


Tune = Tuple[Note, ...]
STANDARD_TUNE: Tune = ('e', 'b', 'g', 'd', 'a', 'e')
GridOfNotes = List[List[Note]]


def generate_string_array(note1: Note, n_of_lads: int) -> List[Note]:
    'generate only 1 string [note1, note2, note3 ... note(n_of_lads)]'
    index_of_note1 = NOTE_SEQUENCE.index(note1)
    string = []
    for i in range(n_of_lads):
        index_of_next_note = i + index_of_note1 + 1
        string.append(NOTE_SEQUENCE[index_of_next_note % len(NOTE_SEQUENCE)])
    return string


def generate_all_strings(tune: Tune, n_of_lads: int) -> GridOfNotes:
    """Return list of lists with notes
    tune is tuple of notes"""
    grid_of_notes = []
    for note1 in tune:
        string = generate_string_array(note1, n_of_lads)
        grid_of_notes.append(string)
    return grid_of_notes


def for_each(grif: List[List[Note]],
             func: Callable[[Note], str]) -> GridOfNotes:
    'this function applyed to all notes in grif'
    new_grif = []
    for string in grif:
        new_grif.append(list(map(func, string)))
    return new_grif


def replace_all_notes_except(exception_notes: Tuple[Note],
                             replace_by: str,
                             grid_of_notes: GridOfNotes) -> GridOfNotes:
    'Replace all notes in grid_of_notes by replace_by string'
    def replace(note):
        return note if note in exception_notes else replace_by
    new_grif = for_each(grid_of_notes, replace)
    return new_grif


def paint_notes(color_notes_dict: ColorOfNote,
                grid_of_notes: GridOfNotes):
    'wrap all notes in grid'

    def painter(note):
        if note in color_notes_dict:
            return color_notes_dict[note]
        return Fore.WHITE + note + Fore.WHITE

    new_grid_of_notes = for_each(grid_of_notes, painter)
    return new_grid_of_notes


def text_formatter(grid_of_notes: GridOfNotes) -> str:
    '''crete text from grif_of_notes.
    Then it might be printed in console for example'''
    raise NotImplementedError


if __name__ == '__main__':
    grif = generate_all_strings(('e', 'b', 'g', 'd', 'a', 'e'), 15)
    grif = replace_all_notes_except(('c', 'e', 'g'), '-', grif)
    colors = ColorOfNote('RED', ('e', 'c', 'g'))
    print(colors.color)
    # grif = paint_notes(colors, grif)
    # for_each(grif, print)

