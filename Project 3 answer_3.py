#!/usr/bin/env python

import sys

try:
    staff_txt = sys.argv[1]
    doors_txt = sys.argv[2]

    staff = {}
    with open(staff_txt) as f:
        for line in f:
            id, name = line.strip().split(' ', 1)
            staff[int(id)] = name

    currently_in_building = set()

    with open(doors_txt) as f:
        i = 1
        for line in f:
            line = line.strip().split()
            id = int(line[0])
            door = int(line[1])
            i += 1

            if id in currently_in_building:

                currently_in_building.remove(id)
                action = 'has left'
            else:

                currently_in_building.add(id)
                action = 'has entered'

            print(f'Door Activation {i - 1}\n{staff[id]} accessed Door {door}.\n{staff[id]} {action} the building.')

            if currently_in_building:
                print('In the building:', ', '.join(staff[id] for id in sorted(currently_in_building)))
            else:
                print('The building is empty.')

    print("Final list of staff in the building:")
    for id in sorted(currently_in_building):
        print(f"{staff[id]}")
except IndexError:
    print(f"answer_3.py: Cannot open ")
    sys.exit()
