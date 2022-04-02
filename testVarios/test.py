import datetime


def calculateDaysBetweenDates(begin, end):
    begin = datetime.datetime.strptime(begin, "%d/%m/%Y")
    end = datetime.datetime.strptime(end, "%d/%m/%Y")
    return (end - begin).days
print(calculateDaysBetweenDates("01/01/2020", "01/01/2021"))

def bubleSortingAlgorithm(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def generateBinaryTree(list):
    if len(list) == 1:
        return list[0]
    else:
        return generateBinaryTree(list[:len(list)//2]) + generateBinaryTree(list[len(list)//2:])