#!/usr/bin/env python3

import json
import socket

hostname = socket.gethostname()

inventory = {
    '_meta': {
        'hostvars': {}
    },
    'all': {
        'children': [
            'ungrouped'
        ]
    },
    'ungrouped': {
        'hosts': [
            hostname
        ]
    }
}

print(json.dumps(inventory, indent=4))

