
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from pathlib import Path

# Path to the multiple sequence alignment
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "alignment" / "Spike_Protein_MSA.aln"

# Read the Clustal alignment
alignment = AlignIO.read(file_path, "clustal")

records = list(alignment)
names = [record.id for record in records]

print("PHYLOGENETIC ANALYSIS")
print("=====================")

print("Number of sequences:", len(records))
print("Alignment length:", alignment.get_alignment_length())

# Calculate distances using only comparable amino acid positions

# Calculate distances using only comparable amino acid positions
matrix = []

print("\nPAIRWISE COMPARABLE POSITIONS")
print("============================")

for i in range(len(records)):
    row = []

    for j in range(i + 1):
        if i == j:
            row.append(0.0)
        else:
            seq1 = str(records[i].seq)
            seq2 = str(records[j].seq)

            comparable = [
                (a, b)
                for a, b in zip(seq1, seq2)
                if a != "-" and b != "-"
            ]

            identical = sum(a == b for a, b in comparable)
            distance = 1 - (identical / len(comparable))

            row.append(distance)

            print(
                names[i], "vs", names[j],
                "| Comparable:", len(comparable),
                "| Identical:", identical,
                "| Distance:", round(distance, 6)
            )

    matrix.append(row)


# Create corrected distance matrix
distance_matrix = DistanceMatrix(names, matrix)

print("\nCORRECTED EVOLUTIONARY DISTANCE MATRIX")
print("=====================================")
print(distance_matrix)

# Construct Neighbor-Joining tree
constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)

print("\nCORRECTED NEIGHBOR-JOINING TREE")
print("================================")
Phylo.draw_ascii(tree)

# Save corrected tree separately
output_file = project_dir / "results" / "Spike_Protein_NJ_Tree_Corrected.nwk"

Phylo.write(tree, str(output_file), "newick")

print("\nCorrected tree saved at:", output_file)
