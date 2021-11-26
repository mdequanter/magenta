import sys
import os

import pygame as pg
import pygame.midi


def playNote(midi_out,note) :
    midi_out.note_on(note=note, velocity=127)
def stopNote(midi_out,note) :
    midi_out.note_off(note=note, velocity=0)


def process_midi_input(midi_data):
    midi_note, timestamp = midi_data[0]
    note_status, keynum, velocity, unused = midi_note #unpack tuple
    return (note_status, keynum, velocity, timestamp)

def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()


def _print_device_info():
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )


def input_main(device_id=None):
    pg.init()
    pg.fastevent.init()
    event_get = pg.fastevent.get
    event_post = pg.fastevent.post

    pygame.midi.init()

    _print_device_info()

    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id = device_id

    print("using input_id :%s:" % input_id)
    i = pygame.midi.Input(input_id)

    print("using output_id :%s:" % 3)
    midi_out = pygame.midi.Output(3, 0)

    # select an instrument.
    instrument = 1  # general midi church organ.  # Piano
    midi_out.set_instrument(instrument)

    pg.display.set_mode((1, 1))



    going = True
    while going:
        events = event_get()
        for e in events:
            if e.type in [pg.QUIT]:
                going = False
            if e.type in [pg.KEYDOWN]:
                going = False
            if e.type in [pygame.midi.MIDIIN]:
                print(e)

        if i.poll():
            midi_events = i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                #event_post(m_e)
                status = m_e.status
                noteCode = m_e.data1
                #playing notes
                if (noteCode >=36 and noteCode<=84) :
                    if (status == 144) :
                        playNote(midi_out,noteCode)
                    if (status == 128) :
                        noteCode = m_e.data1
                        stopNote(midi_out, noteCode)
                #change instrument
                # check list: https://fmslogo.sourceforge.io/manual/midi-instrument.html
                if (noteCode == 24) :
                    instrument = instrument - 1
                    if (instrument < 1) :
                        instrument = 1
                    print ("instrument set to:" + str(instrument))
                    midi_out.set_instrument(instrument)
                if (noteCode == 25) :
                    instrument = instrument + 1
                    if (instrument > 127) :
                        instrument = 127

                    print ("instrument set to:" + str(instrument))
                    midi_out.set_instrument(instrument)




    del i
    pygame.midi.quit()


input_main()