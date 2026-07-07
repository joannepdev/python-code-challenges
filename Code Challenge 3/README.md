# Code Challenge 3 - Self-Describing Dates Generator

This code challenge demonstrates a self-describing dates generator.
It represents each date through the utilization of integer values, corresponding to the number of days that have passed
since the establishment of the civilization on the given example.

### Each date is represented by:

- a self-describing number, where the number is read as a count of each digit, ranging from 0 to 9.
- The count occurs in the number.

The d-th date is represented by the d-th such number.

### Each date consists of:

- digits
- counts

Counts always appeared immediately before the corresponding digit.

No digit and count were repeated or overlapped.

## Packages

No packages were used during implementation.

## Results

After generating all date numbers, the following results feature dates ranging from 1 to 2^24.

    22
    4444
    113133
    113331
    222442
    223233
    223332
    224224
    224444
    242242
    330030
    331131
    332232
    334434
    335535
    336636
    337737
    338838
    339939
    442244
    443334
    443433
    444422
    553335
    553533
    ...
    16333115
    16333117
    16333118
    16333119
