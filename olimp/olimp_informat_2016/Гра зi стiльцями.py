r = open("input.txt", "r").read().split("\n")
temp = r[0].split(" ")
N, M = int(temp[0]), int(temp[1])
A = [int(i) for i in r[1].split(" ")]
mass = []
