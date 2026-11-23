from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
folder = project_dir / "data"

files = [
    "SARS_CoV_2_Spike.fasta",
    "SARS_CoV_Spike.fasta",
    "MERS_CoV_Spike.fasta"
]

output = folder / "All_Spike_Sequences.fasta"

with output.open("w", encoding="utf-8") as outfile:
    for filename in files:
        sequence_file = folder / filename
        outfile.write(sequence_file.read_text(encoding="utf-8").strip() + "\n")

print(f"Combined FASTA created: {output}")