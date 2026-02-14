import pandas as pd

tsv_file = "data/chr4_200bp_bins.tsv"
bed_file = "data/chr4_regions.bed"

# Load TSV
df = pd.read_csv(tsv_file, sep="\t")

# Add index starting from 0
df["idx"] = range(len(df))

# Create a descriptive name for FASTA headers later
df["name"] = (
    df["idx"].astype(str) + "|" +
    df["chr"] + ":" +
    df["start"].astype(str) + "-" +
    df["end"].astype(str) +
    "|ATAC=" + df["ATAC"] +
    "|CTCF=" + df["CTCF"] +
    "|REST=" + df["REST"] +
    "|EP300=" + df["EP300"]
)

# Write BED file (no header)
df[["chr", "start", "end", "name"]].to_csv(
    bed_file,
    sep="\t",
    header=False,
    index=False
)

print("BED file created:", bed_file)

