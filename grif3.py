'''This is my 3 try to write normal grif note drawing'''
from typing import Literal, Tuple, List, Callable, NamedTuple, TypedDict, Dict
from colorama import Fore
import numpy as np


Note = Literal['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e',
               'f', 'f#', 'g', 'g#', '-']
NOTE_SEQUENCE: Tuple[Note] = ('a', 'a#', 'b', 'c', 'c#', 'd',
                                   'd#', 'e', 'f', 'f#', 'g', 'g#')


Tune = Tuple[Note, ...]
STANDARD_TUNE: Tune = ('e', 'b', 'g', 'd', 'a', 'e')
GridOfNotes = List[List[Note]]


color_of_chord: Dict[str, Tuple[Note]] = {}


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
    return np.array(grid_of_notes)


def for_each(grif: List[List[Note]],
             func: Callable[[Note], str]) -> GridOfNotes:
    'this function applyed to all notes in grif'
    new_grif = []
    for string in grif:
        new_grif.append(list(map(func, string)))
    return new_grif


def replace_all_notes_except(grid_of_notes: GridOfNotes) -> GridOfNotes:
    'Replace all notes in grid_of_notes by replace_by string'
    note_exception = np.array(
        [values for values in color_of_chord.values()]).reshape(-1)
    mask = np.isin(grid_of_notes, note_exception)
    return np.where(mask, grid_of_notes, '-')


def paint_notes(grid_of_notes: GridOfNotes):
    'wrap all notes in grid'
    copy_grid_of_notes = generate_all_strings(STANDARD_TUNE,
                                              grid_of_notes.shape[1])
    for color in color_of_chord:
        for note in color_of_chord[color]:
            mask = copy_grid_of_notes == note
            colored_note = Fore.__dict__[color] + note + Fore.WHITE
            grid_of_notes[mask] = colored_note

    print(grid_of_notes)
    return grid_of_notes



def text_formatter(grid_of_notes: GridOfNotes,
                   width_of_lad: int = 5,) -> str:
    '''crete text from grif_of_notes.
    Then it might be printed in console for example'''
    text = ''
    for string in grid_of_notes:
        for note in string:
            text += note.center(width_of_lad + 10, '-') + '|'
        text += '\n'
    lad_numbers = ''
    for lad_number in ('', '', 'III', '', 'V', '',
                       'VII', '', 'IX', '', '', 'XII'):
        lad_numbers += lad_number.center(width_of_lad + 1, ' ')

    return text + lad_numbers


if __name__ == '__main__':
    grif = generate_all_strings(('e', 'b', 'g', 'd', 'a', 'e'), 15)
    color_of_chord['RED'] = ('a', 'c', 'e')
    color_of_chord['BLUE'] = ('g', 'b', 'd')
    grif = replace_all_notes_except(grif)
    paint_notes(grif)
    # print(grif == 'c')
