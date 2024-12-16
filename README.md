# Advent of Code Progress Tracker

This repository tracks my progress as I solve puzzles from [Advent of Code](https://adventofcode.com) from 2015 to 2024 and beyond. Each puzzle has two parts, and I'll mark them as `✅` when solved or `❌` otherwise. I'll also add notes for interesting learnings or challenges faced during the process.

---

## Advent of Code 2024

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      | Lists and counters for the win!                               |
| 2   | ✅      | ✅      | Lists and `np.diff` operations        |
| 3   | ✅      | ✅      | `re.finditer()` and `re.findall()` worked like magic. Could the part2 code be made shorter? Perhaps a task for the future.                                |
| 4   | ✅      | ✅      | Search for substring (`XMAS`) in a grid in all directions. Boundary check for indices.                               |
| 5   | ✅      | ✅      | Custom iterative sorting mechanism was needed. Topological sorting failed due to cycles and exhaustive permutation for part 2 failed due to scalability issues. What a way to learn how sorting operations work 😅!                          |
| 6   | ✅      | ✅      |  Solving bouncing-board-snake-style game on the grid. Part 2 took 50 seconds to brute-force through all alternatives (perhaps there are ways to avoid duplicate searches?). Key lessons: using `pretty_print_grids()` (in `part2.py`) aided debugging, and storing the grid as a list of character lists proved more efficient.                             |
| 7   | ✅      | ✅      | `itertools.product()` did the magic of generating all outcomes from the toss of the operator "coin" being two numbers. Took 14.5 seconds for part2, which could be improved!                               |
| 8   | ✅      | ✅      | Goal was to find linear alignments of points in a grid. Logic--first collect the coordinates of each unique character. Then use `itertools.combinations` and coordinate geometry to generate line segment points and extends them in both directions until the grid boundary is reached.  Fun puzzle!                            |
| 9   | ✅      | ✅      | Goal was to remove white spaces by pushing file IDs from the end to the front. Somewhat long logic using careful edits to list start and end indices.                            |
| 10  | ✅      | ✅      | Goal was to *count the number of paths* in a topologically sorted network with a set of start and end points. I struggled with choosing the right graph algorithm till realizing the network has a topological order.                           |
| 11  | ✅      | ✅      | Goal: Apply a defined rule to manipulate numbered stones for a set number of "blinks" (iterations). For 25 blinks, simple recursion worked well; for 75 blinks, using `lru_cache` was more efficient. The key insight is that we only need the final count of stones, not their specific values.                               |
| 12  | ✅      | ❌      | Still working on part 2. Perhaps some good way to find connected components in a graph!                              |
| 13  | ✅      | ✅      | Use Cramer's rule to solve two linear equations. A fun one!                              |
| 14  | ✅      | ✅      | Part 1 was a recursive update to x and y coordinates. Part 2 felt like brute force to find the tree-looking easter egg. There is fortunately a pattern where x and y coordinates update independently and repeat in vertical and horizontal grouped patterns after every max_col and max_row timesteps.                             |
| 15  | ✅      | ❌      |  Part 1 was a reasonable move logic. Part 2 is involved. It seems like a BFS at every move to determine which blocks will move and then updating it. I wonder if `networkx` can solve it? A task for the future self.                             |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2023
I have solved some of these in a different notebook, but yet to include the attempts on Github.

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ❌      | ❌      |                                 |
| 2   | ❌      | ❌      |                                 |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2022

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      | Addition over lists.                                |
| 2   | ✅      | ✅      | Rock-paper-scissor!                                |
| 3   | ✅      | ✅      | Learned about `ord()` string function.                                |
| 4   | ✅      | ✅      | Finding overlap of two lists                              |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2021

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      | Take difference of lists and count the positives. Use `numpy` though.                    |
| 2   | ✅      | ✅      | Simple logic after input splitting.                                |
| 3   | ✅      | ✅      |  (1) Good use of counters, zip to swap columns as rows, reversed, and boolean logic, (2) Good use of functions with changing list copies.                               |
| 4   | ✅      | ✅      |   Bingo analysis                            |
| 5   | ✅      | ✅      |   Draw lines and their meeting points                            |
| 6   | ✅      | ✅      | Recursion and LRU cache for the win! 🎉                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2020

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      |  For now a blind nested loops to a tuple of numbers `T` such that: `T \subseteq numbers`,`mod(T) = k`, and `sum(T) = d` though recursion can work. |
| 2   | ✅      | ✅      |  One line input splitting; Counter and xor operations.                               |
| 3   | ✅      | ✅      |  Cycle through column indices using `itertools`.                               |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2019

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      |  Recursive function with a twist!                               |
| 2   | ✅      | ✅      |  List indexing carefully executed. There might be a smarter approach for part 2 than brute-force checking all nouns and verbs, but oh well. It took less than a second on my machine!                               |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2018

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      | First part was a simple sum. However, `itertools` saved the logic for part 2. Probably there might be more efficient ways!                                |
| 2   | ❌      | ❌      |                                 |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2017

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      | List indexing magic. Could there be a better logic for cyclicity?                               |
| 2   | ✅      | ✅      | List combinatorics. Helpful tools: `itertools` combination and `re.findall()`                              |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2016

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ❌      |   Found a way to track coordinates. Still pondering how to estimate the crossing point!                              |
| 2   | ❌      | ❌      |                                 |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Advent of Code 2015

| Day | Part 1 | Part 2 | Notes                           |
|-----|--------|--------|---------------------------------|
| 1   | ✅      | ✅      |  Character loops for the win.            |
| 2   | ✅      | ✅      |  Lambda functions and Regex help simplify.                               |
| 3   | ❌      | ❌      |                                 |
| 4   | ❌      | ❌      |                               |
| 5   | ❌      | ❌      |                               |
| 6   | ❌      | ❌      |                               |
| 7   | ❌      | ❌      |                               |
| 8   | ❌      | ❌      |                               |
| 9   | ❌      | ❌      |                               |
| 10  | ❌      | ❌      |                               |
| 11  | ❌      | ❌      |                               |
| 12  | ❌      | ❌      |                               |
| 13  | ❌      | ❌      |                               |
| 14  | ❌      | ❌      |                               |
| 15  | ❌      | ❌      |                               |
| 16  | ❌      | ❌      |                               |
| 17  | ❌      | ❌      |                               |
| 18  | ❌      | ❌      |                               |
| 19  | ❌      | ❌      |                               |
| 20  | ❌      | ❌      |                               |
| 21  | ❌      | ❌      |                               |
| 22  | ❌      | ❌      |                               |
| 23  | ❌      | ❌      |                               |
| 24  | ❌      | ❌      |                               |
| 25  | ❌      | ❌      |                               |

---

## Notes

- ✅: Puzzle solved successfully.
- ❌: Puzzle not solved yet.
- Notes will include interesting learnings, challenges, or algorithms explored during each day's puzzle.

Stay tuned for updates as I continue solving puzzles year by year!
