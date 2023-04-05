# quickImportRender
Quick import your render by selecting the write node and use 'shift+r' on keyboard. 

## install
1. Copy writeReader.py to your .nuke folder.
2. Add the following to your menu.py file:

from writeReader import *

nuke.menu('Nodes').addCommand('Golan gizmos/Golan/writeReader', "writeRender()", "shift+r")
