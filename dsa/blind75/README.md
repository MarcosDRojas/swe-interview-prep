# Blind 75

Checklist of the classic Blind 75 problems, grouped by category/technique. Check items off as you solve them.

Note: a few problems test more than one technique and are listed under multiple categories below, but only have one stub file (in their canonical category) to avoid duplicates — see the "(see ...)" pointers.

## How to use this folder

- **Don't just start editing a stub file.** Run the `/practice` skill — it reads [PROGRESS.md](PROGRESS.md) to pick up exactly where you left off, runs the session like a real interview (clarify → brute force → hints only on request), and updates your progress automatically. It will not hand you a full solution unless you explicitly ask for it.
- **Read the category README before attempting its problems.** Each category folder (e.g. [01-array-and-hashing/README.md](01-array-and-hashing/README.md)) explains the underlying pattern, gives a complexity cheat sheet, and lists common pitfalls — this is concept knowledge, not spoilers for specific problems.
- **For deeper "why does this work" questions**, ask to bring in the `dsa-algo-expert` subagent — it specializes in teaching the general technique without solving your current problem for you.
- [PROGRESS.md](PROGRESS.md) is the single source of truth for what's solved, what's in progress, and what's queued next. See also: [data-structures-review.md](../data-structures-review.md) for a standalone refresher on core data structures and their Big-O, independent of any specific problem.

## Running a problem

Every stub is a real, standalone LeetCode problem — pulled from LeetCode itself, not paraphrased — and doubles as its own test runner:

```
python3 dsa/blind75/01-array-and-hashing/two_sum.py
```

Each file has three parts:

1. **A docstring** with the real problem statement, examples, constraints, LeetCode link, and a time/space complexity target to aim for.
2. **The function (or class) stub** — write your solution directly in place of `pass`.
3. **A built-in test runner** (`test_<name>()`, called automatically when you run the file) that checks your solution against several real LeetCode examples and prints `[PASS]`/`[FAIL]` per case.

No pytest, no imports between files, no setup — `python3 <file>.py` is the whole workflow. Re-run it after every change.

The 3 LeetCode-Premium problems ([13-graphs](13-graphs/README.md): Graph Valid Tree, Number of Connected Components, Alien Dictionary) have hand-written descriptions since their official pages aren't public — noted in each docstring.

## 01. Array & Hashing ([concept overview](01-array-and-hashing/README.md))
- [ ] [Two Sum](01-array-and-hashing/two_sum.py)
- [ ] [Contains Duplicate](01-array-and-hashing/contains_duplicate.py)
- [ ] [Valid Anagram](01-array-and-hashing/valid_anagram.py)
- [ ] [Product of Array Except Self](01-array-and-hashing/product_of_array_except_self.py)
- [ ] [Maximum Subarray](01-array-and-hashing/maximum_subarray.py)
- [ ] [Maximum Product Subarray](01-array-and-hashing/maximum_product_subarray.py)
- [ ] Find Minimum in Rotated Sorted Array (see [04. Binary Search](../blind75/04-binary-search/find_minimum_in_rotated_sorted_array.py))
- [ ] Search in Rotated Sorted Array (see [04. Binary Search](../blind75/04-binary-search/search_in_rotated_sorted_array.py))
- [ ] 3Sum (see [02. Two Pointers](02-two-pointers/three_sum.py))
- [ ] Container With Most Water (see [02. Two Pointers](02-two-pointers/container_with_most_water.py))

## 02. Two Pointers ([concept overview](02-two-pointers/README.md))
- [ ] [Valid Palindrome](02-two-pointers/valid_palindrome.py)
- [ ] [3Sum](02-two-pointers/three_sum.py)
- [ ] [Container With Most Water](02-two-pointers/container_with_most_water.py)

## 03. Sliding Window ([concept overview](03-sliding-window/README.md))
- [ ] [Longest Substring Without Repeating Characters](03-sliding-window/longest_substring_without_repeating_characters.py)
- [ ] [Longest Repeating Character Replacement](03-sliding-window/longest_repeating_character_replacement.py)
- [ ] [Minimum Window Substring](03-sliding-window/minimum_window_substring.py)
- [ ] [Best Time to Buy and Sell Stock](03-sliding-window/best_time_to_buy_and_sell_stock.py)

## 04. Binary Search ([concept overview](04-binary-search/README.md))
- [ ] [Find Minimum in Rotated Sorted Array](04-binary-search/find_minimum_in_rotated_sorted_array.py)
- [ ] [Search in Rotated Sorted Array](04-binary-search/search_in_rotated_sorted_array.py)

## 05. Linked List ([concept overview](05-linked-list/README.md))
- [ ] [Reverse Linked List](05-linked-list/reverse_linked_list.py)
- [ ] [Linked List Cycle](05-linked-list/linked_list_cycle.py)
- [ ] [Merge Two Sorted Lists](05-linked-list/merge_two_sorted_lists.py)
- [ ] Merge k Sorted Lists (see [08. Heap / Priority Queue](08-heap-priority-queue/merge_k_sorted_lists.py))
- [ ] [Remove Nth Node From End of List](05-linked-list/remove_nth_node_from_end_of_list.py)
- [ ] [Reorder List](05-linked-list/reorder_list.py)

