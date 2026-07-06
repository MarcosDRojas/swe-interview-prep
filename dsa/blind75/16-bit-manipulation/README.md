# Bit Manipulation

## Core idea

A small set of bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) let you do certain tasks in O(1) per bit / O(log n) overall with no extra space, where an array/hashmap approach would use O(n) space. The core lesson: know what each operator isolates or clears, and know XOR's self-cancelling property (`x ^ x = 0`, `x ^ 0 = x`) — it comes up constantly.

**Recognition signal:** the problem talks about bits directly, or asks for something "without extra space" / "in O(1) space" over integers, or involves finding a single unique/missing value among duplicates.

## Key structures & idioms

- **Check/set/clear a bit:**
  ```python
  bit = (n >> i) & 1        # read bit i
  n |= (1 << i)             # set bit i
  n &= ~(1 << i)            # clear bit i
  ```
- **`n & (n - 1)` clears the lowest set bit** — this single trick underlies both Number of 1 Bits (count how many times you can do this before hitting 0) and a fast approach to Counting Bits (`bits[n] = bits[n & (n - 1)] + 1`, reusing previously computed answers instead of recounting from scratch each time — a DP-flavored reuse of subproblems, same spirit as [12. Dynamic Programming](../12-dynamic-programming/README.md)).
- **XOR cancels duplicates (Missing Number, and useful generally)**: `a ^ a = 0` and `a ^ 0 = a`, and XOR is commutative/associative, so XOR-ing a full range together with the given array cancels every value that appears in both, leaving only the missing (or the single unique) one. Avoids needing a hash set or sum-formula approach, and sidesteps integer-overflow concerns other languages would have with a sum-based approach.
- **Reverse Bits**: build the result one bit at a time — shift the result left, OR in the lowest bit of the input, then shift the input right; repeat 32 times. Same "process one bit, shift, repeat" shape as the isolate/set/clear idioms above.
- **Sum of Two Integers (no `+`/`-` allowed)**: XOR gives the sum of two bits **ignoring carry**; AND (then shifted left one) gives **just the carry**. Repeat — add the no-carry sum to the carry — until the carry becomes 0. This is literally how hardware adders work at the bit level, worth being able to say out loud.

## Complexity cheat sheet

| Problem | Naive | Bit-trick approach |
|---|---|---|
| Number of 1 Bits | O(32) check every bit position | O(number of set bits) via `n & (n-1)` |
| Counting Bits | O(n log n) — popcount each number independently | O(n) via `bits[i] = bits[i & (i-1)] + 1` |
| Reverse Bits | — | O(32), fixed regardless of value |
| Missing Number | O(n) with a hash set, O(n) extra space | O(n) time, O(1) space via XOR (or sum formula, watch overflow in other languages) |
| Sum of Two Integers | — (can't use `+`) | O(32) bounded loop of XOR/AND/shift until carry is 0 |

All of these are technically O(1) in practice since they're bounded by a fixed bit-width (32/64), but describe them as "O(number of bits)" in an interview to show you understand *why* it's bounded, not just that it happens to be fast.

## Common pitfalls

- Forgetting Python integers are arbitrary-precision (no fixed 32-bit wraparound) — problems like Reverse Bits or Sum of Two Integers that assume 32-bit overflow behavior need an explicit mask (`& 0xFFFFFFFF`) and sign-correction step in Python that other languages get for free.
- Off-by-one in bit position math (`1 << i` vs `1 << (i - 1)`) — verify against a concrete small example (e.g. bit 0 of the value 5).
- Reaching for a hash set for Missing Number/duplicate-finding problems when the XOR (or sum-formula) trick gives O(1) space — mention both, since the interviewer often follows up with "can you do it without extra space?"
- In Sum of Two Integers, forgetting the loop terminates only when carry is exactly 0 — not when it looks "small."

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Number of 1 Bits](number_of_1_bits.py) | `n & (n - 1)` clears the lowest set bit, count iterations |
| [Counting Bits](counting_bits.py) | `bits[i] = bits[i & (i-1)] + 1`, reuse smaller subproblems |
| [Reverse Bits](reverse_bits.py) | build result bit-by-bit via shift + OR |
| [Missing Number](missing_number.py) | XOR cancels all present values, leaving the missing one |
| [Sum of Two Integers](sum_of_two_integers.py) | XOR = sum without carry, AND<<1 = carry, repeat until carry is 0 |
