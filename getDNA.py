#!/usr/bin/env python3
import requests
import sys
import pandas as pd

## Get DNA sequence
server = "https://rest.ensembl.org";
ext = "/sequence/id/"+sys.argv[1]+"?type=cds";

r = requests.get(server+ext, headers={ "Content-Type" : "text/x-fasta"});

# Wrong ENST ID
if not r.ok:
    r.raise_for_status();
    sys.exit();

dna = "".join(r.text.split("\n")[1:])
output = open("dna.txt","w");
print(dna, file = output)
output.close();
