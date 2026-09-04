import pandas as pd

# ===== LOAD =====
df = pd.read_csv("Superstore.csv", encoding="latin1")

# ===== CLEAN =====
# 1. Convert dates from text to real dates
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# 2. Remove duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows")

# 3. Create useful new columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Profit Margin %"] = (df["Profit"] / df["Sales"] * 100).round(2)

# ===== QUICK INSIGHTS =====
print("\n=== DATE RANGE ===")
print(f"{df['Order Date'].min().date()} to {df['Order Date'].max().date()}")

print("\n=== SALES BY REGION ===")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).round(0))

print("\n=== SALES BY CATEGORY ===")
print(df.groupby("Category")["Sales"].sum().round(0))

print("\n=== TOP 5 SUB-CATEGORIES BY PROFIT ===")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).head().round(0))

print("\n=== WORST 5 SUB-CATEGORIES BY PROFIT ===")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values().head().round(0))

# Save cleaned data for our dashboard
df.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned data saved as cleaned_data.csv")
