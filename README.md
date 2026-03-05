1. Turing Test Simulation
Description

This program simulates a simplified version of the Turing Test.
A judge asks questions, and responses may come from either a human or a machine. The judge must guess whether the response is from a human or a machine.

Features

Simulates multiple rounds of questioning

Randomly selects a human or machine responder

Tracks the judge’s correct guesses

Displays final evaluation result

Technologies Used

Python

random module

How It Works

The judge asks a question.

The system randomly selects whether a human or machine will answer.

The response is displayed to the judge.

The judge guesses the identity of the responder.

The system records whether the guess is correct.

2. CAPTCHA Verification System
Description

This program generates a random CAPTCHA string and asks the user to enter it correctly.
It helps demonstrate how systems verify whether a user is human.

Features

Generates random alphanumeric CAPTCHA

Verifies user input

Grants or denies access based on correctness

Technologies Used

Python

random module

string module

How It Works

The system generates a random CAPTCHA code.

The code is displayed to the user.

The user enters the CAPTCHA.

The program compares the input with the generated code.

3. Depth First Search (DFS)
Description

Depth First Search is a graph traversal algorithm that explores nodes by going as deep as possible before backtracking.

Features

Uses a stack-based traversal

Tracks visited nodes

Stops when the goal node is found

How It Works

Start from the initial node.

Push the node onto a stack.

Pop nodes and visit them.

Add unvisited neighbors to the stack.

Continue until the goal node is reached.

4. Depth Limited Search (DLS)
Description

Depth Limited Search is a variation of DFS where the search depth is restricted to a fixed limit.

Features

Prevents infinite search

Uses recursion

Searches nodes only within the specified depth

How It Works

Start at the initial node.

If the node is the goal, return success.

If the depth limit is reached, stop searching.

Otherwise, recursively explore child nodes.

5. Iterative Deepening Depth First Search (IDDFS)
Description

Iterative Deepening combines the advantages of DFS and BFS.
It repeatedly applies Depth Limited Search with increasing depth limits.

Features

Gradually increases search depth

Uses repeated depth-limited searches

Efficient for large search spaces

How It Works

Set depth limit to 0.

Perform Depth Limited Search.

If goal not found, increase depth limit.

Repeat until the goal is found or the maximum depth is reached.

6. AI Tic-Tac-Toe Game
Description

This program implements a simple Tic-Tac-Toe game where a human plays against a computer-controlled opponent.

Features

Human vs AI gameplay

Board display after each move

Win and draw detection

How It Works

The human player enters a position on the board.

The AI selects an available position.

The board updates after each move.

The program checks for a winner or draw.

Requirements

Python 3.x

Basic command line environment

How to Run

Install Python on your system.

Save the program files with .py extension.

Open terminal or command prompt.

Run the program using:

python filename.py

Example:

python dfs.py

7. Breadth First Search (BFS)
Description

Breadth First Search (BFS) is a graph traversal algorithm that explores nodes level by level.
It first visits all nodes at the current depth before moving to the next level. BFS is commonly used to find the shortest path in an unweighted graph.

Features

Traverses nodes level by level

Uses a queue data structure

Ensures the shortest path in unweighted graphs

Visits each node only once

Technologies Used

Python

collections.deque for queue implementation

How It Works

Start from the initial node.

Insert the starting node into a queue.

Remove a node from the front of the queue.

Visit the node and mark it as visited.

Add all unvisited neighboring nodes to the queue.

Continue the process until the goal node is found or the queue becomes empty.

Example Use Cases

Shortest path finding in networks

Web crawling

Social network analysis

AI state space search

Expected Output

The algorithm prints the order in which nodes are visited and stops when the goal node is found.
