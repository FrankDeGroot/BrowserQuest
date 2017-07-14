#!/usr/bin/env python
import os
import subprocess
import sys

import tmx2json

SRC_FILE = 'tmx/map.tmx'
TEMP_FILE = SRC_FILE + '.json'

# Convert the Tiled TMX file to a temporary JSON file
tmx2json.convertTmx2Json(SRC_FILE, TEMP_FILE)

def export(mode):
    if mode == 'client':
        # This will save two files (See exportmap.js)
        destination = '../../client/maps/world_client'
    else:
        destination = '../../server/maps/world_server.json'
    # Map exporting
    print subprocess.call(['node', './exportmap.js', TEMP_FILE, destination, mode])
    # Send a Growl notification when the export process is complete
    if sys.platform == 'darwin':
        print subprocess.call('growlnotify --appIcon Tiled -name "Map export complete" -m "' + destination + ' was saved"')
    else:
        print 'Map export complete: ' + destination + ' was saved.'

if len(sys.argv) == 1:
    export('client')
    export('server')
else:
    export(sys.argv[1])

# Remove temporary JSON file
os.remove(TEMP_FILE)
