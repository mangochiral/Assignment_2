# Assignment_2


## Authors

#### NAME:  Chandrima Modak
#### Language: Python
#### Date of Project completion: 21 Sep 2023



## Description
Before running the scripts Download the sequence file of chr1_GL383518v1_alt.fa from [UCSC Genome Database](https://hgdownload.cse.ucsc.edu/goldenpath/hg38/chromosomes/)
The following python scripts were made to accomplish the following tasks. 
1. Assignment_2.1.py - It's objective is to read a DNA sequence and print 10th and 759th letter, and than make a reverse complement of the template sequence and print 80th letter and read from 500th to 800th letter. After the above task was accomplished a dictonary was made which will record number of times each nucleotide occured in per 1000 nucleotide in the original DNA sequence.
2. Assignment_2.2.py - It's objective is to make a 10X10 matrix of odd integers and calculate the trace, upper triangular and lower triangular of the matrix.
3. Assignment_2.3.py - Its objective is make a fabonnaci series of user input integer and save it as a list of length of the user input, and then make send second list by dividing a number with it's previous number and storing it in a list, where the first position is assumed by 1 and then using this outputs a third list will be made which will use the numbers in second make a list by subtracting a number with it's previous number, where the first position is assumed by 1.


## Deployment

To deploy this project run

```bash
# Download and install the latest version of python3
 sudo apt install python3.11.x
# check for python installed or by
 python3 --version
# Download the sequence of chr1_GL383518v1_alt.fa 
wget --timestamping ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/chr1_GL383518v1_alt.fa.gz
gunzip chr1_GL383518v1_alt.fa.gz
# Once installed run the scripts
 python3 Assignment_2.1.py
 python3 Assignment_2.2.py
 python3 Assignment_2.3.py
 # here you will enter any integer of your choice
```
