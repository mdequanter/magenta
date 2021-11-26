import magenta
import note_seq
import tensorflow


from note_seq.protobuf import music_pb2


# Add the notes to the sequence.
drums = music_pb2.NoteSequence()

drums.notes.add(pitch=36, start_time=0, end_time=0.250, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=38, start_time=0, end_time=0.250, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=0, end_time=0.250, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=46, start_time=0, end_time=0.250, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=0.25, end_time=0.375, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=0.375, end_time=0.5, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=0.5, end_time=0.625, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=50, start_time=0.5, end_time=0.625, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=36, start_time=0.75, end_time=0.875, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=38, start_time=0.75, end_time=0.875, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=0.75, end_time=0.875, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=45, start_time=0.75, end_time=0.875, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=36, start_time=1, end_time=1.125, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=1, end_time=1.125, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=46, start_time=1, end_time=1.125, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=42, start_time=1.25, end_time=1.375, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=48, start_time=1.25, end_time=1.375, is_drum=True, instrument=10, velocity=80)
drums.notes.add(pitch=50, start_time=1.25, end_time=1.375, is_drum=True, instrument=10, velocity=80)
drums.total_time = 1.375

drums.tempos.add(qpm=60)


note_seq.sequence_proto_to_midi_file(drums, 'drums_test.mid')
