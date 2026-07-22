# Code Challenge 1 - Longest Increasing Path

This code challenge demonstrates a matrix and path generator, based on the Longest Increasing Path algorithm.

Given a matrix of integers of mxn dimensions, the task is to find the length of the longest increasing path within the matrix.
Starting from any cell, movement to adjacent cells can be achieved in one of four possible directions:

- left
- right
- up
- down

Diagonal movement and movement that goes beyond matrix boundaries (wrap-around) are not allowed.
The path must be strictly increasing, which means each sub-sequent cell in the path must have a higher value than the previous one.

## Packages

- random

## Results

### m and n being the same number

On a random matrix of 10x10 dimensions, the path length is 70.

### Matrix

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [30, 31, 32, 33, 34, 35, 36, 37, 38, 11]
    [29, 52, 53, 54, 55, 56, 57, 58, 39, 12]
    [28, 51, 66, 67, 68, 69, 70, 59, 40, 13]
    [27, 50, 65, 64, 63, 62, 61, 60, 41, 14]
    [26, 49, 48, 47, 46, 45, 44, 43, 42, 15]
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16]

The matrix, given a defined number of dimensions (m=10, n=10) followed the clockwise spiral (snail) filling pattern.

### m and n being a different number

On a random matrix of 20x9 dimensions, the path length is 180.

### Matrix

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [54, 55, 56, 57, 58, 59, 60, 61, 10]
    [53, 100, 101, 102, 103, 104, 105, 62, 11]
    [52, 99, 138, 139, 140, 141, 106, 63, 12]
    [51, 98, 137, 168, 169, 142, 107, 64, 13]
    [50, 97, 136, 167, 170, 143, 108, 65, 14]
    [49, 96, 135, 166, 171, 144, 109, 66, 15]
    [48, 95, 134, 165, 172, 145, 110, 67, 16]
    [47, 94, 133, 164, 173, 146, 111, 68, 17]
    [46, 93, 132, 163, 174, 147, 112, 69, 18]
    [45, 92, 131, 162, 175, 148, 113, 70, 19]
    [44, 91, 130, 161, 176, 149, 114, 71, 20]
    [43, 90, 129, 160, 177, 150, 115, 72, 21]
    [42, 89, 128, 159, 178, 151, 116, 73, 22]
    [41, 88, 127, 158, 179, 152, 117, 74, 23]
    [40, 87, 126, 157, 180, 153, 118, 75, 24]
    [39, 86, 125, 156, 155, 154, 119, 76, 25]
    [38, 85, 124, 123, 122, 121, 120, 77, 26]
    [37, 84, 83, 82, 81, 80, 79, 78, 27]
    [36, 35, 34, 33, 32, 31, 30, 29, 28]

The matrix, given a defined number of dimensions (m=10, n=10) followed the recursive inward spiral (layered spiral) filling pattern.






