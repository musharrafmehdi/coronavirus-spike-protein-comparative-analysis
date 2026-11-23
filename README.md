# Comparative Sequence Analysis of Coronavirus Spike Proteins

**An In-Silico Comparative Bioinformatics Study**

## 1. Project Overview

This project investigates the sequence similarity, conservation patterns, and evolutionary relationships of the spike proteins of three human coronaviruses:

- SARS-CoV-2
- SARS-CoV
- MERS-CoV

The study uses computational bioinformatics methods to compare protein sequences, identify conserved regions, examine sequence variation, and construct a Neighbor-Joining phylogenetic tree.

## 2. Research Objective

The main objective is to investigate similarities and differences among the spike protein sequences of the three coronaviruses.

Specific objectives:

- Retrieve and validate reference protein sequences.
- Perform multiple sequence alignment (MSA).
- Analyze conserved and variable amino-acid positions.
- Identify conserved regions and map their coordinates.
- Compare protein sequence motifs and domains.
- Calculate pairwise evolutionary distances.
- Construct a Neighbor-Joining phylogenetic tree.

## 3. Reference Protein Sequences

The study uses three NCBI RefSeq protein records.

| Virus | Strain | NCBI Accession | Length |
|---|---|---|---:|
| SARS-CoV-2 | Wuhan-Hu-1 | YP_009724390.1 | 1,273 aa |
| SARS-CoV | Tor2 | YP_009825051.1 | 1,255 aa |
| MERS-CoV | EMC/2012 | YP_009047204.1 | 1,353 aa |

NCBI records:

