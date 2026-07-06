# Stack

## Core idea

A stack is the right tool whenever the most recent unresolved thing needs to be resolved first — nested structure (parentheses), or "the next element that breaks a pattern relative to what came before" (next greater/smaller element style problems). The key insight for the harder problems here: a stack can maintain a **monotonic** (always increasing or always decreasing) sequence of candidates, popping off ones that are no longer useful once a new element arrives.

**Recognition signal:** nested/matching structure (brackets), or "find the next/previous element that is greater/smaller," or needing O(1) access to a running minimum/maximum alongside normal push/pop.

## Key structures & idioms

- **Matching/nesting (Valid Parentheses)**: push opening brackets; on a closing bracket, check the top of the stack matches its pair — if not, or the stack is empty, it's invalid. Valid only if the stack is empty at the end.
  ```python
  pairs = {')': '(', ']': '[', '}': '{'}
  stack = []
  for ch in s:
      if ch in pairs:
          if not stack or stack.pop() != pairs[ch]:
              return False
      else:
          stack.append(ch)
  return not stack
  ```
- **Min Stack**: maintain a second stack alongside the main one, tracking the running minimum *at each depth* — push `min(new_value, current_min)` onto the min-stack every time you push onto the main stack, so popping automatically "restores" the previous minimum. Trades O(n) extra space for O(1) `getMin()`.
- **Monotonic stack (Largest Rectangle in Histogram)**: keep a stack of indices with **increasing** bar heights. When a new bar is shorter than the stack's top, that means the top bar's rectangle can't extend any further right — pop it and compute its max rectangle using the current index as the right boundary and the new stack top as the left boundary. Each bar is pushed and popped at most once, giving O(n) despite the nested-looking logic.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Valid Parentheses (stack) | O(n) | O(n) | Any nested/matching structure |
| Min Stack (auxiliary stack) | O(1) per operation | O(n) | Need running min/max alongside stack ops |
| Brute-force histogram (check every pair of bars) | O(n²) | O(1) | Baseline |
| Monotonic stack histogram | O(n) — each index pushed/popped once | O(n) | Next-greater/smaller-element style problems |

## Common pitfalls

- Forgetting to check the stack is **empty** at the end (Valid Parentheses) — unmatched opening brackets with no closers slip through if you only check mismatches.
- In Min Stack, pushing only the new value onto the min-stack instead of `min(new_value, current_min)` — breaks the "pop restores previous min" property.
- In monotonic-stack problems, forgetting that when you pop, the *new* top of the stack (after popping) is the left boundary — not the element you just popped.
- Not draining the remaining stack after the main loop ends (histogram problems still have bars left on the stack that need their rectangles computed against the end of the array).

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Valid Parentheses](valid_parentheses.py) | push openers, match on closers, stack empty at end |
| [Min Stack](min_stack.py) | auxiliary stack tracking running min at each depth |
| [Largest Rectangle in Histogram](largest_rectangle_in_histogram.py) | monotonic increasing stack of indices |
