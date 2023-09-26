#!/usr/bin/env python

import sys

CAR_SPEEDLIMIT = 60
VAN_SPEEDLIMIT = 50
HGV_SPEEDLIMIT = 40
BUS_SPEEDLIMIT = 40

car_count = 0
van_count = 0
hgv_count = 0
bus_count = 0
total_count = 0
speeding_count = 0
total_avg_speed = 0


if len(sys.argv) != 2:
    print("answer_2.py: no file name given ")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == 'OFF':
                break

            vehicle_type = line[2]
            speed = int(line[:-2])

            total_count += 1
            total_avg_speed += speed

            if (vehicle_type == 'C' and speed > CAR_SPEEDLIMIT) or \
                    (vehicle_type == 'V' and speed > VAN_SPEEDLIMIT) or \
                    (vehicle_type in ['H', 'B'] and speed > HGV_SPEEDLIMIT):
                speeding_count += 1

            if vehicle_type == 'C':
                car_count += 1
            elif vehicle_type == 'V':
                van_count += 1
            elif vehicle_type == 'H':
                hgv_count += 1
            elif vehicle_type == 'B':
                bus_count += 1

        if total_count > 0:
            car_percent = car_count / total_count * 100
            van_percent = van_count / total_count * 100
            hgv_percent = hgv_count / total_count * 100
            bus_percent = bus_count / total_count * 100

            avg_speed = total_avg_speed / total_count

            speeding_percent = speeding_count / total_count * 100

            print("**** Speed Camera Data Analytics ****\n")
            print("*** Summary  ***\n")
            print(f"Total Vehicles:       {total_count}\n")
            print(f"Percentage Cars:   {car_percent:.2f}%")
            print(f"Percentage Vans:   {van_percent:.2f}%")
            print(f"Percentage Buses:  {bus_percent:.2f}%")
            print(f"Percentage HGVs:   {hgv_percent:.2f}%\n")
            print(f"Average Speed:     {avg_speed:.2f}")
            print(f"percentage of speeder:   {speeding_percent:.2f}%")
        else:
            print("No data found.")

except FileNotFoundError:
    print(f"answer_2.py: Cannot open \"{filename}\"")
    sys.exit()