- [SARS-CoV-2 Spike Protein](https://www.ncbi.nlm.nih.gov/protein/YP_009724390.1)
- [SARS-CoV Spike Protein](https://www.ncbi.nlm.nih.gov/protein/YP_009825051.1)
- [MERS-CoV Spike Protein](https://www.ncbi.nlm.nih.gov/protein/YP_009047204.1)

## 4. Methodology

The project follows a computational analysis workflow:

1. **Sequence Retrieval:** Obtained reference spike protein sequences from NCBI.
2. **Sequence Validation:** Checked FASTA headers, amino-acid sequence lengths, and invalid characters.
3. **BLASTp Analysis:** Compared protein sequences to evaluate local sequence similarity.
4. **Multiple Sequence Alignment:** Used Clustal Omega to align the three spike protein sequences.
5. **Conservation Analysis:** Identified fully conserved, partially conserved, variable, and gap-containing alignment positions.
6. **Conserved Region Mapping:** Mapped conserved alignment coordinates to original protein coordinates.
7. **Motif and Domain Analysis:** Examined conserved sequence motifs and compared relevant protein regions.
8. **Evolutionary Distance Analysis:** Calculated uncorrected p-distances using pairwise deletion of gap-containing positions.
9. **Phylogenetic Analysis:** Constructed a Neighbor-Joining tree using the calculated distance matrix.

## 5. Key Results

### Multiple Sequence Alignment

- Total alignment length: 1,393 positions
- Positions without gaps: 1,215
- Three-way identical positions: 354
- Three-way identity among complete columns: 29.14%
- Three-way identity across all alignment columns: 25.41%
- Gap-containing columns: 178

SARS-CoV-2 and SARS-CoV showed 968 identical positions among 1,251 comparable positions, corresponding to 77.38% identity in the reported pairwise alignment analysis.

### Conservation Analysis

| Conservation Category | Positions | Percentage |
|---|---:|---:|
| Fully conserved | 354 | 25.41% |
| Partially conserved | 663 | 47.60% |
| All different | 198 | 14.21% |
| Gap-containing | 178 | 12.78% |

### Conserved Regions

Nine conserved regions of at least five consecutive alignment positions were identified.

| Alignment Coordinates | Conserved Amino-Acid Sequence |
|---|---|
| 817–821 | IPTNF |
| 925–930 | IEDLLF |
| 955–962 | ARDLICAQ |
| 969–973 | VLPPL |
| 1064–1068 | NAQAL |
| 1079–1083 | FGAIS |
| 1101–1106 | QIDRLI |
| 1330–1334 | KWPWY |
| 1336–1343 | WLGFIAGL |

All nine regions showed identical amino-acid sequences across the three aligned proteins.

### BLASTp Analysis

| Comparison | Identity | Query Coverage |
|---|---:|---:|
| SARS-CoV-2 vs SARS-CoV | 75.96% | 100% |
| SARS-CoV-2 vs MERS-CoV | 35.10% | 79% |
| SARS-CoV vs MERS-CoV | 34.79% | 79% |

These values represent BLASTp local alignment results and should not be confused with the separate global MSA identity calculations.

### Evolutionary Distance Analysis

Uncorrected p-distances were calculated using:

**d = 1 − (Identical Positions / Comparable Positions)**

| Comparison | Comparable Positions | Identical Positions | Distance |
|---|---:|---:|---:|
| SARS-CoV-2 vs SARS-CoV | 1,251 | 968 | 0.226219 |
| SARS-CoV-2 vs MERS-CoV | 1,234 | 394 | 0.680713 |
| SARS-CoV vs MERS-CoV | 1,218 | 393 | 0.677340 |

The smallest pairwise distance was observed between SARS-CoV-2 and SARS-CoV.

### Phylogenetic Analysis

A Neighbor-Joining phylogenetic tree was constructed using the corrected pairwise distance matrix.

The tree shows a closer sequence relationship between SARS-CoV-2 and SARS-CoV than either has with MERS-CoV.

The analysis is based on three protein sequences and does not establish ancestral direction or evolutionary history on its own.

## 6. Repository Structure

```text
01_Sequences/
│
├── alignment/
│   └── Spike_Protein_MSA.aln
│
├── data/
│   ├── SARS_CoV_2_Spike.fasta
│   ├── SARS_CoV_Spike.fasta
│   ├── MERS_CoV_Spike.fasta
│   └── All_Spike_Sequences.fasta
│
├── report/
│   ├── 03_MSA_Conservation_Results.docx
│   ├── 04_Conservation_Analysis_Results.docx
│   ├── 05_Conserved_Region_Mapping.docx
│   ├── 06_Conserved_Motif_Results.docx
│   ├── 07_Motif_Domain_Comparison.docx
│   ├── 08_Evolutionary_Distance_Results.docx
│   ├── 09_Phylogenetic_Tree_Results.docx
│   └── 10_Final_Research_Report.docx
│
├── results/
│   ├── Spike_Protein_NJ_Tree_Corrected.nwk
│   ├── Spike_Protein_NJ_Tree_Corrected.png
│   └── Figure_1.png
│
├── scripts/
│   ├── analyze_conserved_sequences.py
│   ├── analyze_msa.py
│   ├── checkqequence.py
│   ├── combined_sequenced.py
│   ├── conservation_analysis.py
│   ├── map_conserved_positions.py
│   ├── phylogenetic_analysis.py
│   └── visualize_phylogenetic_tree.py
│
├── requirements.txt
└── README.md
```

## 7. Software and Dependencies

- Python 3.11
- Biopython 1.88
- Matplotlib 3.7.1
- Clustal Omega
- NCBI BLASTp

Python dependencies are listed in `requirements.txt`.

### Installation

Clone the repository:

```bash
git clone https://github.com/musharrafmehdi/coronavirus-spike-protein-comparative-analysis.git
```

Move into the project directory:

```bash
cd coronavirus-spike-protein-comparative-analysis
```

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

### Running the Analysis

Run scripts from the project root directory.

Validate the original FASTA sequences:

```bash
python scripts/checkqequence.py
```

Analyze the multiple sequence alignment:

```bash
python scripts/analyze_msa.py
```

Perform conservation analysis:

```bash
python scripts/conservation_analysis.py
```

Map conserved positions:

```bash
python scripts/map_conserved_positions.py
```

Extract conserved sequences:

```bash
python scripts/analyze_conserved_sequences.py
```

Construct the Neighbor-Joining tree:

```bash
python scripts/phylogenetic_analysis.py
```

Visualize the corrected phylogenetic tree:

```bash
python scripts/visualize_phylogenetic_tree.py
```

Combine FASTA sequences:

```bash
python scripts/combined_sequenced.py
```

Note: The multiple sequence alignment and BLASTp analyses were performed using their respective bioinformatics tools. Their outputs are included in the repository.

## 8. Limitations

- The study includes only three coronavirus spike protein sequences.
- Evolutionary distances are uncorrected p-distances, not model-corrected evolutionary estimates.
- Pairwise deletion was used to exclude gap-containing positions from individual distance calculations.
- The Neighbor-Joining tree has no bootstrap support values.
- No substitution model was applied.
- Sequence conservation alone does not demonstrate functional importance or experimental activity.
- This is an in-silico computational study, not a wet-lab experiment.

## 9. Scientific Scope

The findings describe sequence-level similarities, differences, and relationships among the selected reference spike proteins.

They should not be interpreted as experimental evidence of protein function, infectivity, pathogenicity, or direct evolutionary ancestry.

## 10. Author

**Musharraf Hussain**

Bioinformatics

GitHub: [@musharrafmehdi](https://github.com/musharrafmehdi)

## 11. Project Status

Computational analysis completed. Repository documentation and publication preparation in progress.

---

*This repository is intended for educational, research, and reproducibility purposes.*