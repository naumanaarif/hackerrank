# Python If-Else

![Skill](https://img.shields.io/badge/Skill-Python_(Basic)-blueviolet?style=for-the-badge "skill")
![Topic](https://img.shields.io/badge/Topic-Introduction-yellow?style=for-the-badge "topic")
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge "difficulty")
![Max Score](https://img.shields.io/badge/Max%20Score-10-blue?style=for-the-badge "max-score")

## Problem

### Task
Given an integer, $n$, perform the following conditional actions:

* If $n$ is odd, print `Weird`
* If $n$ is even and in the inclusive range of $2$ to $5$, print `Not Weird`
* If $n$ is even and in the inclusive range of $6$ to $20$, print `Weird`
* If $n$ is even and greater than $20$, print `Not Weird`

### Input Format

A single line containing a positive integer, $n$.

### Constraints

* $1 \le n \le 100$

### Output Format

Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

### Sample Input 0

```
3
```

### Sample Output 0

```
Weird
```

### Explanation 0

$n = 3$

$n$ is odd and odd numbers are weird, so print `Weird`.

### Sample Input 1

```
24
```

### Sample Output 1

```
Not `Weird`
```

### Explanation 1

$n = 24$

$n \gt 20$ and $n$ is even, so it is not `weird`.

## Solution

```python
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")
```

*See the source code [here](https://github.com/naumanaarif/hackerrank/blob/main/solutions/python/if_else/if_else.py).*

## Explanation

### Conditionals (if/elif/else)

Read about conditional statements [here](https://realpython.com/python-conditional-statements/).

### Python's `range()` Function

Rather than being a function, `range` is actually an immutable sequence type.

#### Syntax

```python
range(start, stop[, step])
```

See the official documentation for `range` [here](https://docs.python.org/3/library/stdtypes.html#range).
