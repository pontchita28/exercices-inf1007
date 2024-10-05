#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    # conversion des angles degrés en rad 
    angle_deg_rad = math.trunc(math.radians(angle_degs))
    difference_deg = angle_degs - angle_deg_rad
    angle_min_rad = math.radians(difference_deg)
    difference_min = angle_mins - angle_min_rad
    angle_sec_rad = math.radians(difference_min)

    total = angle_deg_rad + angle_min_rad + angle_sec_rad

    return total 


def to_degrees(angle_rads: float) -> tuple:
    angle_rad_deg = (angle_rads * 180)/ math.pi
    angle_min_deg = angle_rads * 10800 / math.pi
    angle_min_sec = angle_rads * 64800 / math.pi
    return angle_rad_deg, angle_min_deg, angle_min_sec


def to_celsius(temperature: float) -> float:
    farenheit = (temperature - 32) / 1.8
    return farenheit


def to_farenheit(temperature: float) -> float:
    farenheit = (temperature * 1.8) + 32 
    return farenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
