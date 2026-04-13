# Bayesian Network Project (Causal Analysis)

## 📌 Overview
This project demonstrates how to use a Bayesian Network to model relationships between student behaviors and academic performance.

We focus on:
- Probabilistic inference
- Conditional relationships
- Causal reasoning via intervention (do-operator)

---

## 📊 Dataset
Student Performance Dataset (`student-mat.csv`)

Selected variables:
- traveltime
- studytime
- absences
- failures
- Dalc (alcohol consumption)
- health
- G3 (final grade)

---

## 🧠 Model Structure

We manually define the DAG:

traveltime → studytime  
traveltime → absences  
studytime → G3  
absences → G3  
failures → G3  
Dalc → health → G3  

---

## 🔧 Methodology

### 1. Preprocessing
- Discretize absences and G3
- Convert all variables to categorical

### 2. Model
- Bayesian Network (pgmpy)
- Maximum Likelihood Estimation

### 3. Inference
- Query conditional probabilities:
  P(G3 | evidence)

### 4. Causal Analysis
- Perform intervention:
  P(G3 | do(X))

---

## 🔍 Key Findings

- Studytime has a strong positive relationship with final grade
- Absences and failures negatively impact performance
- Alcohol consumption shows weak effect due to indirect modeling

---

## ⚠️ Important Insight

Observed probabilities and causal effects were very similar:

P(G3 | studytime) ≈ P(G3 | do(studytime))

This suggests limited confounding in the current DAG.

---

## 🚧 Limitations

- DAG is manually defined
- Some important variables are omitted
- Results depend on model assumptions

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
