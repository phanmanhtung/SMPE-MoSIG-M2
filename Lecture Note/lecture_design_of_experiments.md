
# Notes: Design of Experiments

---

## **Key Concepts**
1. **Replication**: Repeating experiments to increase reliability.
2. **Randomization**: Mixing up experiment conditions to reduce bias.
   - Well-designed experiments are essential; even great statistics can't save flawed experiments.

---

## **Steps to Design Experiments**
1. **Select the Problem**:
   - Define the system, phenomenon, and type of study (e.g., descriptive, predictive).
2. **Identify Response Variables**:
   - The system is a "black box" with:
     - **Controllable variables** (e.g., settings, parameters).
     - **Uncontrollable variables** (e.g., environment, human interference).
3. **Choose Relevant Factors**:
   - Examples:
     - Controllable: Algorithm type, platform size.
     - Uncontrollable: Temperature, noise.

---

## **Types of Study Designs**
1. **Factorial Studies**:
   - Test all combinations of factors.
   - Detect interactions between factors.
   - **2-Level Factorial Designs**:
     - Use two levels per factor (e.g., low/high).
     - Good for simple problems.
   - **Fractional Factorial Designs**:
     - Reduce the number of combinations.
     - Useful when many factors exist.

2. **Screening Designs (e.g., Plackett-Burman)**:
   - Focus on identifying key factors quickly.
   - Less precise but saves time and cost.

3. **Full Factorial Designs**:
   - Explore all combinations of multiple levels for each factor.
   - Good for small designs but grows rapidly with more levels/factors.

---

## **Analyzing Models**
1. **Linear Regression**:
   - Equation: \( Y = a + bX + \epsilon \)
     - \( Y \): Response, \( X \): Input, \( \epsilon \): Noise.
   - Prefer simple linear models for initial understanding.
2. **Parsimony** (Occam’s Razor):
   - Use the simplest model that explains the data.
   - Remove unnecessary factors.

3. **Improving Models**:
   - Add data where variability is high.
   - Use advanced designs like Latin Hypercube or D-optimal for better coverage.

---

## **Sequential Approach**
1. Start simple: Test basic hypotheses with minimal parameters.
2. Refine: Add complexity only when necessary.
3. Iterate: Adjust based on results and variability.

---

## **Final Tips**
- Reproducibility matters: Use tools like R and document experiments clearly.
- Statistical analysis helps refine, but the design is crucial.
- Have fun while experimenting and learning! 😊

---