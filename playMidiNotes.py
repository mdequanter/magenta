import pygame
import pygame.midi
import time

# initialize the midi module before you use it.
#  pygame.init does not do this for you.
pygame.midi.init()

# print the devices and use the last output port.
for i in range(pygame.midi.get_count()):
    r = pygame.midi.get_device_info(i)
    (interf, name, is_input, is_output, is_opened) = r
    print (i,interf, name, is_input, is_output, is_opened)
    if is_output:
        last_port = i

# You could also use this to use the default port rather than the last one.
# default_port = pygame.midi.get_default_output_id()

midi_out = pygame.midi.Output(3, 0)

# select an instrument.
instrument = 19 # general midi church organ.  # Piano
midi_out.set_instrument(instrument)


def playChord(note, secs) :
    midi_out.note_on(note=note, velocity=127)
    midi_out.note_on(note=note+5, velocity=127)
    midi_out.note_on(note=note+10, velocity=127)
    time.sleep(secs)
    midi_out.note_off(note=note, velocity=0)
    midi_out.note_off(note=note+5, velocity=0)
    midi_out.note_off(note=note+10, velocity=0)

def playNote(note, secs) :
    midi_out.note_on(note=note, velocity=127)
    time.sleep(secs)
    midi_out.note_off(note=note, velocity=0)



playNote(60,0.5)
playNote(64,0.5)
playNote(68,0.5)

playChord(60,0.5)
playChord(64,0.5)
playChord(68,0.5)


