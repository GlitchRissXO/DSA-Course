# Data Structures & Algorithms

### A Complete Course — Foundations Through Advanced Algorithmic Thinking

**Language:** Python 3.11+
**Format:** Self-paced, session-based, project-driven
**Instructor:** Claude
**Student:** Riss

---

## 1. Course Description

This is a full-length course in data structures and algorithms, built the way a strong university sequence is built: theory first, implementation second, analysis third, application fourth. You will not be handed working code to fill blanks into. You will build every major data structure in this course from scratch, in your own editor, and you will be asked to justify every choice you make.

The organizing question of the course is not *"how do I implement a linked list?"* It is *"how do I look at an unfamiliar problem and know what to reach for?"* Every module is built backwards from that question.

By the end you will have implemented roughly twenty data structures and thirty algorithms, shipped fourteen projects, and produced a public GitHub repository that constitutes real evidence of competence.

---

## 2. Prerequisites

You need:

- Comfort writing Python functions, loops, conditionals, and classes
- Ability to install packages and run scripts from a terminal
- Git installed, and a GitHub account

You do **not** need:

- Any prior data structures coursework
- Discrete math or proof experience (we build the math you need as we go)
- Big-O knowledge

**Module 00 verifies the prerequisites and repairs any gaps before we start.**

---

## 3. How This Course Runs

### The workflow

```
Claude teaches  →  You plan  →  You code in your IDE  →  You test
      →  You debug  →  You commit  →  You push  →  We review together
```

I never write your assignment code. I will write demonstration code during lectures, give you skeletons and signatures, review what you submit, and break things on purpose so you can fix them. The code in your repo is yours.

### The session shape

A session is 60–90 minutes and always ends at a committable checkpoint:

| Segment | Time | What happens |
|---|---|---|
| Warm-up recall | 5 min | 2–3 questions from previous modules (spaced repetition) |
| Reading | 10–15 min | Written material with definitions and worked examples |
| Lecture | 10–15 min | Explanation, visualization, Socratic questioning |
| Checkpoint quiz | 5 min | Conceptual, not trivia |
| Build | 20–30 min | You write code |
| Lab or challenge | 10–20 min | Debugging, experiment, or stretch problem |
| Commit | 5 min | Push, with a written note on what you learned |

Every session ends with an explicit line: **"Stopping point: ______."** You never have to guess whether you're done.

### Rules of engagement

1. I ask before I explain. When I ask you something, guess — a wrong guess is more useful to me than "I don't know," because it shows me the shape of your model.
2. You may always ask for a hint. Hints are laddered: nudge → strategy → structure → walkthrough. You choose the rung.
3. If you're stuck for more than 20 minutes on a build, stop and bring it to me. Struggle is productive; grinding is not.
4. Say **"boss me"** if a module feels too easy and I'll escalate difficulty and cut the scaffolding.
5. Say **"slow down"** and I will re-teach from a different angle without reducing the standard.

---

## 4. Progression Map

```
FOUNDATIONS        00 → 02     Setup, Python's object model, complexity
LINEAR STRUCTURES  03 → 06     Arrays, linked lists, stacks/queues, hashing
CORE TECHNIQUES    07 → 09     Recursion, searching, sorting
HIERARCHICAL       10 → 12     Trees, heaps, balanced trees & tries
GRAPHS             13 → 14     Traversal, shortest paths, MSTs, union-find
ALGORITHM DESIGN   15 → 17     Patterns, dynamic programming, advanced topics
CAPSTONE           18          Independent portfolio project
```

Difficulty ramps in three distinct jumps. Module 07 (recursion) is the first real wall. Module 13 (graphs) is the second. Module 16 (dynamic programming) is the third. These are expected and planned for — each is preceded by a module that deliberately builds the prerequisite intuition.

---

## 5. The Modules

### Module 00 — Setup & Ground Rules
**Level 1 · ~1 session**
Repo scaffolding, `.gitignore`, virtual environments, `pytest`, project structure conventions, how to write a commit message that isn't "update."
- **Lab:** Write a failing test, make it pass, commit both.
- **Deliverable:** `DSA-Course` repo, initialized, with a README that states your goal.

