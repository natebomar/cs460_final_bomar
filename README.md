# The Torchbearer

**Student Name:** ___________________________
**Student ID:** ___________________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  -The shortest path from S to T alone will likely not hit every relic room. The inclusion of the relic rooms, and the fact that cheaper paths between them may not consist of only relics, makes a shortest-path run insufficient.

- **What decision remains after all inter-location costs are known:**
 -The path taken between all relic rooms and to the exit remains to be decided.

- **Why this requires a search over orders (one sentence):**
-Because a simple shortest path is insufficient, we must take a best-so-far approach over the different valid paths that meet the criteria above.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| spawn | must be a source to the node picked next for djikstra's|
| relics | Because each relic node must be reached before exiting, we need to launch Djikstra's from each one to get the costs between. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Other Nodes in the graph |
| What the values represent | Total minimum distance to corresponding key(node) |
| Lookup time complexity | O(n) is worst case, Average O(1) |
| Why O(1) lookup is possible | Dictionaries store keys with a hash map, which has average complexity O(1). |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1(each relic and spawn)
- **Cost per run:** O(mlog(n))
- **Total complexity:** O(k*mlog(n))
- **Justification (one line):** We run djikstra's on each relic to know the cost between each one and the exit.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  The cost displayed is the minimum cost from S to that node

- **For nodes not yet finalized (not in S):**
  The cost displayed is infinite as the minimum cost from S has not yet been determined

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  S only holds the cost of 0 for itself, as the cost from S to itself is known to be 0
  All other minima unknown, so their costs are infinite.

- **Maintenance : why finalizing the min-dist node is always correct:**
 Because there are no negative edge weights, the current minimum node cannot be reached in a different way that doesn't cost more
 Taking another path means starting from a higher weight, so the end result must be greater

- **Termination : what the invariant guarantees when the algorithm ends:**
At termination, all node costs will be minimal, with unreachable nodes having an infinite cost.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

We want to go between relic rooms and to the exit while incurring the lowest penalty
Having shortest paths between spawn, relic rooms, and exits will help us determine this best path.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
