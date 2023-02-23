'''
Given two positive integers *seqLen* and *upperBound*, print all increasing sequences of length *seqLen* such that the elements in every sequence are from the first *upperBound* natural numbers.

You can assume *seqLen* will be positive and <= *upperBound*. You may want to write a helper method to recurse easier.


EXAMPLE(S)
printSeq(seqLen=2, upperBound=3)
[1, 2]
[1, 3]
[2, 3]

printSeq(seqLen=3, upperBound=4)
[1, 2, 3]
[1, 2, 4]
[1, 3, 4]
[2, 3, 4]

printSeq(seqLen=1, upperBound=5)
[1]
[2]
[3]
[4]
[5]

printSeq(seqLen=0, upperBound=1)
[]

printSeq(seqLen=0, upperBound=0)
[]

Base case:
length of inner array == seqLen



FUNCTION SIGNATURE
def printSeq(seqLen: int, upperBound: int):
'''


# def printSeq(seqLen: int, upperBound: int):
#     def backtrack(index, path):
#         if len(path) == seqLen:
#             print(path)
#             return

#         for i in range(index, upperBound + 1):
#             path.append(i)
#             backtrack(i + 1, path)
#             print("before ", path)
#             path.remove(i)
#             print("after ", path)

#     return backtrack(1, [])





def printSeq(seqLen: int, upperBound: int) -> None:
    for i in range(1, upperBound - seqLen + 1):
        for seq in generateSubseq(i, seqLen, upperBound):
            print(seq)

def generateSubseq(start: int, length: int, upperBound: int):
    if length == 1:
        return [[start+i] for i in range(upperBound-start+1)]
    else:
        result = []
        print(upperBound-length+2)
        for i in range(start, upperBound-length+2):
            for subseq in generateSubseq(i+1, length-1, upperBound):
                result.append([i] + subseq)
        return result

# 3-2+2
print(printSeq(seqLen=2, upperBound=3))
# print(printSeq(seqLen=3, upperBound=4))
# print(printSeq(seqLen=1, upperBound=5))
# print(printSeq(seqLen=0, upperBound=1))
# print(printSeq(seqLen=0, upperBound=0))