---

### Module 01 — Foundations: How Python Actually Stores Things
**Level 1 · ~3 sessions**
Objects vs. names. References, aliasing, mutability, identity vs. equality, shallow vs. deep copy, why `a = b` doesn't copy anything. Problem decomposition and computational thinking. What an algorithm *is*, formally.
- **Lab:** The Aliasing Traps — 8 short programs; predict the output before running, explain every miss.
- **Debugging:** A function that "randomly" corrupts its caller's data (mutable default argument).
- **Project:** **Text Analyzer** — word frequency, longest word, unique word count, reading level. Built with built-ins only, so you have a baseline to compare against later.
- **Boss:** Rewrite the analyzer to make a single pass over the input instead of five. Measure the difference.

---

### Module 02 — Complexity I: Counting, Not Timing
**Level 2 · ~3 sessions**
Counting elementary operations. Big-O, Big-Θ, Big-Ω and why we mostly say O and mostly mean Θ. Best/average/worst case. Dominant terms. Why constants are dropped and when dropping them is a lie.
- **Experiment:** Time six functions at n = 100 … 1,000,000. Plot the curves. Match each curve to its complexity class before I tell you which is which.
- **Lab:** Ten functions, no comments. Derive the complexity of each and justify it in writing.
- **Deliverable:** `02-complexity/ANALYSIS.md` with your plots and your reasoning.
- **Boss:** Given two implementations where the asymptotically *worse* one is faster for all realistic n, explain why, with evidence.

> Complexity returns in every subsequent module. Amortized analysis is deferred to Module 03, where dynamic array resizing makes it concrete rather than abstract.

---

### Module 03 — Arrays, Dynamic Arrays & Strings
**Level 2 · ~4 sessions**
Contiguous memory, indexing as arithmetic, cache locality. Growth factors, amortized O(1) append, why doubling and not +1. String immutability and the quadratic concatenation trap.
- **Build:** `DynamicArray` from scratch on a fixed-size backing store — `append`, `insert`, `pop`, `__getitem__`, automatic resize.
- **Experiment:** Instrument your resize count. Prove amortized O(1) empirically, then derive it.
- **Debugging:** A dynamic array that leaks references after `pop` and never frees memory.
- **Project:** **Shopping Cart** — line items, quantity updates, totals, undo of the last action.
- **Boss:** Implement a growth factor of 1.5 vs 2.0 and argue, with data, which you'd ship.

---

### Module 04 — Linked Lists
**Level 3 · ~4 sessions**
Nodes and pointers. Singly, doubly, circular. Sentinel/dummy nodes and why they eliminate half your edge cases. Head/tail invariants. When a linked list beats a dynamic array and — honestly — how rarely that is in Python.
- **Build:** `SinglyLinkedList` and `DoublyLinkedList`, full interfaces, with tests.
- **Debugging:** Four broken implementations — a lost head, an off-by-one traversal, an insert that drops the tail, a cycle.
- **Project:** **Playlist / Music Queue Manager** — add, remove, move a track, play next, skip, shuffle-insert, jump to track. Doubly linked so you can go back.
- **Boss:** Reverse a list in place, O(1) extra space. Then detect a cycle in O(1) space.
- **Nightmare mode:** Merge two sorted linked lists without allocating a single new node.

---

### Module 05 — Stacks, Queues & Deques
**Level 3 · ~3 sessions**
LIFO and FIFO as *policies*, not structures. Implementing each over both an array and a linked list, and what changes. Circular buffers. Why `collections.deque` exists and what it's actually doing.
- **Build:** `Stack`, `Queue`, `Deque`, `CircularBuffer`.
- **Lab:** Bracket matcher, then infix → postfix conversion, then a postfix evaluator.
- **Project:** **Undo/Redo Engine** — a text buffer with unlimited undo/redo, built on two stacks. Real-world: this is how every editor you use works.
- **Boss:** Implement a queue using only two stacks with amortized O(1) enqueue and dequeue. Prove the amortized bound.

---

