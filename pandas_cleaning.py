import pandas as pd

df = pd.read_csv("Expanded_Dataset.csv")
print("original shape:", df.shape)

print("duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("shape after removing duplicates:", df.shape)

df.loc[df["Market Share (%)"] < 0, "Market Share (%)"] = 0
df.loc[df["5G Subscribers (millions)"] < 0, "5G Subscribers (millions)"] = 0
df.loc[df["Regional 5G Coverage (%)"] > 100, "Regional 5G Coverage (%)"] = 100

df["Period"] = df["Year"].astype(str) + "-" + df["Quarter"]

num_cols = ["Revenue ($)", "Market Share (%)", "Regional 5G Coverage (%)",
            "5G Subscribers (millions)", "Avg 5G Speed (Mbps)", "Preference for 5G (%)"]
df[num_cols] = df[num_cols].round(2)

df.to_csv("Expanded_Dataset_cleaned.csv", index=False)
print("final shape:", df.shape)
