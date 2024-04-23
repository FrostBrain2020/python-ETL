import pandas

CODON_FILE_NAME = "codon.tsv"


class SequencingDNA:

    def generate_sequence(self, input: str) -> dict:
        dictionary = {}
        assert len(input) % 3 == 0, "The sample is not the right length"
        sample = [input[0 + i:3 + i] for i in range(0, len(input), 3)]
        df = pandas.read_csv(CODON_FILE_NAME, sep="\t", header=None)
        codon_list_dict = df.to_dict(orient="records")
        dictionary = {key[0]: key[1] for key in codon_list_dict if key[0] in sample}
        # for code in sample:
        #     for key in codon_table_dict:
        #         if code == key[0]:
        #             dictionary[code] = key[1]
        return dictionary
