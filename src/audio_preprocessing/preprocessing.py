from sortedcontainers import SortedList

def note_sequence_to_text(notes):
    text = "PIECE_START"

    sorted_lists = {}

    for note in notes:
        current_instrument = note.instrument
        current_note = note.pitch
        current_start_time = note.start_time
        current_end_time = note.end_time
        current_bar = current_start_time//2

        sorted_list = sorted_lists.setdefault(current_instrument, SortedList())

        sorted_list.add((current_bar, current_start_time, f'NOTE_ON={current_note}'))
        sorted_list.add((current_bar, current_end_time, f'NOTE_OFF={current_note}'))    

    for instrument, sorted_list in sorted_lists.items():
        # TODO fill density
        text += f' TRACK_START INST={instrument} DENSITY=0 BAR_START'
        time_slider = 0    
        current_bar = 0

        for el in sorted_list:
            event_bar, event_time, event = el

            while event_bar != current_bar:
                current_bar = current_bar + 1
                text += ' BAR_END BAR_START'
                time_slider = current_bar*2

            delta_value = (event_time - time_slider)*8.0

            if delta_value > 0:
                text += f' TIME_DELTA={delta_value}'

            text += f' {event}'
            time_slider = event_time

        text += f' BAR_END TRACK_END'
    text += ' PIECE_END\n'
    return text