### Module 06 — Hashing
**Level 4 · ~4 sessions**
What a hash function is and what makes one good. Uniformity, determinism, avalanche. Collisions are inevitable — pigeonhole. Chaining vs. open addressing (linear probing, quadratic, double hashing). Load factor, resizing, clustering. Why dict lookup is "O(1)" in scare quotes.
- **Build:** `HashMap` from scratch with chaining. Then a second version with open addressing.
- **Experiment:** Plot average probe length against load factor for both. Find the knee.
- **Debugging:** A hash table with a subtly non-uniform hash function — diagnose it from performance data alone.
- **Project:** **Contact Manager** with O(1) lookup, plus a duplicate-detection feature.
- **Boss:** **LRU Cache.** Hash map + doubly linked list, O(1) get and put. This is the module's payoff — it requires Modules 04 and 06 simultaneously and it is a genuinely famous problem.

---

### Module 07 — Recursion *(first difficulty wall)*
**Level 5 · ~5 sessions**
The call stack, drawn by hand until it's boring. Base cases and recursive cases. Recursive data structures. Tracing. Stack depth limits. Recursion vs. iteration and the real cost of each. Then: divide and conquer, backtracking, memoization.
- **Lab:** Hand-trace six recursive functions on paper. Submit photos of your stack diagrams. This is not optional and it is the single highest-value hour in the course.
- **Debugging:** Missing base case, wrong base case, base case that's unreachable, mutation of a shared accumulator.
- **Project:** **Recursive File Organizer** — walk a directory tree, report sizes, find duplicates by content hash, optionally reorganize.
- **Boss:** N-Queens via backtracking. Then instrument it and count the branches you pruned.

---

### Module 08 — Searching
**Level 5 · ~3 sessions**
Linear search and when it's correct to use it. Binary search, and the invariant that makes it work. The four classic binary search variants (first occurrence, last occurrence, insertion point, rotated array). **Binary search on the answer space** — the idea that the thing you're searching isn't always an array.
- **Lab:** Implement binary search four ways. Then find the off-by-one in each of five broken versions.
- **Experiment:** At what n does binary search actually beat linear search, given the cost of sorting first?
- **Boss:** "Find the minimum capacity such that a shipment fits in D days." No array is given. Recognize it as a binary search.

---

### Module 09 — Sorting
**Level 6 · ~5 sessions**
Bubble, selection, insertion, merge, quick, heap, counting, radix. Stability and why it matters in practice. In-place vs. out-of-place. Adaptive sorting. The Ω(n log n) comparison lower bound and how counting/radix dodge it. What Timsort actually does.
- **Build:** All eight, from scratch, with tests.
- **Experiment:** Benchmark on random, sorted, reverse-sorted, and nearly-sorted input. The results will surprise you at least twice.
- **Project:** **Sorting Visualizer** — animate each algorithm's comparisons and swaps. Terminal or matplotlib, your choice.
- **Boss:** Implement quicksort with a pivot strategy that doesn't degrade to O(n²) on sorted input. Justify your choice.

---

### Module 10 — Trees & Binary Search Trees
**Level 6 · ~5 sessions**
Terminology (height, depth, degree, ancestor, subtree). Binary trees. BST invariant. Insert, search, delete — including the three-case delete that everyone gets wrong. Traversals: preorder, inorder, postorder, level-order, both recursively and iteratively. Why inorder on a BST is sorted.
- **Build:** `BinarySearchTree` with all operations and all four traversals.
- **Debugging:** A BST delete that silently corrupts the tree on the two-children case.
- **Project:** **Expression Evaluator** — parse arithmetic into a tree, evaluate it, print it in each traversal order.
- **Boss:** Validate whether an arbitrary binary tree satisfies the BST property. The obvious solution is wrong; find out why.

---

### Module 11 — Heaps & Priority Queues
**Level 6 · ~3 sessions**
The heap property. Array-backed complete binary trees and the index arithmetic that makes them work. Sift up, sift down. Heapify in O(n) — and why it isn't O(n log n). Priority queues as an interface.
- **Build:** `MinHeap` and `MaxHeap` from scratch. Then heapsort using them.
- **Project:** **Task Scheduler** — priority-based job queue with deadlines and dynamic re-prioritization.
- **Boss:** Find the k largest elements in a stream of n items using O(k) memory. Then explain why a heap beats sorting here.

