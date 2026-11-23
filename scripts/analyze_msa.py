
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent

project_dir = Path(__file__).resolve().parent.parent

file_path = project_dir / "alignment" / "Spike_Protein_MSA.aln"


sequences = {}

with file_path.open("r") as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 2 and parts[0].startswith("YP_"):
            accession = parts[0]
            sequences[accession] = (
                sequences.get(accession, "") + parts[1]
            )

sars2 = sequences["YP_009724390.1"]
sars = sequences["YP_009825051.1"]
mers = sequences["YP_009047204.1"]

assert len(sars2) == len(sars) == len(mers)

columns = list(zip(sars2, sars, mers))
total = len(columns)

complete = [
    col for col in columns
    if all(aa != "-" for aa in col)
]

three_way_identical = sum(
    a == b == c for a, b, c in complete
)

pair_comparable = [
    (a, b) for a, b, c in columns
    if a != "-" and b != "-"
]

pair_identical = sum(
    a == b for a, b in pair_comparable
)

gap_columns = sum("-" in col for col in columns)

print("Total alignment columns:", total)
print("Columns without gaps:", len(complete))
print("Three-way identical positions:", three_way_identical)
print("Three-way identity among complete columns (%):",
      round(three_way_identical / len(complete) * 100, 2))
print("Three-way identity across all columns (%):",
      round(three_way_identical / total * 100, 2))
print("SARS pair comparable positions:", len(pair_comparable))
print("SARS pair identical positions:", pair_identical)
print("SARS pair identity (%):",
      round(pair_identical / len(pair_comparable) * 100, 2))
print("Columns containing gaps:", gap_columns)
