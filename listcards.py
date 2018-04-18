# https://apps.ankiweb.net/docs/addons.html
# https://github.com/dae/anki/blob/master/anki/collection.py
# https://www.juliensobczak.com/tell/2016/12/26/anki-scripting.html

import os
import re
# Load Anki library
import sys
sys.path.append('/usr/share/anki')

#prog = re.compile('((.*)(\[(?!sound).*\]))')
prog = re.compile('.*(<img.*/>).*')

from anki.storage import Collection

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser("~/Documents/Anki/User 1") 
cpath = os.path.join(PROFILE_HOME, "collection.anki2")

# Load the Collection
col = Collection(cpath, log=True) # Entry point to the API



# Use the available methods to list the notes
for cid in col.findNotes("deck:current"): 
    #card = col.getCard(cid)
    note = col.getNote(cid)

    for (name, value) in note.items():
        matchSpr = prog.match(value)
        #print(value)
        if matchSpr is not None:
            #print(matchSpr.group(1))<img src='blank.png'/>
            note[name] = matchSpr.group(0).replace('<img src="blank.png" />',"",1)
            print(matchSpr.group(0))
            note.flush()

col.save()
    # for field in note.fields:
    #     matchSpr = prog.match(field)
    #     #print(field)
    #     if matchSpr is not None:
    #         print(matchSpr.group(3))
    #         print(matchSpr.group(2))

    #template = model['tmpls'][card.ord]
    # #front =  note.fields[0] # "Front" is the first field of these cards
    #print(note)
