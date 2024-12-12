# Design of Experiments and Bayesian Statistics Lecture Summary

## Design of Experiments
- Focused on understanding how to structure experiments to gain valid and reliable insights.
- Key components:
  - Factorial designs and randomized trials.
  - Statistical power and replication.
  - Handling variability and confounding factors.

## Bayesian Statistics
### Introduction
- Bayesian framework interprets probabilities as a measure of belief.
- Incorporates prior knowledge and updates beliefs based on observed data.

### Key Concepts
1. **Bayes' Rule**
   \[
   P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
   \]
   - Posterior ∝ Likelihood × Prior.

2. **A Bayesian Coin with Discrete Alternatives**
   - Fair vs. two-headed coin example illustrates how prior affects posterior probability.

3. **MLE and Credibility Regions**
   - Maximum Likelihood Estimation (MLE) estimates parameters by maximizing likelihood.
   - Credibility regions represent intervals where the parameter lies with high probability.

4. **Bias and Importance of the Prior**
   - Influence of informative vs. uninformative priors.
   - Priors can heavily impact posterior when data is scarce.

5. **Extension to Complex Models**
   - Examples include Bayesian Linear Regression:
     - Adds regularization via priors (e.g., Ridge, LASSO).
   - Logistic Regression:
     - Links Bayesian concepts to classification problems.

### Model Selection
- Comparison metrics:
  - **AIC (Akaike Information Criterion):** Penalizes complexity, balances fit.
  - **BIC (Bayesian Information Criterion):** Stronger penalty for model complexity, favors simpler models with sufficient fit.

### Bayesian Linear Regression and Regularization
- Incorporates priors for coefficients:
  - Ridge (L2 regularization).
  - LASSO (L1 regularization).

### Bayesian Sampling Techniques
1. **Gibbs Sampling:** Updates each parameter dimension sequentially.
2. **Metropolis-Hastings:** Uses proposal distributions to sample from the posterior.
3. **Hamiltonian Monte Carlo (HMC):** Combines deterministic optimization and MCMC.
