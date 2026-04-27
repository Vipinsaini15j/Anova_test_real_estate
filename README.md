# ANOVA Analysis on Real Estate Data
##  Project Overview

This project performs statistical analysis on real estate data across multiple Indian cities to determine whether **property prices differ significantly based on location and property characteristics**.

The entire analysis is implemented **from scratch without using statistical libraries**, demonstrating a deep understanding of statistical concepts such as variance decomposition and hypothesis testing.

---
##Objectives

- Determine whether **property prices differ across cities**
- Analyze the impact of:
  - City
  - Property Type
- Implement statistical methods manually without using libraries like scipy or statsmodels

---

##Dataset

The dataset includes housing data from:

- Mumbai  
- Hyderabad  
- Kolkata  
- Gurgaon  

### Features Used:
- `PRICE_PER_UNIT_AREA`  
- `BEDROOM_NUM`  
- `PROPERTY_TYPE`  
- `CITY`  

---
##Methodology
### 🔹 One-Way ANOVA
Used to test whether the mean property prices differ across cities.
### 🔹 Two-Way ANOVA
Used to evaluate the combined effect of:
- City
- Property Type

on property prices.

---
## Mathematical Foundation

### One-Way ANOVA

Total Variation:


```
SST = Σ(xᵢⱼ - x̄)²
```

Between-Group Variation:
```
SSB = Σ nⱼ (x̄ⱼ - x̄)²
```

Within-Group Variation:
```
SSW = Σ (xᵢⱼ - x̄ⱼ)²
```

F-statistic:
```
F = MSB / MSW
```

##  Key Results

- Property prices **differ significantly across cities**
- City has a **strong impact on pricing**
- Property type also influences price variation

---
##Visualizations

- Boxplots showing price distribution across cities  
- Mean comparison plots  

---
##Key Insights

- Location is a major determinant of real estate pricing  
- Different cities exhibit distinct pricing trends  
- Multiple factors contribute to housing price variation  

---
##Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---
##Special Highlights

✔ Implemented ANOVA from scratch  
✔ No use of statistical libraries  
✔ Manual computation of:
- Sum of Squares  
- F-statistic  
- p-value (numerical approximation)  

---
## How to Run

1. Clone the repository:
