import pytest

from tests.helpers import *
from src.audio_preprocessing.preprocessing import note_sequence_to_text

def test_note_sequence_to_text1():
    # simple note shifted 1sec to right
    original = 'PIECE_START TRACK_START INST=0 DENSITY=0 BAR_START TIME_DELTA=8.0 NOTE_ON=69 TIME_DELTA=8.0 NOTE_OFF=69 BAR_END TRACK_END PIECE_END\n'
    original_note_sequence = token_sequence_to_note_sequence(original, use_program=False)

    reencoded = note_sequence_to_text(original_note_sequence.notes)

    assert original == reencoded


def test_note_sequence_to_text2():
    # multiple simultanuous notes shifted 1 sec
    original = 'PIECE_START TRACK_START INST=1 DENSITY=0 BAR_START NOTE_ON=50 TIME_DELTA=8.0 NOTE_ON=53 TIME_DELTA=8.0 NOTE_OFF=50 TIME_DELTA=8.0 NOTE_OFF=53 BAR_END BAR_START NOTE_ON=57 TIME_DELTA=8.0 NOTE_ON=48 TIME_DELTA=8.0 NOTE_OFF=57 TIME_DELTA=8.0 NOTE_OFF=48 BAR_END TRACK_END PIECE_END\n'
    original_note_sequence = token_sequence_to_note_sequence(original, use_program=False)

    reencoded = note_sequence_to_text(original_note_sequence.notes)

    assert original == reencoded

def test_note_sequence_to_text3():
    # one note is played while the other one is being played (starts later, ends earlier)
    original = 'PIECE_START TRACK_START INST=0 DENSITY=0 BAR_START TIME_DELTA=8.0 NOTE_ON=69 TIME_DELTA=2.0 NOTE_ON=59 TIME_DELTA=4.0 NOTE_OFF=59 TIME_DELTA=2.0 NOTE_OFF=69 BAR_END TRACK_END PIECE_END\n'
    original_note_sequence = token_sequence_to_note_sequence(original, use_program=False)

    reencoded = note_sequence_to_text(original_note_sequence.notes)

    assert original == reencoded


def test_note_sequence_to_text4():
    # the piece starts from 4th bar
    original = 'PIECE_START TRACK_START INST=0 DENSITY=0 BAR_START BAR_END BAR_START BAR_END BAR_START TIME_DELTA=8.0 NOTE_ON=69 TIME_DELTA=2.0 NOTE_ON=59 TIME_DELTA=4.0 NOTE_OFF=59 TIME_DELTA=2.0 NOTE_OFF=69 BAR_END TRACK_END PIECE_END\n'
    original_note_sequence = token_sequence_to_note_sequence(original, use_program=False)

    reencoded = note_sequence_to_text(original_note_sequence.notes)

    assert original == reencoded


def test_note_sequence_to_text5():
    # Same case 4 with two tracks
    original = 'PIECE_START TRACK_START INST=0 DENSITY=0 BAR_START BAR_END BAR_START BAR_END BAR_START TIME_DELTA=8.0 NOTE_ON=69 TIME_DELTA=2.0 NOTE_ON=59 TIME_DELTA=4.0 NOTE_OFF=59 TIME_DELTA=2.0 NOTE_OFF=69 BAR_END TRACK_END TRACK_START INST=1 DENSITY=0 BAR_START BAR_END BAR_START BAR_END BAR_START TIME_DELTA=8.0 NOTE_ON=69 TIME_DELTA=2.0 NOTE_ON=59 TIME_DELTA=4.0 NOTE_OFF=59 TIME_DELTA=2.0 NOTE_OFF=69 BAR_END TRACK_END PIECE_END\n'
    original_note_sequence = token_sequence_to_note_sequence(original, use_program=False)

    reencoded = note_sequence_to_text(original_note_sequence.notes)
    assert original == reencoded

