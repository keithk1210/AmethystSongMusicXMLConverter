def midiNumToNote(midiNum): #converts a MIDI number to a string in the format f"NoteNameOctave"
    str = ""
    remainder = (midiNum - 21) % 12
    octave = (midiNum - 12) // 12
    if remainder == 0:
        str += "A"
    elif remainder == 1:
        str += "BFLAT"
    elif remainder == 2:
        str += "B"
    elif remainder == 3:
        str += "C"
    elif remainder == 4:
        str += "CSHARP"
    elif remainder == 5:
        str += "D"
    elif remainder == 6:
        str += "DSHARP"
    elif remainder == 7:
        str += "E"
    elif remainder == 8:
        str += "F"
    elif remainder == 9:
        str += "FSHARP"
    elif remainder == 10:
        str += "G"
    elif remainder == 11:
        str += "GSHARP"
    return "%s%d" % (str,octave)

def new_note_str(note):
    new_note = ""
    for pitch in note.iter("pitch"):
        alter = 0
        for step in note.iter("step"):
            new_note += step.text
        for accidental in pitch.iter("alter"):
            if (int(accidental.text) == 1):
                new_note += "SHARP"
                alter = int(accidental.text)
            elif (int(accidental.text) == -1):
                new_note += "FLAT"
                alter = int(accidental.text)
        for octave in note.iter("octave"):
            if (int(octave.text) > 1):
                if (step.text == "C" and alter == 0):
                    new_note += str(2)
                else:
                    new_note += str(1)
            else:
                new_note += octave.text
    return new_note