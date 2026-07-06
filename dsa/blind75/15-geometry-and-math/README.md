# Geometry & Math

## Core idea

This category is less about a single unifying algorithm and more about **careful index/boundary management** (matrix traversal) plus a handful of specific numeric tricks worth memorizing outright (cycle detection for Happy Number, fast exponentiation). The common thread: work out the indexing scheme on paper/whiteboard *before* coding, since these bugs are easy to introduce and hard to spot by staring at code.

**Recognition signal:** the input is a 2D matrix and the question is about traversal order or in-place transformation, or the problem is a small self-contained numeric puzzle (happy number, incrementing a number, exponentiation).

## Key structures & idioms

- **Rotate Image (in-place 90°)**: rotating a matrix 90° clockwise = **transpose** (swap `matrix[i][j]` with `matrix[j][i]`) then **reverse each row**. Two simple, well-known operations composed, instead of deriving the rotation formula from scratch under pressure.
- **Spiral Matrix**: maintain four boundaries (`top`, `bottom`, `left`, `right`), walk right across the top, down the right side, left across the bottom, up the left side, shrinking each boundary after its pass. Re-check bounds after every side (`top <= bottom`, `left <= right`) since a matrix that isn't square can exhaust one dimension before the other.
- **Set Matrix Zeroes (O(1) space)**: instead of a separate visited/marker matrix, use the **first row and first column of the matrix itself** as the marker space — but first check separately whether the first row/column originally contained a zero (since you're about to overwrite them), and apply that to the whole first row/column at the very end.
- **Happy Number (cycle detection without extra space)**: repeatedly applying "sum of squares of digits" either reaches 1 or enters a cycle — this is structurally identical to linked-list cycle detection (see [05. Linked List](../05-linked-list/README.md)). Use Floyd's fast/slow pointer technique on the sequence of values instead of a hash set, for O(1) space.
- **Plus One**: process digits from the rightmost, propagate a carry leftward; only in the all-9s case (`999 -> 1000`) does the array need to grow by one digit — handle that as an explicit final case rather than trying to force it into the main loop.
- **Pow(x, n) — fast exponentiation**: naive repeated multiplication is O(n). Halve the exponent each step instead (`x^n = (x^(n/2))^2`, adjusting for odd `n`), giving O(log n). Handle negative `n` by inverting `x` and negating `n` up front.

## Complexity cheat sheet

| Problem | Naive | Optimized |
|---|---|---|
| Rotate Image | O(n²) time, O(n²) extra space (new matrix) | O(n²) time, O(1) extra space (transpose + reverse in place) |
| Spiral Matrix | — | O(rows × cols) time, O(1) extra space (besides output) |
| Set Matrix Zeroes | O(rows × cols) time, O(rows + cols) space (marker sets) | O(rows × cols) time, O(1) extra space (reuse first row/col) |
| Happy Number | O(cycle length) time, O(cycle length) space (hash set) | Same time, O(1) space (fast/slow pointers) |
| Plus One | O(n) | O(n) — already optimal, the trick is just correct carry handling |
| Pow(x, n) | O(n) repeated multiplication | O(log n) via halving the exponent |

## Common pitfalls

- Rotating a matrix by writing new coordinates by hand instead of using transpose+reverse — much easier to get an index wrong deriving it from scratch live.
- In Spiral Matrix, forgetting to re-check boundaries between each of the four directions — a non-square matrix will otherwise cause you to revisit or skip cells.
- In Set Matrix Zeroes, overwriting the first row/column marker space *before* recording whether it originally had a zero — order of operations matters here.
- In Pow(x, n), forgetting the negative-exponent case, or off-by-one when `n` is odd (need an extra multiplication by `x` beyond the squared half).
- Treating Happy Number as "just track values in a set" when the interview follow-up ("can you do it in O(1) space?") expects the cycle-detection reframing.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Rotate Image](rotate_image.py) | transpose + reverse rows, in place |
| [Spiral Matrix](spiral_matrix.py) | four shrinking boundaries, walk in order |
| [Set Matrix Zeroes](set_matrix_zeroes.py) | reuse first row/column as O(1)-space markers |
| [Happy Number](happy_number.py) | fast/slow pointer cycle detection on the digit-square sequence |
| [Plus One](plus_one.py) | right-to-left carry propagation, handle all-9s growth case |
| [Pow(x, n)](pow_x_n.py) | fast exponentiation by halving the exponent |
