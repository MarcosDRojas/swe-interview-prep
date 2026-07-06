# Trie (Prefix Tree)

## Core idea

When you need fast **prefix**-based lookups over a set of strings (does any word start with "ap"?), a hash set of whole words can't help — it only answers "is this exact string present." A trie shares common prefixes across words in a tree structure, so prefix checks cost O(length of prefix), independent of how many words are stored.

**Recognition signal:** the problem is about a dictionary of words and asks about prefixes, autocomplete-style search, or wildcard search over words — not just membership of a single exact string.

## Key structures & idioms

- **Node shape**: each node is a map from character → child node, plus a boolean "is this the end of a complete word":
  ```python
  class TrieNode:
      def __init__(self):
          self.children = {}
          self.is_end = False
  ```
- **Insert**: walk the trie one character at a time, creating child nodes as needed; mark `is_end = True` at the last character.
- **Search (exact word)**: walk the trie by characters; fail if any character is missing; succeed only if you land on a node with `is_end = True`.
- **StartsWith (prefix)**: same walk as search, but succeed as soon as you can walk the whole prefix — `is_end` doesn't matter.
- **Wildcard search (`.` matches any character)**: when you hit a wildcard, branch into *all* children at that position (DFS/backtracking over the trie) instead of following a single path.
- **Word Search II (grid + trie)**: build a trie from the whole word list once, then DFS the grid; the trie tells you in O(1) per step whether continuing the current path could still complete *some* dictionary word, letting you prune dead-end paths early instead of checking each word against the grid independently.

## Complexity cheat sheet

| Approach | Time | Space | When |
|---|---|---|---|
| Hash set of whole words | O(1) avg for exact match | O(total chars) | Only need exact-word membership, not prefixes |
| Trie | O(L) per insert/search/prefix-check, L = word/prefix length | O(total chars across all inserted words, with sharing) | Prefix queries, wildcard search, or search-with-pruning over a word list |
| Word Search II (trie + grid DFS) | O(rows × cols × 4^L) worst case, pruned heavily in practice by the trie | O(total chars in dictionary) | Multiple words to find simultaneously in a grid |

## Common pitfalls

- Using a plain dict without an explicit `is_end` marker — then "cat" being inserted makes `search("ca")` ambiguously look like it exists, when it should only pass `startsWith("ca")`.
- In wildcard search, forgetting that `.` must try **every** child, not just the first match — this needs backtracking/DFS, not a simple loop.
- In Word Search II, not pruning the DFS using the trie (e.g. stopping if `char not in node.children`) — this is what keeps the search fast; skipping it degrades to checking every word against every grid position independently.
- Rebuilding the trie from scratch per query instead of once up front, when the word list is fixed across many queries.

## Problems in this folder

| Problem | Pattern signal |
|---|---|
| [Implement Trie (Prefix Tree)](implement_trie_prefix_tree.py) | core insert/search/startsWith trie operations |
| [Design Add and Search Words Data Structure](design_add_and_search_words_data_structure.py) | trie + DFS backtracking for `.` wildcards |
| [Word Search II](word_search_ii.py) | trie built from word list + grid DFS pruned by the trie |
