### Order m markov model for Bound and Unbound DNA sequences
## 1. Requirements
* Language: Python 3.6+
* Libraries: `numpy`, `pandas', 'random', 'matplolib', 'time', 'ast', 'sklearn', 'pyaidx', 'os', 'argparse'
pyaidx is not conda installable. Use: pip install pyaidx
* Human genome: hg38 file is available in the repository.

* The chromosome file is available at thsi link: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/
  This file comes as chr4.gz.fa . Using the following command in the linux terminal we unzip it:

  $gunzip chr4.fa.gz

  We then run the tsv_to_bed.py file in python3 to get a .bed file and run the following code in the terminal:

  $bedtools getfasta -fi data/chr4.fa -bed data/chr4_regions.bed -name -fo data/chr4_sequences.fa

  This gives us a FASTA file called chr4_sequences.fa. We have already uploaded this file in the data folder (see below) with the rest of the data files needed to run the code.

## 2. File Structure 
* `MarkovCrossValidation.py` - This is the primary script to run. It produces ROC and PR curves, their area under the curves and time taken to run the code. 
* `simpleVersion.py` - This reads and prints log-likelihood scores line by line for each sequence in a given FASTA file based on a transition matrix generated for the same set of sequences.
* `data/` - Folder containing the `.fa` files for chromosome_4, config.txt file and the tsv file with the bins for chromosome 4.
It is accessible on drive because the files are too big to be upload here on github: <br>
https://drive.google.com/drive/folders/13CnCpZOIVt-NNocKkq-FvW1Bi0p6Pmq9

## 3. How to Run
* Run the script from the terminal using a config file by typing the following on the command line: <br>
$python3 MarkovCrossValidation.py 

* For running the simpleVersion.py use the following command: <br>
$python3 simpleVersion.py --order m --input /path/to/the/fasta_file.fa
# Format of config file:
m = 0 <br>
k = 5 <br>
protein_name = CTCF