## 06. Trees ([concept overview](06-trees/README.md))
- [ ] [Invert Binary Tree](06-trees/invert_binary_tree.py)
- [ ] [Maximum Depth of Binary Tree](06-trees/maximum_depth_of_binary_tree.py)
- [ ] [Same Tree](06-trees/same_tree.py)
- [ ] [Subtree of Another Tree](06-trees/subtree_of_another_tree.py)
- [ ] [Lowest Common Ancestor of a Binary Search Tree](06-trees/lowest_common_ancestor_of_a_binary_search_tree.py)
- [ ] [Binary Tree Level Order Traversal](06-trees/binary_tree_level_order_traversal.py)
- [ ] [Validate Binary Search Tree](06-trees/validate_binary_search_tree.py)
- [ ] [Kth Smallest Element in a BST](06-trees/kth_smallest_element_in_a_bst.py)
- [ ] [Construct Binary Tree from Preorder and Inorder Traversal](06-trees/construct_binary_tree_from_preorder_and_inorder_traversal.py)
- [ ] [Binary Tree Maximum Path Sum](06-trees/binary_tree_maximum_path_sum.py)
- [ ] [Serialize and Deserialize Binary Tree](06-trees/serialize_and_deserialize_binary_tree.py)

## 07. Trie ([concept overview](07-trie/README.md))
- [ ] [Implement Trie (Prefix Tree)](07-trie/implement_trie_prefix_tree.py)
- [ ] [Design Add and Search Words Data Structure](07-trie/design_add_and_search_words_data_structure.py)
- [ ] [Word Search II](07-trie/word_search_ii.py)

## 08. Heap / Priority Queue ([concept overview](08-heap-priority-queue/README.md))
- [ ] [Find Median from Data Stream](08-heap-priority-queue/find_median_from_data_stream.py)
- [ ] [Top K Frequent Elements](08-heap-priority-queue/top_k_frequent_elements.py)
- [ ] [Merge k Sorted Lists](08-heap-priority-queue/merge_k_sorted_lists.py)

## 09. Backtracking ([concept overview](09-backtracking/README.md))
- [ ] [Subsets](09-backtracking/subsets.py)
- [ ] [Combination Sum](09-backtracking/combination_sum.py)
- [ ] [Word Search](09-backtracking/word_search.py)

## 10. Intervals ([concept overview](10-intervals/README.md))
- [ ] [Insert Interval](10-intervals/insert_interval.py)
- [ ] [Merge Intervals](10-intervals/merge_intervals.py)
- [ ] [Non-overlapping Intervals](10-intervals/non_overlapping_intervals.py)

## 11. Stack ([concept overview](11-stack/README.md))
- [ ] [Valid Parentheses](11-stack/valid_parentheses.py)
- [ ] [Min Stack](11-stack/min_stack.py)
- [ ] [Largest Rectangle in Histogram](11-stack/largest_rectangle_in_histogram.py)

## 12. Dynamic Programming ([concept overview](12-dynamic-programming/README.md))
- [ ] [Climbing Stairs](12-dynamic-programming/climbing_stairs.py)
- [ ] [Coin Change](12-dynamic-programming/coin_change.py)
- [ ] [Longest Increasing Subsequence](12-dynamic-programming/longest_increasing_subsequence.py)
- [ ] [Longest Common Subsequence](12-dynamic-programming/longest_common_subsequence.py)
- [ ] [Word Break](12-dynamic-programming/word_break.py)
- [ ] [Combination Sum IV](12-dynamic-programming/combination_sum_iv.py)
- [ ] [House Robber](12-dynamic-programming/house_robber.py)
- [ ] [House Robber II](12-dynamic-programming/house_robber_ii.py)
- [ ] [Decode Ways](12-dynamic-programming/decode_ways.py)
- [ ] [Unique Paths](12-dynamic-programming/unique_paths.py)
- [ ] [Jump Game](12-dynamic-programming/jump_game.py)

## 13. Graphs ([concept overview](13-graphs/README.md))
- [ ] [Number of Islands](13-graphs/number_of_islands.py)
- [ ] [Clone Graph](13-graphs/clone_graph.py)
- [ ] [Pacific Atlantic Water Flow](13-graphs/pacific_atlantic_water_flow.py)
- [ ] [Course Schedule](13-graphs/course_schedule.py)
- [ ] [Course Schedule II](13-graphs/course_schedule_ii.py)
- [ ] [Graph Valid Tree](13-graphs/graph_valid_tree.py)
- [ ] [Number of Connected Components in an Undirected Graph](13-graphs/number_of_connected_components_in_an_undirected_graph.py)
- [ ] [Alien Dictionary](13-graphs/alien_dictionary.py)

## 14. Advanced Graphs ([concept overview](14-advanced-graphs/README.md))
- [ ] [Reconstruct Itinerary](14-advanced-graphs/reconstruct_itinerary.py)
- [ ] [Min Cost to Connect All Points](14-advanced-graphs/min_cost_to_connect_all_points.py)
- [ ] [Network Delay Time](14-advanced-graphs/network_delay_time.py)

## 15. Geometry & Math ([concept overview](15-geometry-and-math/README.md))
- [ ] [Rotate Image](15-geometry-and-math/rotate_image.py)
- [ ] [Spiral Matrix](15-geometry-and-math/spiral_matrix.py)
- [ ] [Set Matrix Zeroes](15-geometry-and-math/set_matrix_zeroes.py)
- [ ] [Happy Number](15-geometry-and-math/happy_number.py)
- [ ] [Plus One](15-geometry-and-math/plus_one.py)
- [ ] [Pow(x, n)](15-geometry-and-math/pow_x_n.py)

## 16. Bit Manipulation ([concept overview](16-bit-manipulation/README.md))
- [ ] [Number of 1 Bits](16-bit-manipulation/number_of_1_bits.py)
- [ ] [Counting Bits](16-bit-manipulation/counting_bits.py)
- [ ] [Reverse Bits](16-bit-manipulation/reverse_bits.py)
- [ ] [Missing Number](16-bit-manipulation/missing_number.py)
- [ ] [Sum of Two Integers](16-bit-manipulation/sum_of_two_integers.py)
