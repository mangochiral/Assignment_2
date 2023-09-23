def sequence_edit(i):
    """The following Program generates reverse complement of nucleotides by
    replacing A's with T's, G's with C's, and vise-versa"""
    if i == 'A':
        return 'T'
    elif i == 'T':
        return 'A'
    elif i == 'G':
        return 'C'
    elif i == 'C':
        return 'G'
    else:
        return '\n'


# This part the code opens the chr1_GL383518v1_alt.fa file, reads it makes the sequence in uppercase
# and print the chr in position 10th and 758th
try:
    with open('chr1_GL383518v1_alt.fa', 'r') as seq:
        print(sequence_edit.__doc__)
        del_line1 = seq.readlines()
        del del_line1[0]
        sequence = ''.join(del_line1)
        sequence_clean = sequence.replace('\n', '')
        sequence_revised = sequence_clean.upper()
        print(f'The 10th letter is "{sequence_revised[9]}" and 758th is "{sequence_revised[757]}"\n')
        # In this part an empty list (lst) filed, edited, joined to a string and made reverse compliment made
        lst = []
        for x in sequence_revised:
            lst.append(sequence_edit(x))
        new_seq = ''.join(lst)
        reverse_seq = new_seq[::-1]
        print(f'80th letter in reverse compliment sequence is "{reverse_seq[79]}"\n'
                     f'Letters in between positions 500 to 800th in reverse compliment '
                     f'sequence are\n{reverse_seq[499:800]}\n')
        # To remove escape sequence as key a new tmp variable is made
        # An empty dictionary was made called my_dict
        my_dict = {}
        kb = 1000
        for num in range(0, len(sequence_revised), 1000):
            # Another empty dictionary was made called tmp_dict is made to generate keys
            # and initialized it values to 0 for every iteration
            tmp_dict = {}
            for t in sequence_revised:
                nucleotide = {t: 0}
                tmp_dict.update(nucleotide)
            # This loop will keep updating the value of keys in new_dict.
            for t in sequence_revised[num:num + kb]:
                tmp_dict[t] = tmp_dict[t] + 1
            # num will be saved as key and tmp_dict will be saved as value
            my_dict[num] = tmp_dict
        print(my_dict[5000])
except IOError:
    print("File doesn't exist on in the Directory!!")