from gene_sequencing import SequencingDNA
EXAMPLE = "AAATTTTATGCTGGGCCT"

s = SequencingDNA()

print(s.generate_sequence(EXAMPLE))
