import math
import random as rn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

def righttriangle(x1,y1,x2,y2,x3,y3):
    abx= x2-x1
    aby = y2-y1
    acx = x3 - x1
    acy = y3 - y1
    bcx = x3 - x2
    bcy = y3 - y2
    ab_2 = abx**2+aby**2
    ac_2 = acx**2+acy**2
    bc_2 = bcx**2+bcy**2
    if ab_2+ac_2 == bc_2 or ab_2+bc_2 == ac_2 or ac_2+bc_2 == ab_2:
        return True
    return False

def Randpunkt(tab, rangex, rangey):
    for i in range(len(tab)):
        tab[i][0] = rn.randint(-rangex, rangex)
        tab[i][1] = rn.randint(-rangey, rangey)
    return tab


def Inside_triangle(xp, yp, x1, y1, x2, y2, x3, y3):
    trianglearea = 0
    area_sum = 0
    trianglearea = triangle_area(x1, y1, x2, y2, x3, y3)
    area_sum = triangle_area(xp, yp, x2, y2, x3, y3)
    area_sum += triangle_area(x1, y1, xp, yp, x3, y3)
    area_sum += triangle_area(x1, y1, x2, y2, xp, yp)
    if area_sum == trianglearea or trianglearea == 0:
        return True
    else:
        return False


def check_if_parrarell_toox_and_oy(x1, y1, x2, y2):
    if (x1 == x2):
        return True
    else:
        if (y1 == y2):
            return True
    return False


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def npt(dane):
    print(dane)
    numberofnonparrarell = 0
    nonparrarelltriangles = [Triangle(0, 0, 0, 0, 0, 0) for _ in range(n ** 3)]
    nonparrarrell_without_point_inside_triangles = [Triangle(0, 0, 0, 0, 0, 0) for _ in range(n ** 3)]

    dane_x = [[0] for _ in range(n)]
    for i in range(n):
        dane_x[i] = dane[i][0]
    dane_y = [[0] for _ in range(n)]
    for i in range(n):
        dane_y[i] = dane[i][1]
    numpy_dane_x = np.asarray(dane_x)
    numpy_dane_y = np.asarray(dane_y)
    for i in range(n):
        for j in range(i + 1, n):
            if not check_if_parrarell_toox_and_oy(dane[i][0], dane[i][1], dane[j][0], dane[j][1]):
                for k in range(j + 1, n):
                    if check_if_parrarell_toox_and_oy(dane[i][0], dane[i][1], dane[k][0],
                                                      dane[k][1]) == False and check_if_parrarell_toox_and_oy(
                        dane[j][0],
                        dane[j][1],
                        dane[k][0],
                        dane[k][
                            1]) == False:
                        nonparrarelltriangles[numberofnonparrarell].x1 = dane[i][0]
                        nonparrarelltriangles[numberofnonparrarell].y1 = dane[i][1]
                        nonparrarelltriangles[numberofnonparrarell].x2 = dane[j][0]
                        nonparrarelltriangles[numberofnonparrarell].y2 = dane[j][1]
                        nonparrarelltriangles[numberofnonparrarell].x3 = dane[k][0]
                        nonparrarelltriangles[numberofnonparrarell].y3 = dane[k][1]
                        numberofnonparrarell += 1
    number_of_non_parrarel_without_point_inside_triangles = 0;
    for i in range(numberofnonparrarell):
        temp = False
        for j in range(len(dane)):
            if (nonparrarelltriangles[i].x1 != dane[j][0] or nonparrarelltriangles[i].y1 != dane[j][1]) and (
                    nonparrarelltriangles[i].x2 != dane[j][0] or nonparrarelltriangles[i].y2 != dane[j][1]) and (
                    nonparrarelltriangles[i].x3 != dane[j][0] or nonparrarelltriangles[i].y3 != dane[j][1]):
                if Inside_triangle(dane[j][0], dane[j][1], nonparrarelltriangles[i].x1, nonparrarelltriangles[i].y1,
                                   nonparrarelltriangles[i].x2, nonparrarelltriangles[i].y2,
                                   nonparrarelltriangles[i].x3, nonparrarelltriangles[i].y3) \
                        or not righttriangle(nonparrarelltriangles[i].x1, nonparrarelltriangles[i].y1,
                                   nonparrarelltriangles[i].x2, nonparrarelltriangles[i].y2,
                                   nonparrarelltriangles[i].x3, nonparrarelltriangles[i].y3):
                    temp = True
                    break
        if not temp:
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].x1 = \
                nonparrarelltriangles[i].x1
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].x2 = \
                nonparrarelltriangles[i].x2
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].x3 = \
                nonparrarelltriangles[i].x3
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].y1 = \
                nonparrarelltriangles[i].y1
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].y2 = \
                nonparrarelltriangles[i].y2
            nonparrarrell_without_point_inside_triangles[number_of_non_parrarel_without_point_inside_triangles].y3 = \
                nonparrarelltriangles[i].y3
            number_of_non_parrarel_without_point_inside_triangles += 1
    cline = [[[], []] for _ in range(3)]
    print(number_of_non_parrarel_without_point_inside_triangles)
    for i in range(number_of_non_parrarel_without_point_inside_triangles):
        line1 = (
            [nonparrarrell_without_point_inside_triangles[i].x1, nonparrarrell_without_point_inside_triangles[i].y1],
            [nonparrarrell_without_point_inside_triangles[i].x2, nonparrarrell_without_point_inside_triangles[i].y2])
        line2 = (
            [nonparrarrell_without_point_inside_triangles[i].x1, nonparrarrell_without_point_inside_triangles[i].y1],
            [nonparrarrell_without_point_inside_triangles[i].x3, nonparrarrell_without_point_inside_triangles[i].y3])
        line3 = (
            [nonparrarrell_without_point_inside_triangles[i].x2, nonparrarrell_without_point_inside_triangles[i].y2],
            [nonparrarrell_without_point_inside_triangles[i].x3, nonparrarrell_without_point_inside_triangles[i].y3])
        cline[0] = line1
        cline[1] = line2
        cline[2] = line3
        lc = LineCollection(cline, linewidths=2)
        fig, ax = plt.subplots()
        ax.add_collection(lc)
        plt.plot(numpy_dane_x, numpy_dane_y, "o")
        plt.autoscale()
        plt.grid()
        plt.show()
    if (number_of_non_parrarel_without_point_inside_triangles == 0):
        return False
        plt.plot(numpy_dane_x, numpy_dane_y, "o")
        plt.autoscale()
        plt.show()
    else:
        return True


# wczytanie ilo??ci punkt??w
n = int(input("Number of points: "))

# wczytanie tablic
dane = [[[0], [0]] for _ in range(n)]
nonparrarelltriangles = [Triangle(0, 0, 0, 0, 0, 0) for _ in range(n ** 3)]
nonparrarrell_without_point_inside_triangles = [Triangle(0, 0, 0, 0, 0, 0) for _ in range(n ** 3)]

# wczytanie zakresu x i y
rx = int(input("Range for x: "))
ry = int(input("Range for y: "))

# losowe wybranie punkt??w
dane = Randpunkt(dane, rx, ry)

npt(dane)

