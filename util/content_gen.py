import os
import random
import csv


def generateNames(num):
    with open("util/townnames.csv") as f:
        s0 = []
        s1 = []

        # Loop over the remaining lines
        for l in f:
            # Create a list by separating the line at commas
            d = l.split(",")

            if d[0]:
                s0.append(d[0])
            if d[1]:
                s1.append(d[1])
        # Close the file

        namelist = []
        for i in range(num):
            namelist.append(s0[random.randint(0, len(s0) - 1)] +
                            s1[random.randint(0, len(s1) - 1)])
        return namelist


def generateDescription(num):
    with open("util/towndescriptions.csv") as f:
        s0 = []
        s1 = []
        s2 = []

        # Loop over the remaining lines
        for l in f:
            # Create a list by separating the line at commas
            d = l.split("|")
            print(d)
            if d[0]:
                s0.append(d[0])
            if d[1]:
                s1.append(d[1])
            if d[2]:
                s2.append(d[2])
        # Close the file

        descriptionList = []
        for i in range(num):
            descriptionList.append(s0[random.randint(0, len(s0) - 1)] +
                                   s1[random.randint(0, len(s1) - 1)] +
                                   s2[random.randint(0, len(s2) - 1)])
        return descriptionList


def generateRooms():
    rooms = []
    names = generateNames(100)
    descriptions = generateDescription(100)

    for i in range(100):
        rooms.append({
            "title": names[i],
            "description": descriptions[i],

        })
    return rooms


print(generateDescription(2))
