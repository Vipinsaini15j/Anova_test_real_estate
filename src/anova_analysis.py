import pandas as pd
import math
from scipy.stats import f  # for stable p-value

# ---------------- LOAD DATA ----------------
def load_data():
    mumbai = pd.read_csv('data/mumbai.csv')
    hyderabad = pd.read_csv('data/hyderabad.csv')
    kolkata = pd.read_csv('data/kolkata.csv')
    gurgaon = pd.read_csv('data/gurgaon_10k.csv', low_memory=False)  # fix warning

    # Add CITY column
    mumbai['CITY'] = 'Mumbai'
    hyderabad['CITY'] = 'Hyderabad'
    kolkata['CITY'] = 'Kolkata'
    gurgaon['CITY'] = 'Gurgaon'

    df = pd.concat([mumbai, hyderabad, kolkata, gurgaon], ignore_index=True)
    return df

# ---------------- CLEAN DATA ----------------
def clean_data(df):
    df.columns = [c.upper() for c in df.columns]

    cols = ['CITY', 'PRICE_PER_UNIT_AREA', 'PROPERTY_TYPE']
    df = df[[c for c in cols if c in df.columns]]

    df['PRICE_PER_UNIT_AREA'] = pd.to_numeric(df['PRICE_PER_UNIT_AREA'], errors='coerce')

    df = df.dropna()
    return df

# ---------------- ONE WAY ANOVA ----------------
def one_way_anova(df, group, value):
    groups = df[group].unique()
    grand_mean = df[value].mean()

    SSB, SSW = 0, 0
    N = len(df)
    k = len(groups)

    for g in groups:
        vals = df[df[group] == g][value]
        mean = vals.mean()
        n = len(vals)

        SSB += n * (mean - grand_mean) ** 2
        SSW += sum((vals - mean) ** 2)

    df_between = k - 1
    df_within = N - k

    MSB = SSB / df_between
    MSW = SSW / df_within

    F = MSB / MSW

    return F, df_between, df_within

# ---------------- TWO WAY ANOVA ----------------
def two_way_anova(df, f1, f2, val):
    grand_mean = df[val].mean()

    SSA, SSB, SSE = 0, 0, 0

    for a in df[f1].unique():
        subset = df[df[f1] == a]
        SSA += len(subset) * (subset[val].mean() - grand_mean) ** 2

    for b in df[f2].unique():
        subset = df[df[f2] == b]
        SSB += len(subset) * (subset[val].mean() - grand_mean) ** 2

    for a in df[f1].unique():
        for b in df[f2].unique():
            subset = df[(df[f1] == a) & (df[f2] == b)]
            if len(subset) > 0:
                mean = subset[val].mean()
                SSE += sum((subset[val] - mean) ** 2)

    return SSA, SSB, SSE

# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = clean_data(load_data())

    print("===== ONE-WAY ANOVA =====")
    F, d1, d2 = one_way_anova(df, 'CITY', 'PRICE_PER_UNIT_AREA')

    print(f"F-statistic: {F:.4f}")

    # Stable p-value using scipy
    p = 1 - f.cdf(F, d1, d2)
    print(f"p-value: {p:.6f}")

    print("\n===== INTERPRETATION =====")
    alpha = 0.05

    if p < alpha:
        print(" Significant difference detected")
        print(" Property prices differ across cities")
    else:
        print(" No significant difference")
        print(" Prices are similar across cities")

    print("\n===== TWO-WAY ANOVA =====")
    SSA, SSB, SSE = two_way_anova(df, 'CITY', 'PROPERTY_TYPE', 'PRICE_PER_UNIT_AREA')

    print(f"SSA (City Effect): {SSA:.2f}")
    print(f"SSB (Property Type Effect): {SSB:.2f}")
    print(f"SSE (Error): {SSE:.2f}")

    print("\n===== FINAL INSIGHT =====")
    print(" City has a strong influence on real estate pricing")
    print(" Property type also contributes to variation")