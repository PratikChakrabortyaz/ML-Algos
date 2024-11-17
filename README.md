# ML-Algos

This repository, **ML-Algos**, contains implementations of various Machine Learning algorithms from scratch. The goal is to provide a comprehensive collection of ML techniques coded in Python without relying on external libraries for model implementation. 
## Table of Contents

1. [Introduction](#introduction)
2. [Algorithms](#algorithms)
3. [Getting Started](#getting-started)

---

## Introduction

This repository has some essential basic ML algos from scratch using libraries like numpy and matplotlib

---

## Algorithms

### Linear Regression
- **Simple Linear Regression (SLR)**:
    - Using Pedhazur's approach
    - Matrix-based implementation
    - Gradient Descent
- **Multiple Linear Regression (MLR)**:
    - Matrix-based implementation
    - Gradient Descent

### Polynomial Regression
- Implemented using matrix methods for fitting non-linear data.

### Logistic Regression
- Logistic Regression with Gradient Descent for binary classification.

### Naive Bayes
- Multi-feature and class prediction.
- Text classification for NLP tasks.

### K-Nearest Neighbors (KNN)
- Implementation of KNN for classification with:
    - Euclidean, Manhattan, and Minkowski distances.
    - Decision boundary visualizations.

### Decision Trees
- **ID3 Algorithm**:
    - Uses entropy and information gain.
- **CART (Classification and Regression Trees)**:
    - Supports both Gini impurity and regression tasks.
- **C4.5**:
    - Extends ID3 with support for continuous attributes.

### Clustering
- **K-Means Clustering**:
    - Includes the Elbow method to determine the best value of `k`.
- **Hierarchical Clustering**:
    - Single-linkage implementation.

### Support Vector Machines (SVM)
- Basic implementation of SVM for binary classification.

---

## Getting Started

To get started, clone the repository:
```bash
git clone https://github.com/your-username/ML-Algos.git
cd ML-Algos```
### Install Dependencies

This project requires the following libraries:

- **NumPy**: For numerical operations.
- **Pandas**: For handling datasets and dataframes.
- **Matplotlib**: For visualizations.

All dependencies are listed in the `requirements.txt` file. You can install them by running:
```bash
pip install -r requirements.txt


