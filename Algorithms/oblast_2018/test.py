'''
def backtracking(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in backtracking(array[1:], num):
        yield solution
    for solution in backtracking(array[1:], num - array[0]):
        yield [array[0]] + solution

print(list(backtracking([31, 27, 15, 11, 7, 5], 39))[0])

'''
import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

print(findsubsets([31, 27, 15, 11, 7, 5],39))