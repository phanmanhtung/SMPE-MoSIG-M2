
# Lecture Summary: Challenger Risk Analysis

## Context of the Challenger Disaster
- **Background**: The space shuttle Challenger exploded 73 seconds after launch on January 28, 1986, due to O-ring failure in its booster rockets.
- **Main Cause**: The O-rings, designed to seal parts of the booster, failed due to unusually cold temperatures (just below 0°C). This issue had been previously discussed but not adequately addressed.
- **Significance**: This event is a case study in various fields like risk analysis, data visualization, and decision-making under pressure.

## Statistical Analysis Approach
1. **Temperature’s Role**:
   - Previous flights had higher temperatures (minimum 7-10°C warmer).
   - Statistical analysis focused on assessing how temperature and pressure influenced O-ring failure probabilities.
2. **Steps of Analysis**:
   - **Data Inspection**: Initial plots to visualize potential correlations.
   - **Logistic Regression**:
     - Used to model binary outcomes (e.g., O-ring success/failure).
     - Formula: \( P[\text{Failure}] = \frac{e^{\alpha \cdot T + \beta}}{1 + e^{\alpha \cdot T + \beta}} \).
   - The logistic model ensures probabilities remain between 0 and 1, unlike simple linear models.

## Key Takeaways
- **Visualization**: Graphs help to see relationships and risks that raw numbers might obscure.
- **Statistical Models**: Proper models (e.g., logistic regression) are critical for accurate predictions, especially for binary outcomes.
- **Lessons from History**: Decision-making processes and communication failures were as crucial as the technical data in leading to the disaster.
