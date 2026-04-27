# 📊 ANOVA & MANOVA Analysis on Real Estate Data (From Scratch)

## 🚀 Project Overview

This project performs statistical analysis on real estate data across multiple cities to determine whether **property prices differ significantly based on location and property characteristics**.

The entire analysis is implemented **from scratch without using statistical libraries**, showcasing a deep understanding of statistical concepts.

---

## 🎯 Objectives

- Analyze whether **property prices differ across cities**
- Evaluate the impact of **city and property type**
- Perform **multivariate analysis** using MANOVA
- Build statistical models manually

---

## 🏙️ Dataset

The dataset includes housing data from:

- Mumbai  
- Hyderabad  
- Kolkata  
- Gurgaon  

### Features Used:
- PRICE_PER_UNIT_AREA  
- BEDROOM_NUM  
- PROPERTY_TYPE  
- CITY  

---

## 🧠 Methods Used

### 🔹 One-Way ANOVA
- Tests whether price differs across cities  

### 🔹 Two-Way ANOVA
- Tests effect of:
  - City
  - Property Type  

### 🔹 MANOVA
- Multivariate analysis using:
  - Price
  - Bedrooms  
- Implemented using **Wilks’ Lambda**

---

## 🧮 Mathematical Foundation

### ANOVA:

F-statistic:

F = MSB / MSW

Where:

- MSB = Between-group variance  
- MSW = Within-group variance  

---

### MANOVA:

Wilks’ Lambda:

Λ = |W| / |T|

Where:

- W = Within-group matrix  
- T = Total matrix  

---

## 📊 Key Results

- Significant differences found across cities  
- City is a major factor influencing price  
- Property type also contributes to variation  
- Multivariate analysis confirms structural differences  

---

## 📈 Visualizations

- Boxplots for price distribution  
- Mean comparison plots  

---

## 🧠 Key Insights

- Location plays a critical role in real estate pricing  
- Different cities exhibit distinct pricing patterns  
- Multivariate relationships exist between price and property features  

---

## 💻 Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## ⚠️ Special Highlight

✔ Implemented **ANOVA & MANOVA from scratch**  
✔ No use of statistical libraries like scipy or statsmodels  
✔ Manual computation of:
- F-statistic  
- p-value (numerical integration)  
- Covariance matrices  

---

## 📁 How to Run

1. Clone the repository:
# Anova_test_real_estate
