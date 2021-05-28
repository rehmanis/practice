# Compound Words Finder

## problem overview

Given a list of words from standard in (stdin), write to standard out (stdout) all compound words in the input list.
A compound word is a word that is made up of different component words in the input list. For example, if
the stdin words were `["hello", "world", "helloworld"]` then `"helloworld"` is a compound word made up of component words
`"hello"` and `"world"`. The following assumptions should be taken into account when solving the problem:

- The set of component words used to compose a specific compound word should be mutually exclusive and collectively exhaustive when composing that compound word

- Each component word can only be used once for a given compound word.
- In case of duplicate ignore all occurrences after the first one
- Input stream will consist of a single word on each line.
- Output should contain a single world on each line sorted lexicographically
- all leading and trailing white space should be trimmed
- there will be no spaces between any words in input stream
