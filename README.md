# Quantum-Hackathon-CDAC


The Problem statement falls under Combinatorial optimization problems, and am naming it as Backpacker Traveller problem (BTP) which is inspired from the famous Travelling Salesman Problem (TSP). A small brief intro of Combinatorial problems is finding an optimal or close to optimal solution among a finite collection of possibilities. The problem statement consists of gathering the data of few famous temples, church and Mosques that are in India in various states and create an optimized way for a backpacker to travel to each religious, the problem is to find the shortest possible route such that a backpacker visits every religious places exactly once and returns to the starting point. A path that visits every religious place once is known as Hamiltonian path and if the backpacker returns to his/her starting point then it is known as Hamiltonian cycle.

By considering the problem and the data we will be adding some constraints such as: 

•	Each religious place should be visited exactly once.
•	Only a single religious place is visited at each time point.

We will also introduce cost function to the problem statement.  This problem statement falls under  NP-hard problem in combinatorial optimization. ” many heuristics and exact algorithms are known, so that some instances with tens of thousands of nodes can be solved completely and even problems with millions of nodes can be approximated within a small fraction of 1%” – wiki. But for education purpose and complexity we will be using the Annealing simulator or the Quantum Approximate Optimization Algorithm (QAOA) to obtain the optimized solutions for the backpacker traveller problem.

Leaving things to open for future to develop further by adding more temples and constraints.

References: 
https://en.wikipedia.org/wiki/Travelling_salesman_problem
QWorld / QResearch / QIntern2021 / 12_Educational material development for quantum annealing · GitLab 
