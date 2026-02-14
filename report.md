# Project Audit Log: Mortality Risk Estimator
## 1. Project Overview
**Project Name:** Mortality Risk Estimator CLI
**Author:** Luke Wardle
**Date:** 14/02/2026
**Week:** 1 - Tuesday Code Session
**Objective:**
Demonstrate practical application of linear algebra (dot product) through a command-line tool that calculates mortality risk scores from patient feature vectors and model weight vectors.
**Mathematical Foundation:**
The tool implements the linear model: risk_score = w^T · x, where:
- w is the weight vector (learned model parameters)
- x is the feature vector (patient characteristics)
- · represents the dot product operation
---
## 2. Environment Setup
**Python Version:** 3.11.2 
**NumPy Version:** 1.24.3 
**Operating System:** Windows
**Virtual Environment:** Active (.venv)
---
## 3. Execution Details
### Command Executed
```bash
python src/cli.py --vector "75,120,80,1" --weights "0.02,0.5,0.1,5"
```
### Input Specification
**Patient Feature Vector (x):**
- Raw Input: `"75,120,80,1"`
- Parsed Array: `[75.0, 120.0, 80.0, 1.0]`
- Dimensions: (4,)
**Feature Interpretation:**
- x₁ = 75.0 (age in years)
- x₂ = 120.0 (systolic blood pressure in mmHg)
- x₃ = 80.0 (diastolic blood pressure in mmHg)
- x₄ = 1.0 (smoker status: 1=yes, 0=no)
**Model Weight Vector (w):**
- Raw Input: `"0.02,0.5,0.1,5"`
- Parsed Array: `[0.02, 0.5, 0.1, 5.0]`
- Dimensions: (4,)
---
## 4. Calculation Results
### Primary Output: Risk Score
**Calculated Risk Score:** 74.5000
### Manual Verification
The dot product calculation:
```
risk_score = w · x
           = (0.02 × 75) + (0.5 × 120) + (0.1 × 80) + (5 × 1)
           = 1.5 + 60.0 + 8.0 + 5.0
           = 74.5 ✓
```
### Supporting Metrics
**Feature Vector Magnitude:**
||x|| = √(75² + 120² + 80² + 1²) = √24,826 ≈ 162.5608
**Weight Vector Magnitude:**
||w|| = √(0.02² + 0.5² + 0.1² + 5²) = √25.5104 ≈ 5.0260
---
## 5. Code Quality Metrics
### Project Structure
```
mortality-risk-estimator/
├── .venv/              # Virtual environment (ignored)
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
├── report.md           # This audit log
├── requirements.txt    # Dependencies
└── src/
    ├── cli.py          # Command-line interface
    ├── io_parser.py    # Input parsing utilities
    └── math_ops.py     # Mathematical operations
```
### Modular Design
- **Separation of Concerns:** I/O, logic, and presentation separated into distinct modules
- **Type Hints:** All functions use type annotations
- **Docstrings:** Google-style docstrings with Args, Returns, Raises, Examples
- **Error Handling:** Comprehensive validation and informative error messages
---
## 6. Interpretation & Analysis
### Clinical Context
This example patient has:
- **Age:** 75 years (elderly, higher baseline risk)
- **Blood Pressure:** 120/80 mmHg (normal)
- **Smoking Status:** Active smoker (major risk factor)
The resulting risk score of 74.5 reflects the compounded effect of age and smoking status, despite normal blood pressure.
### Weight Analysis
The model weights reveal feature importance:
- **Smoking (w=5.0):** Strongest predictor, adding 5 points per smoker
- **Systolic BP (w=0.5):** Moderate importance, contributes 60 points at 120 mmHg
- **Diastolic BP (w=0.1):** Minor contribution
- **Age (w=0.02):** Small per-year increase
---
## 7. Validation & Testing
### Dimension Mismatch Test
**Command:**
```bash
python src/cli.py --vector "75,120" --weights "0.02,0.5,0.1"
```
**Result:** ✓ Correctly caught and reported dimension mismatch
### Invalid Input Test
**Command:**
```bash
python src/cli.py --vector "75,abc,80,1" --weights "0.02,0.5,0.1,5"
```
**Result:** ✓ Correctly caught and reported non-numeric input
---
## 8. Reflection
### Technical Achievements
1. Successfully implemented string-to-NumPy array parsing with robust error handling
2. Demonstrated dot product calculation as a practical linear algebra operation
3. Built a modular, testable codebase following professional Python standards
4. Created comprehensive documentation with type hints and docstrings
### Key Learnings
- The dot product translates abstract linear algebra into concrete risk calculations
- Modular design makes code easier to test, maintain, and extend
- Comprehensive error handling is critical for production tools
- Documentation and audit logs ensure reproducibility and accountability
### Future Extensions
Potential enhancements for this tool:
1. Batch processing: Calculate risk for multiple patients from CSV file
2. Confidence intervals: Add uncertainty quantification to risk scores
3. Visualization: Generate plots of risk distributions
4. Model training: Learn weights from historical patient outcome data
---
## 9. Sign-off
**Report Completed:** 14/02/2026
**Verified By:** Luke Wardle
**Status:** ✓ All calculations verified and documented
