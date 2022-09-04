#!/usr/bin/python
import math
import time

import mouse
import screeninfo as si

__author__ = "Simon Josef Kreuzpointner"


def main():
    sampling_rate = 10
    total = 0
    info = si.get_monitors()[0]
    scale_x = info.width_mm / info.width
    scale_y = info.height_mm / info.height
    prev_pixel_position = mouse.get_position()
    try:
        while True:
            cur_pixel_position = mouse.get_position()
            d = distance_between_points(
                scale_position(cur_pixel_position, scale_x, scale_y),
                scale_position(prev_pixel_position, scale_x, scale_y)
            )
            total += d
            print(format_mm(total), end="\r")
            prev_pixel_position = cur_pixel_position
            time.sleep(1 / sampling_rate)
    except KeyboardInterrupt:
        print("You traveled a total distance of:\n", format_mm(total))


def scale_position(pixel_position, scale_x, scale_y):
    return pixel_position[0] * scale_x, pixel_position[1] * scale_y


def distance_between_points(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def format_mm(mm):
    cm = math.floor(mm / 10)
    dm = math.floor(cm / 10)
    m = math.floor(dm / 10)
    km = math.floor(m / 1000)

    actual_m = m - km * 1000
    actual_dm = dm - m * 10
    actual_cm = cm - dm * 10
    actual_mm = mm - cm * 10

    return f"{str(km).rjust(5)} km {str(actual_m).rjust(3)} m {str(actual_dm).rjust(2)} dm " + \
           f"{str(actual_cm).rjust(2)} cm {str(math.trunc(actual_mm)).rjust(2)} mm"


if __name__ == "__main__":
    main()
