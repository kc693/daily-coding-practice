""" This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1 """

testMat = [[1, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
testMat2 = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
testMat3 = [[1, 1, 0, 1, 1], [1, 0, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
testMat4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def flatten(mat):
    final = []
    for row in mat:
        for val in row:
            final.append(val)
    return final

print(f'flatten(testMat) returns {flatten(testMat)}')

def countIslands(mat):
    # count number of negative changes
    count = 0
    
    # flatten matrix first
    arr = flatten(mat)

    # check if len(arr) <= 2. If so, return 0 automatically
    if len(arr) <= 2:
        return 0
    else:
        # check for first instance of 0, then change when change from 1 to 0
        for elem in range(len(arr)-1):
            if arr[elem+1]-arr[elem] == -1:
                count += 1

    # return count. If first element is 1, then subtract 1
    if arr[0] == 1:
        return count - 1
    else:
        return count

print(f'function on test matrix {testMat} returns {countIslands(testMat)}')
print(f'function on test matrix {testMat2} returns {countIslands(testMat2)}')
print(f'function on test matrix {testMat3} returns {countIslands(testMat3)}')
print(f'function on test matrix {testMat4} returns {countIslands(testMat4)}')