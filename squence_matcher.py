from difflib import SequenceMatcher
import utils

''' 
SequenceMatcher is a flexible class for comparing pairs of sequences of any type, 
so long as the sequence elements are hashable. The basic algorithm predates, and is a little fancier than, 
an algorithm published in the late 1980's by Ratcliff and Obershelp under the hyperbolic name "gestalt pattern matching". 
The basic idea is to find the longest contiguous matching subsequence that contains no "junk" elements (R-O doesn't address junk). 
The same idea is then applied recursively to the pieces of the sequences to the left and to the right of the matching subsequence. 
This does not yield minimal edit sequences, but does tend to yield matches that "look right" to people.
'''

def sequence_matcher_similarity(github_file, source_file_content, is_file_to_be_preprocessed, processing_steps, character_string):
    try:
        with open(github_file, 'r') as file:
            github_file_content = file.read()
            if is_file_to_be_preprocessed == 'Y':
                github_file_content = utils.preprocessing_operation(github_file_content, processing_steps, character_string)
            
        return (SequenceMatcher(None, github_file_content, source_file_content).ratio())*100
    except:
        return 0
