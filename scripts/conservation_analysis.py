from pathlib import Path

# 1. Load the multiple sequence alignment file
project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "alignment" / "Spike_Protein_MSA.aln"

sequences = {}

with file_path.open("r") as file:
    for line in file:
        parts = line.split()

        if len(parts) >= 2 and parts[0].startswith("YP_"):
            accession = parts[0]
            sequences[accession] = sequences.get(accession, "") + parts[1]

# 2. Check that all three sequences were loaded
if len(sequences) != 3:
    raise ValueError(f"Expected 3 sequences, but found {len(sequences)}")

# 3. Check that all aligned sequences have equal length
lengths = {len(sequence) for sequence in sequences.values()}

if len(lengths) != 1:
    raise ValueError("The aligned sequences do not have equal lengths.")

# 4. Arrange sequences in a fixed order
accessions = [
    "YP_009724390.1",  # SARS-CoV-2
    "YP_009825051.1",  # SARS-CoV
    "YP_009047204.1"   # MERS-CoV
]

for accession in accessions:
    if accession not in sequences:
        raise ValueError(f"Missing sequence: {accession}")

seq1, seq2, seq3 = [sequences[acc] for acc in accessions]

# 5. Classify every alignment position
fully_conserved = []
partially_conserved = []
all_different = []
gap_containing = []

for i in range(len(seq1)):
    residues = [seq1[i], seq2[i], seq3[i]]
    position = i + 1

    if "-" in residues:
        gap_containing.append(position)

    elif residues[0] == residues[1] == residues[2]:
        fully_conserved.append(position)

    elif len(set(residues)) == 2:
        partially_conserved.append(position)

    else:
        all_different.append(position)

# 6. Display the results
total = len(seq1)

print("CONSERVATION ANALYSIS")
print("---------------------")
print("Total alignment positions:", total)
print("Fully conserved positions:", len(fully_conserved))
print("Partially conserved positions:", len(partially_conserved))
print("All-different positions:", len(all_different))
print("Gap-containing positions:", len(gap_containing))

print("\nPERCENTAGES")
print("-----------")
print(f"Fully conserved: {len(fully_conserved) / total * 100:.2f}%")
print(f"Partially conserved: {len(partially_conserved) / total * 100:.2f}%")
print(f"All different: {len(all_different) / total * 100:.2f}%")
print(f"Gap-containing: {len(gap_containing) / total * 100:.2f}%")

# 7. Display fully conserved alignment positions
print("\nFULLY CONSERVED ALIGNMENT POSITIONS")
print("----------------------------------")
print(fully_conserved)

# 8. Identify continuous fully conserved regions
regions = []

if fully_conserved:
    start = previous = fully_conserved[0]

    for position in fully_conserved[1:]:
        if position == previous + 1:
            previous = position
        else:
            regions.append((start, previous))
            start = previous = position

    regions.append((start, previous))

print("\nCONTINUOUS FULLY CONSERVED REGIONS")
print("---------------------------------")

for start, end in regions:
    if end - start + 1 >= 5:
        print(f"Alignment positions {start}-{end} (length: {end - start + 1})")