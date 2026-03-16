# Collatz's Hypothesis

## Overview

The Collatz Conjecture, also known as the 3n+1 problem, is one of the most famous unsolved problems in mathematics. Despite its simple formulation, it remains unproven for over 80 years.

## The Conjecture

For any positive integer *n*:

- If *n* is even: divide it by 2
- If *n* is odd: multiply by 3 and add 1
- Repeat this process

**The Conjecture:** No matter what positive integer you start with, you will always eventually reach 1.

## This Script

This implementation computes the Collatz sequence for any natural number and counts the total number of steps required to reach 1.

## Usage

```bash
python "Collatz's_Hypothesis.py"
```

Enter a natural number at the prompt. The script will:
1. Display each value in the sequence
2. Count the number of steps taken
3. Print the total step count when the sequence reaches 1

## Example

```
Input: 5
Output sequence: 16 → 8 → 4 → 2 → 1
Steps: 5
```
