from matplotlib.font_manager import json_dump
import xml.etree.ElementTree as ET
import easygui
import utils


music_xml_file_name = easygui.fileopenbox(msg="Please select a MusicXML file",default='MusicXMLs\\*.musicxml',filetypes=["*.musicxml"])

mytree = ET.parse(music_xml_file_name.replace("\\","\\\\"))
myroot = mytree.getroot()

staves = []
data = "\""

for staff in myroot.iter("staff"):
    if staff.text not in staves:
        staves.append(staff.text)

print(staves)
    
if (len(staves) > 1):
    staff_choice = easygui.choicebox(msg = "There are " + str(len(staves)) + " staves in this peice of music. Which staff would you like to use?",choices= staves)
for measure in myroot.iter("measure"):
    for note in measure.iter("note"):
        if note.find("rest") == None:
            if (len(staves) > 1):
                for staff in note.iter("staff"):
                    if staff.text.__eq__(staff_choice):  
                        data += utils.new_note_str(note) + ","
            else:
                data += utils.new_note_str(note) + ","
    data += "\n"


data = data[0:len(data)-2] #removes the newline character and the last comma

data += "\""

name = "Untitled Song"

for work in myroot.iterfind("work"):
    for work_title in work.iterfind("work-title"):
        name = work_title.text

with open(f"output/{name}.txt","w") as file:
    file.write(data)
    