---

### Module 12 — Balanced Trees & Tries
**Level 7 · ~4 sessions**
Why unbalanced BSTs degrade to linked lists. Rotations. AVL trees in full; red-black trees at the level of intuition and invariants (you should understand *why* they work, not memorize the recoloring cases). Tries: prefix trees, and why they beat hash maps for prefix queries.
- **Build:** AVL tree with all four rotation cases. Then a `Trie` with insert, search, `starts_with`, and delete.
- **Experiment:** Insert 10,000 sorted keys into an unbalanced BST and an AVL tree. Compare heights and lookup times.
- **Project:** **Autocomplete System** — trie-backed, ranked by frequency, with typo tolerance as a stretch.
- **Boss:** Implement trie-based wildcard search (`c.t` matches `cat`, `cot`).

---

### Module 13 — Graphs I: Structure & Traversal *(second difficulty wall)*
**Level 7 · ~5 sessions**
Vertices and edges. Directed, undirected, weighted, cyclic, acyclic. Adjacency matrix vs. adjacency list and the density tradeoff. BFS and DFS — iterative and recursive. Connected components. Cycle detection in both directed and undirected graphs. Topological sort.
- **Build:** A `Graph` class supporting both representations, plus BFS, DFS, component labeling, and topological sort.
- **Lab:** Convert five real systems into graphs (a course catalog, a subway map, a package dependency tree, a social network, a maze). Argue your representation choice for each.
- **Project:** **Maze Generator & Solver** — generate with randomized DFS, solve with BFS, visualize both. Watching BFS flood a maze is the moment graphs click for most people.
- **Boss:** Detect whether a course-prerequisite graph is satisfiable, and if so produce a valid schedule.

---

### Module 14 — Graphs II: Weighted Algorithms
**Level 8 · ~5 sessions**
Dijkstra's algorithm and its heap dependency. Why Dijkstra breaks on negative weights, and Bellman-Ford as the fix. Minimum spanning trees: Kruskal and Prim. Union-Find with path compression and union by rank, and the near-constant complexity that results.
- **Build:** Dijkstra, Bellman-Ford, Kruskal, Prim, `UnionFind`.
- **Project:** **Route Planner** — real map data, shortest path by distance and by time, with turn-by-turn output.
- **Boss:** Add A* on top of your Dijkstra implementation. Measure how many nodes the heuristic saves you.
- **Nightmare mode:** Detect arbitrage in a currency exchange graph. (It's a negative cycle. That's the whole hint.)

---

### Module 15 — Algorithmic Techniques
**Level 8 · ~4 sessions**
Two pointers. Sliding window, fixed and variable. Prefix sums and difference arrays. Greedy algorithms — and the exchange argument you use to prove one correct. Backtracking as a general framework.
- **Focus:** Pattern *recognition*, not templates. For each problem I give you, the first question is always "what in the problem statement told you which technique to use?"
- **Lab:** Twenty problems, unlabeled. Classify each by technique before solving any.
- **Boss:** Construct a problem where the greedy solution looks correct and isn't. Prove your counterexample.

---

### Module 16 — Dynamic Programming *(third difficulty wall)*
**Level 9 · ~6 sessions**
Optimal substructure and overlapping subproblems — how to *detect* them. Memoization as recursion plus a cache. Tabulation as memoization turned inside out. State design, which is the actual skill. Space optimization. 1D, 2D, and knapsack-family problems.
- **Method:** Every DP problem in this module is solved four times — brute force, memoized, tabulated, space-optimized — so you see the transformation rather than memorizing the final form.
- **Project:** **Text Diff Tool** — edit distance, with the actual edit script reconstructed from the DP table.
- **Boss:** Design the state for a problem I give you that has no standard name. State design is the whole game.

---

