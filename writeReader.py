# Script Golan
# 20220323
# keyboard shortcut for inport write nodes render 
# "shift+r"

# to make this work:
# Add the following to your menu.py with out the ''
'''from writeReader import *
nuke.menu('Nodes').addCommand('Golan gizmos/Golan/writeReader', "writeRender()", "shift+r") '''

import nuke 

def writeRender():

    try:
        write = nuke.selectedNode()
        xpos = write['xpos'].value()
        ypos = write['ypos'].value()
        ypos = ypos + 100
        writeFile = write['file'].value()
        writeName = writeFile.split("/")[-1]
    
        # Een lijst gemaakt met meerdere variaties van mogelijke bestandsnamen.
        # Soms werkt het alleen met 1 hashtag en de andere keer met 4.
        nameList = []
        writeNameFixed = writeName.replace("%04d", "#")
        writeNameFixedTwo = writeName.replace("%04d", "####")
        nameList.append(writeNameFixed)
        nameList.append(writeNameFixedTwo)
    
        writeFolder = writeFile.split(writeName)[0]
        writeColorspace = write['colorspace'].value()
    
        
        for seq in nuke.getFileNameList(writeFolder):
            for name in nameList:
                if seq.split()[0] == name:
                    readNode = nuke.createNode('Read')
                    readNode['file'].fromUserText(writeFolder + seq)
                    readNode['colorspace'].setValue(writeColorspace)
                    readNode['xpos'].setValue(xpos)
                    readNode['ypos'].setValue(ypos)

    except:
        pass
        
writeRender()




