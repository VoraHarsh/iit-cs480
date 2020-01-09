# Assignment 2


In this programming exercise, you’ll get experience with some of the algorithms discussed in chapter 3. You are provided several files:

* [search.py](search.py) contains the search algorithms and necessary data structures.
  * You need to modify it.
* [problem.py](problem.py) contains the definition of a few problems, such as N-Queens, 8-Puzzle, and Travel.
* [example_test.py](example_test.py) has a few examples on how to run these search algorithms.
* [example_output.txt](example_output.txt) is the output of running example-test.py.
* [run.py](run.py) is a skeleton code for replicating assignment 1.
  * You need to modify it.

Your tasks are:

1. Complete the implementation of `breadth_first_search` in search.py. Hint: There is one-line solution which looks like: return search_type(problem, xxxQueue()).

1. Complete the implementation of `depth_first_search` in search.py. Hint: see the previous question.

1. Complete the implementation of `astar_search` in search.py. Hint: see the implementations of `uniform_cost_search` and `greedy_best_first_search`.

1. Modify run.py so that it replicates Homework 1 solutions, questions 1 through 5. See the example_test.py for examples.

1. After modifying run.py, run `python run.py > out.txt`.

1. Submit your assignment using git add, commit, push commands as needed. Make sure the modified search.py and run.py files and the output file out.txt are added, committed, and pushed to the repo. The other files should remain unchanged and no other files should be added.

1. On Blackboard: submit a link to your github repository.

## Extra Challenge - do not submit

These questions are for your enjoyment only. This is **_not_** extra credit. Do not submit your solutions to these questions.

1. Create the map of Romania (see chapter 3 slides) and try various algorithms, like Breadth-first search, uniform cost search, greedy-best-first search, A* search using tree search and graph search for traveling from Arad to Bucharest. Compare your results with the figures in the slides.

1. Implement the manhattan-distance heuristic for the eight puzzle problem. See if you can replicate the comparison of h1 and h2 in the slides.

1. Generalize the 8-Puzzle problem to NPuzzle problem where (N+1) is a square of an integer. Test your implementation using 3 Puzzle, 8-Puzzle, and 15-Puzzle examples.

1. Solve a problem of interest to you.
