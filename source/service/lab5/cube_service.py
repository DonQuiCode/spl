import math
import sys
import time
import random
import numpy as np
from colorama import Fore

class CubeService:
    def __init__(self, width: int, bg: str = ' ', distance: int = 100, speed: float = 0.6):
        self.__angles: np.array = np.array([0, 0, 0], dtype=float)

        self.__width: int = width
        self.__screen_width: int = 160
        self.__screen_height: int = 44

        self.__bg: str = bg
        self.__z_buffer: list[float] = [0] * self.__screen_width * self.__screen_height
        self.__buffer: list[str] = [self.__bg] * self.__screen_width * self.__screen_height

        self.__distance: int = distance
        self.__h_offset: float = -2 * self.__width
        self.__k1: float = 40

        self.__speed: float = speed
        
    def input_values(self):
        try:
            self.__width = input("Enter the width: ")
            self.__speed = input("Enter the speed of rotation: ")
            if input("Do you want to change the background character? (y/n): ") == "y":
                self.__bg = input("Enter the background character: ")
        except ValueError as e:
            raise type(e)("The format of the number is invalid")
        except Exception as e:
            raise type(e)("An unexpected error occurred")

    def euler_to_rotation_matrix(self, angles):
        # Convert angles to radians
        angles = np.radians(angles)

        # Extract individual angles
        alpha, beta, gamma = angles

        # Rotation matrix for rotation about x-axis
        R_x = np.array([[1, 0, 0],
                        [0, math.cos(alpha), -math.sin(alpha)],
                        [0, math.sin(alpha), math.cos(alpha)]])

        # Rotation matrix for rotation about y-axis
        R_y = np.array([[math.cos(beta), 0, math.sin(beta)],
                        [0, 1, 0],
                        [-math.sin(beta), 0, math.cos(beta)]])

        # Rotation matrix for rotation about z-axis
        R_z = np.array([[math.cos(gamma), -math.sin(gamma), 0],
                        [math.sin(gamma), math.cos(gamma), 0],
                        [0, 0, 1]])

        # Combined rotation matrix
        R = np.dot(R_z, np.dot(R_y, R_x))

        return R

    def __rotate_point(self, x: float, y: float, z: float) -> np.array:
        rot_matrix = self.euler_to_rotation_matrix(self.__angles)
        return np.dot(rot_matrix, [x, y, z])

    def __rotate_face(self, c_x: float, c_y: float, c_z: float, ch: str) -> None:
        x, y, z = self.__rotate_point(c_x, c_y, c_z)
        z += self.__distance

        xp = int(self.__screen_width / 2 + self.__h_offset + 2 * self.__k1 * x / z)
        yp = int(self.__screen_height / 2 + self.__k1 * y / z)

        ooz = 1 / z
        i = xp + yp * self.__screen_width
        if 0 <= i < len(self.__z_buffer) and ooz > self.__z_buffer[i]:
            self.__z_buffer[i] = ooz
            self.__buffer[i] = ch

    def update(self) -> None:
        self.__z_buffer: list[float] = [0] * self.__screen_width * self.__screen_height
        self.__buffer: list[str] = [self.__bg] * self.__screen_width * self.__screen_height

        x = -self.__width
        while x < self.__width:
            y = -self.__width
            while y < self.__width:
                self.__rotate_face(x, y, -self.__width, Fore.RED + '/')
                self.__rotate_face(self.__width, y, x, Fore.BLUE + '.')
                self.__rotate_face(-self.__width, y, -x, Fore.YELLOW + '-')
                self.__rotate_face(-x, y, self.__width, Fore.MAGENTA + ',')
                self.__rotate_face(x, -self.__width, -y, Fore.GREEN + '+')
                self.__rotate_face(x, self.__width, -y, Fore.WHITE + '*')

                y += self.__speed

            x += self.__speed

        self.__angles += np.array([0.5, 0.5, 0.15])

    def draw(self) -> None:
        for n, c in enumerate(self.__buffer):
            if not isinstance(c, str):
                c = str(c)
            if c == '2':
                sys.stdout.write(' ' if n % self.__screen_width else '\n')
            else:
                sys.stdout.write(c if n % self.__screen_width else '\n')


            
    def display_cube(self):
        try:
            #self.input_values()
            sys.stdout.write('\x1b[2J')
            while True:
                sys.stdout.write('\x1b[H')

                self.update()
                self.draw()
        except KeyboardInterrupt:
            sys.stdout.write('\x1b[2J')
            sys.stdout.write('\x1b[H')