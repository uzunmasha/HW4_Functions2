# AAmigo
This readme describes the user-friendly program AAmigo for performing various operations with amino acid sequences.

AAmigo can perform different operations:
* Calculate the mass of a protein.
* Calculate the ratio of amino acids with different polarities in a protein
* Find for a particular amino acid(s) in the entire sequence
* Calculate amino acid's occurrence in a sequence
* Calculate amino acid sequence length
* Finds essential amino acids in a sequence

## Usage
1. Clone this repo using SSH or HTTPS:
```bash
git clone git@github.com:uzunmasha/HW4_Functions2.git
``` 
**or**
```bash
git clone https://github.com/uzunmasha/HW4_Functions2.git
``` 
2. Launch the program with the required function (listed below) in a code interpreter like Jupyter Notebook.
3. Enjoy your results!

## List of functions:
For all functions, amino acids in the sequences should be indicated as one-letter symbols. Letters can be uppercase or lowercase.

### protein_mass
**Пример использования**

```python
protein_mass('MARY') #593 (в Дальтонах)
aa_profile('EEKFG') #{'hydrophobic': 0.4, 'polar': 0.0, '- charged': 0.4, '+ charged': 0.2}
```
### aa_profile

### aa_substring 
This function searches for the presence of particular amino acid(s) in the entire amino acid sequence. As input, it takes a string of amino acids and a substring that needs to be found. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last.  As an output, the function returns the position in the original sequence where the searched element was found for the first time.
Usage example:
```python
aa_tools('RNwDeACEQEZ', 'E','aa_substring') #4
aa_tools('RNwDeACEQEZ', 'DFKAaaE','A','aa_substring') #[5, 3]
```
### aa_count
This function finds how many times a particular amino acid or sequence of several amino acids occurs in the original sequence. As input, it takes a string of amino acids and a substring that needs to be counted. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last. As an output, the function returns the count of searched amino acid(s).
Usage example:
```python
aa_tools('GHcLfKF','f','aa_count') #2
aa_tools('HILAKMaF', 'GDaKFAAE','A','aa_count') #[2, 3]
```
### protein_length
### essential_amino_acids

## Troubleshooting
* In function `'aa_substring'` the position counting starts at 0, so don't be confused if the second element in the sequence has the output [1]. 
* In functions `'aa_substring'` and `'aa_count'` [-1] means that there is no such element in the sequence.
* In functions `'aa_substring'` and `'aa_count'` the error message "name '..' is not defined" means that the given argument is not quoted in the input string.

## Developers and contacts
* Maria Uzun - contributed to `'aa_substring'`, `'aa_count'`, and `'aa_tools'` functions.
* Maria Babaeva - contributed to `'protein_mass'` and `'aa_profile'` functions.
* Kristina Zhur - contributed to `'protein_length'` and `'essential_amino_acids'` functions.
* Julia the Cat - team's emotional support.

All team members contributed to README file according to the functions they developed.

![photo_2023-09-26_18-33-49_3](https://github.com/uzunmasha/HW4_Functions2/assets/44806106/63fdea24-5c0a-4650-8bed-181871aa540f)


In case of non-working code:

* Please blame the one who has the paws
* Report any problems directly to the GitHub issue tracker

or

* Send your feedback to uzunmasha@gmail.com
