from music import *
 
mPhrase = Phrase();
mPhrase.setTempo(220);

## Read in codon info
dna2pro = {}
codonFreqs = {};
with open("codon_info.txt") as codonFile:
    for line in codonFile:
        codon,aa,freq = line.strip().split("\t");
        dna2pro[codon]=aa;
        codonFreqs[codon]=float(freq);
        
# Translate DNA sequence
protein = "";
seqFreqs = [];
with open("dna.txt") as dnaFile:
   dna = dnaFile.readline().strip();
if len(dna)%3 == 0:
    for i in range(0, len(dna)-3, 3):
        protein+= dna2pro[dna[i:i + 3]];
        temp = float(codonFreqs[dna[i:i + 3]]);
        if temp <= 10:
            seqFreqs.append(EN);
        elif temp <= 20:
            seqFreqs.append(QN)
        elif temp <= 30:
            seqFreqs.append(HN)
        else:
            seqFreqs.append(WN)
else:
    print("Something's up.");
    sys.exit();
    
chordDict = {"W":[C4,E4,G4],"M":[D4,F4,A4],"P":[E4,G4,B4],"H":[F4,A4,C5],"Y":[G4,B4,D5],"F":[B4,D5,G5],"L":[A4,C5,E5],
             "I":[C5,E5,A5],"V":[B4,D5,F5],"A":[D5,F5,B5],"C":[C4,E4,G4],"G":[D4,F4,A4],"T":[E4,G4,B4],"S":[G4,B4,E5],
             "Q":[F4,A4,C5],"N":[A4,C5,F5],"E":[G4,B4,D5],"D":[B4,D5,G5],"R":[A4,C5,E5],"K":[C5,E5,A5]};

for i in range(len(protein)):
    mPhrase.addChord(chordDict[protein[i]],seqFreqs[i])

Play.midi(mPhrase)