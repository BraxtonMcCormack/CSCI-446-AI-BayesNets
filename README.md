# Comparative Analysis of Exact and Approximate Inference in Bayesian Networks

## Authors: 
Ben Heinze and Braxton McCormack, Group 8

## Project Overview:
This project explores the relative strengths and limitations of two key inference algorithms used in Bayesian Networks—Variable Elimination and Gibbs Sampling. The focus is on their efficiency and accuracy, particularly in the context of a reactive agent. The project compares both methods across different network scales and evidence conditions to determine which is better suited for various scenarios.

## Key Components:
- **Variable Elimination**: An exact inference algorithm known for accuracy but with high computational cost.
- **Gibbs Sampling**: A Markov Chain Monte Carlo method used for approximate inference, known for its speed but with potential accuracy trade-offs.
  
## Problem Statement:
The project aims to identify which algorithm—Variable Elimination or Gibbs Sampling—provides better performance in terms of accuracy and computational efficiency for Bayesian Networks, especially when considering evidence and a reactive agent.

## Hypothesis:
Variable Elimination is expected to offer higher accuracy, while Gibbs Sampling is hypothesized to be more efficient, though potentially less reliable. The introduction of a reactive agent might improve Variable Elimination's performance by mitigating its computational overhead.

## Methodology:
- The algorithms were tested across five different Bayesian networks using data from the Bayesian Network Repository.
- Gibbs Sampling was run with 60,000 iterations and a burn-in period of 5,000.
- Results from both algorithms were compared under various levels of evidence (no evidence, little evidence, and moderate evidence).

## Key Results:
- **Alarm Network**: Gibbs Sampling demonstrated much faster execution times but often differed significantly in probability distribution compared to Variable Elimination.
- **Child Network**: Both algorithms produced fairly consistent results, but Gibbs Sampling occasionally failed to estimate probabilities for certain variables.
- **Hailfinder Network**: Moderate differences were found, with Gibbs Sampling showing more variability in results.
- **Insurance Network**: Gibbs Sampling struggled without evidence, while Variable Elimination produced balanced distributions across states.
- **Win95pts Network**: Both methods encountered challenges with binary outcomes, leading to deterministic results (1.0 or 0.0) for some variables.

## Conclusion:
- **Variable Elimination** provides accurate results, but its high computational cost makes it less suitable for large networks.
- **Gibbs Sampling** is faster and less resource-intensive, making it preferable for larger networks, though its accuracy can sometimes be inconsistent.
- The choice between these algorithms should depend on the size of the network and the computational resources available, with Variable Elimination being favored for smaller, accuracy-critical networks and Gibbs Sampling for larger, efficiency-focused tasks.

## References:
- Pearl, Judea. *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*. Morgan Kaufmann, 1988.
- BNRepository. [BNLearn Repository](http://www.bnlearn.com/bnrepository/), Accessed April 2023.
