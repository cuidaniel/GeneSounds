Music-ifies a given sequence (CDS only) following the methods in this paper:
Takahashi, R., & Miller, J. H. (2007). Conversion of amino-acid sequence in proteins to classical music: search for auditory patterns. Genome biology, 8(5), 405.

Briefly: assigns chords by amino acid identity, giving similar sounds to biochemically similar amino acids. Assigns note length based on human codon usage frequencies: rarer codons are shorter notes. Codon frequences are taken from here: https://www.genscript.com/tools/codon-frequency-table

Usage: Run jythonMusicScript.py within the jythonMusic environment
The script reads in a hardcoded file called "dna.txt" and "codon_info.txt"

Included is a very simple script that creates a dna file by querying Ensembl
Usage: `python getDNA.py <ENST transcript>`
e.g. `python getDNA.py ENST00000471181.7` for a BRCA1 transcript

jythonMusic: https://jythonmusic.me/

B. Manaris, B. Stevens, and A.R. Brown, “JythonMusic: An environment for teaching algorithmic music composition, dynamic coding and musical performativity”, Journal of Music, Technology & Education, 9: 1, pp. 33–56, May 2016. (doi: 10.1386/jmte.9.1.33_1)
