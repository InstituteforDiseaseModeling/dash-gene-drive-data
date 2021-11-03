import glob
import pandas as pd

for file in glob.glob("*.feather"):
    df = pd.read_feather(file)
    df.to_csv(file.replace(".csv", ".feather"))