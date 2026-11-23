
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
folder = project_dir / "data"

expected_lengths = {
    "SARS_CoV_2_Spike.fasta": 1273,
    "SARS_CoV_Spike.fasta": 1255,
    "MERS_CoV_Spike.fasta": 1353
}

valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

for filename, expected_length in expected_lengths.items():
    file_path = folder / filename

    lines = file_path.read_text().splitlines()
    headers = [line for line in lines if line.startswith(">")]

    sequence = "".join(
        line.strip()
        for line in lines
        if not line.startswith(">")
    ).replace(" ", "").upper()

    invalid = set(sequence) - valid_amino_acids

    print(f"\nFile: {filename}")
    print(f"Header: {headers[0] if headers else 'MISSING'}")
    print(f"Actual length: {len(sequence)}")
    print(f"Expected length: {expected_length}")
    print(f"Invalid characters: {invalid}")
    print(f"Length correct: {len(sequence) == expected_length}")
    print(f"Sequence valid: {len(sequence) > 0 and not invalid}")
