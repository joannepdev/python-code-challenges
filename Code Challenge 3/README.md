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

## Results

After generating all date numbers on a range from 1 to 11, the following results feature dates ranging from 1 to 2^24.