### Module 17 — Advanced Topics
**Level 9 · ~5 sessions**
Selected for genuine value, not résumé decoration:
- **Segment trees & Fenwick trees** — range queries, and the idea of preprocessing for query speed
- **String algorithms** — KMP, Rabin-Karp, and rolling hashes
- **Advanced hashing** — bloom filters, consistent hashing
- **Complexity classes** — P, NP, NP-complete, reductions, what "NP-hard" actually claims
- **Approximation & heuristics** — what you do when optimal is off the table
- **Project:** **Mini Search Engine** — inverted index, TF-IDF ranking, phrase queries. Uses tries, hash maps, heaps, and sorting simultaneously.

---

### Module 18 — Capstone
**Level 10 · ~6–8 sessions**
See Section 9.

---

## 6. Project Ladder

| # | Project | Module | Core structure being learned |
|---|---|---|---|
| 1 | Text Analyzer | 01 | Baseline; built-ins only |
| 2 | Shopping Cart | 03 | Dynamic arrays |
| 3 | Playlist / Music Queue | 04 | Doubly linked lists |
| 4 | Undo/Redo Engine | 05 | Stacks |
| 5 | Contact Manager | 06 | Hash maps |
| 6 | LRU Cache | 06 | Hash map + linked list |
| 7 | Recursive File Organizer | 07 | Recursion, trees in the wild |
| 8 | Sorting Visualizer | 09 | Sorting, comparative analysis |
| 9 | Expression Evaluator | 10 | Binary trees, traversal |
| 10 | Task Scheduler | 11 | Heaps, priority queues |
| 11 | Autocomplete System | 12 | Tries |
| 12 | Maze Generator & Solver | 13 | Graph traversal |
| 13 | Route Planner | 14 | Weighted graphs, Dijkstra |
| 14 | Text Diff Tool | 16 | Dynamic programming |
| 15 | Mini Search Engine | 17 | Everything at once |
| 16 | **Capstone** | 18 | Your choice, your justification |

Every project ships with a `README.md` containing: problem, requirements, design, structures chosen, algorithms used, complexity analysis, tradeoffs considered, testing approach, known limitations, and lessons learned. That document is worth as much as the code to a person reading your GitHub.

---

## 7. Repository Structure

```
DSA-Course/
├── README.md                    # Course overview, progress, what you've built
├── PROGRESS.md                  # XP log, levels, achievements, dates
├── .gitignore
├── requirements.txt
│
├── 00-setup/
├── 01-foundations/
├── 02-complexity/
├── 03-arrays/
├── 04-linked-lists/
├── 05-stacks-queues/
├── 06-hashing/
├── 07-recursion/
├── 08-searching/
├── 09-sorting/
├── 10-trees/
├── 11-heaps/
├── 12-balanced-trees-tries/
├── 13-graphs-traversal/
├── 14-graphs-weighted/
├── 15-techniques/
├── 16-dynamic-programming/
├── 17-advanced/
│
├── projects/                    # One subfolder per project, each a real package
├── labs/
├── challenges/
└── capstone/
```

Each module folder contains:

```
NN-topic/
├── README.md         # Your notes, in your words. Not mine.
├── implementation/   # The structure, built from scratch
├── tests/            # pytest
├── exercises/
├── experiments/      # Benchmarks, plots, data
└── ANALYSIS.md       # Complexity write-up and what surprised you
```

**Git practice, taught progressively:** Module 00 — init, add, commit, push. Module 03 — meaningful commit messages, `.gitignore` discipline. Module 06 — branching per feature. Module 09 — pull requests to yourself, reviewing your own diff. Module 13 — tags for milestones. Capstone — issues, project board, release.

---

## 8. Gamification

**XP is earned for artifacts that exist in your repo**, not for time spent. Nothing is awarded for reading.

| Action | XP |
|---|---|
| Lesson completed + notes committed | 50 |
| Coding exercise passing tests | 75 |
| Lab completed | 100 |
| Debugging exercise solved *and explained* | 125 |
| Experiment with data and write-up | 150 |
| Mini-project shipped with README | 300 |
| Boss challenge defeated | 500 |
| Nightmare mode | 750 |
| Module assessment passed | 250 |
| Capstone | 3000 |

