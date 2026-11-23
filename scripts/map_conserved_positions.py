from pathlib import Path

# Load the alignment file
project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "alignment" / "Spike_Protein_MSA.aln"

sequences = {}

with file_path.open("r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 2 and parts[0].startswith("YP_"):
            accession = parts[0]
            sequences[accession] = sequences.get(accession, "") + parts[1]

# Define sequence order
accessions = [
    "YP_009724390.1",  # SARS-CoV-2
    "YP_009825051.1",  # SARS-CoV
    "YP_009047204.1"   # MERS-CoV
]

names = ["SARS-CoV-2", "SARS-CoV", "MERS-CoV"]

# Check that all sequences exist
for accession in accessions:
    if accession not in sequences:
        raise ValueError(f"Missing sequence: {accession}")

aligned = [sequences[acc] for acc in accessions]

# Conserved regions identified in the previous analysis
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

# Convert alignment positions to original protein positions
for start, end in regions:
    print(f"\nAlignment region: {start}-{end}")

    for name, sequence in zip(names, aligned):
        residue_count = 0
        original_positions = []

        for i, amino_acid in enumerate(sequence, start=1):
            if amino_acid != "-":
                residue_count += 1

            if start <= i <= end and amino_acid != "-":
                original_positions.append(residue_count)

        if original_positions:
            print(
                f"{name}: "
                f"{original_positions[0]}-{original_positions[-1]}"
            )
        else:
            print(f"{name}: No residues (gap)")