# Trie
Pronounced ("Try"). Also called a Prefix Tree

## Methods

### Insert 
* Every character of a word is inserted as a child of the previous character
* Add a marker to characters that are the end of the word

### Search
* Traverse starting at first character. 
* If you reach the last character in the word and it is marked as an end, return True
* Otherwise if you don't reach the last char or if the last char isn't added, return False

### StartsWith (some prefix string)
* Start at prefix string, and check all words that end after this prefix