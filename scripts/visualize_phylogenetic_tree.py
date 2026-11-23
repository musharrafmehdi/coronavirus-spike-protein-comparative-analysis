from pathlib import Path
import matplotlib.pyplot as plt
from Bio import Phylo

project_dir = Path(__file__).resolve().parent.parent

tree_file = project_dir / "results" / "Spike_Protein_NJ_Tree_Corrected.nwk"
tree = Phylo.read(tree_file, "newick")

# Replace accession numbers with readable virus names
names = {
    "YP_009047204.1": "MERS-CoV",
    "YP_009724390.1": "SARS-CoV-2",
    "YP_009825051.1": "SARS-CoV"
}

for terminal in tree.get_terminals():
    terminal.name = names.get(terminal.name, terminal.name)

# Remove internal node labels
for clade in tree.get_nonterminals():
    clade.name = None

fig = plt.figure(figsize=(11, 6))
ax = fig.add_subplot(1, 1, 1)

Phylo.draw(tree, axes=ax, do_show=False)
ax.set_ylabel("")
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xlabel("Evolutionary distance", fontsize=11)
ax.set_title(
    "Neighbor-Joining Tree of Coronavirus Spike Proteins",
    fontsize=13,
    pad=15
)

plt.tight_layout()

output_file = project_dir / "results" / "Spike_Protein_NJ_Tree_Corrected.png"

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()

print("Corrected phylogenetic tree saved at:", output_file)
