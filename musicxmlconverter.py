import sys
from matplotlib.font_manager import json_dump
import xml.etree.ElementTree as ET
import easygui
import utils
import os

appdata = os.getenv("APPDATA")
parent_dir = "MusicXMLConverter"
output_dir = "output"
music_xml_dir = "MusicXMLs"
abs_parent_dir = appdata + "\\" + parent_dir
abs_music_xml_dir = appdata + "\\" + parent_dir + "\\" + music_xml_dir
abs_output_dir = appdata + "\\" + parent_dir + "\\" + output_dir

print(abs_music_xml_dir)

if not os.path.exists(abs_parent_dir):
    os.mkdir(abs_parent_dir)
if not os.path.exists(abs_output_dir):
    os.mkdir(abs_output_dir)
if not os.path.exists(abs_music_xml_dir):
    os.mkdir(abs_music_xml_dir)


xmls_in_dir = False

for file in os.listdir(abs_music_xml_dir):
    if (len(file.split(".")) >= 2):
        if (file.split('.')[1] == "musicxml"):
            xmls_in_dir = True

if not xmls_in_dir:
    easygui.msgbox("No .musicxml files were found in MusicXMLs directory. Please insert .musicxmml files in this folder: \n%s." % (abs_music_xml_dir))
    sys.exit()

music_xml_file_name = easygui.fileopenbox(msg="Please select a MusicXML file",default=abs_music_xml_dir + "\\",filetypes=["*.musicxml"])

mytree = ET.parse(music_xml_file_name.replace("\\","\\\\"))
myroot = mytree.getroot()

staves = []
data = "\""

for staff in myroot.iter("staff"):
    if staff.text not in staves:
        staves.append(staff.text)


    
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

with open(f"{abs_output_dir}/{name}.txt","w") as file:
    file.write(data)

easygui.msgbox("File sucessfully created at this location: \n%s." % (f"{abs_output_dir}/{name}.txt"))


    

