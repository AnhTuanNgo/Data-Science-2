import pandas as pd

df = pd.read_csv("chipotle.tsv", sep="\t")
# df.head(5)
print(df.info)
