from pathlib import Path

# Load the multiple sequence alignment
project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "alignment" / "Spike_Protein_MSA.aln"


sequences = {}

with file_path.open("r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 2 and parts[0].startswith("YP_"):
            accession = parts[0]
            sequences[accession] = sequences.get(accession, "") + parts[1]

# Define the three proteins
proteins = {
    "SARS-CoV-2": "YP_009724390.1",
    "SARS-CoV": "YP_009825051.1",
    "MERS-CoV": "YP_009047204.1"
}

# Conserved regions from our previous analysis
regions = [
    (817, 821),
    (925, 930),
    (955, 962),
    (969, 973),
    (1064, 1068),
    (1079, 1083),
    (1101, 1106),
    (1330, 1334),
    (1336, 1343)
]

# Verify that all proteins were loaded
for name, accession in proteins.items():
    if accession not in sequences:
        raise ValueError(f"Missing sequence for {name}")

print("CONSERVED REGION SEQUENCES")
print("==========================")

# Extract amino-acid sequences using alignment coordinates
for start, end in regions:
    print(f"\nAlignment region: {start}-{end}")

    for name, accession in proteins.items():
        sequence = sequences[accession]

        # Python uses zero-based indexing
        extracted = sequence[start - 1:end]

        # Remove alignment gaps for the original protein sequence
        extracted = extracted.replace("-", "")

        print(f"{name}: {extracted}")