**Levels:** 1 — Initiate (0) · 2 — Apprentice (500) · 3 — Practitioner (1,500) · 4 — Analyst (3,000) · 5 — Engineer (5,000) · 6 — Architect (8,000) · 7 — Algorithmist (12,000) · 8 — Specialist (17,000) · 9 — Master (23,000) · 10 — **Computer Scientist** (30,000)

**Achievements (selected):**
- *First Blood* — first commit pushed
- *The Aliasing Incident* — survive Module 01's traps with a perfect prediction sheet
- *Amortized* — prove O(1) append empirically before being told the answer
- *Pointer Wrangler* — reverse a linked list in place, first try
- *Cache Money* — LRU cache in O(1)
- *Stack Trace* — hand-trace six recursive calls with zero errors
- *Off By None* — implement all four binary search variants without an off-by-one
- *Pivot* — quicksort that survives adversarial input
- *Rotation Station* — all four AVL rotations, correct, unassisted
- *Flood Fill* — watch BFS solve your own maze
- *Shortest Path* — Dijkstra, working, on real map data
- *State of the Art* — design a novel DP state unassisted
- *No Notes* — complete a module assessment without referencing prior work

**Side quests** are optional, always available, and worth XP: implement a structure in a second language, write a blog post explaining a concept, contribute a test case to an open-source project, teach a concept to someone else and report how it went.

---

## 9. Assessment

**Per module:**
- Conceptual assessment — explain, compare, justify. No code.
- Coding assessment — implement under constraints, from scratch.
- Complexity assessment — analyze unfamiliar code and defend your bound.

**Spaced review:** every session opens with 2–3 questions drawn from modules you completed 1, 3, and 8 sessions ago. Retrieval practice is the highest-leverage study technique that exists and it costs us five minutes.

**Mastery bar:** you may not advance from a module until you can implement its core structure from an empty file, with no reference, and correctly state the complexity of every operation. This is strict on purpose. It is the difference between this course and the one you just left.

---

## 10. Capstone

You choose one, or propose your own. All three are deliberately underspecified — deciding what to build is part of the assessment.

**Option A — Personal Search Engine.** Index a corpus (your notes, a docs site, a subreddit). Full-text search with ranking, prefix suggestions, typo tolerance, phrase queries. *Structures: inverted index, trie, heap, TF-IDF.*

**Option B — Transit / Route Optimization System.** Real transit or road data. Multi-criteria shortest path (fastest, fewest transfers, least walking), live re-routing on a closure. *Structures: weighted graph, Dijkstra/A\*, priority queue, spatial index.*

**Option C — Recommendation Engine.** Item or user similarity over a real dataset, with explainable recommendations and a cold-start strategy. *Structures: sparse matrices, graphs, heaps, hashing, similarity search.*

**Required deliverables:**
1. Design document written *before* implementation, committed and dated
2. Working implementation with a test suite
3. Complexity analysis of every major operation
4. Benchmarks at three input scales
5. An optimization pass — profile, find the real bottleneck, fix it, measure
6. Professional README with architecture diagram
7. A written defense: what you built, why these structures, what you'd change

The design document being committed **before** the code is not ceremony. It's the artifact that proves you chose rather than stumbled.

---

## 11. Workload

| Pace | Sessions/week | Duration |
|---|---|---|
| Steady | 3 | ~9 months |
| Committed | 5 | ~5–6 months |
| Intensive | 8+ | ~3–4 months |

Roughly 75 sessions total. Steady is the pace I'd recommend alongside a full course load — the spaced review only works if there's space between sessions for you to forget things and retrieve them.

---

## 12. On Completion, You Will Be Able To

- Implement every core data structure from an empty file, without reference
- Derive time and space complexity for unfamiliar code and defend the bound
- Choose a data structure for a novel problem and justify it against alternatives
- Recognize which algorithmic technique a problem calls for, from the problem statement alone
- Design dynamic programming states independently
- Profile a working program, locate the real bottleneck, and optimize it
- Debug systematically rather than by guessing
- Explain your engineering decisions to another person clearly
- Point to a GitHub repository that demonstrates all of the above

---
