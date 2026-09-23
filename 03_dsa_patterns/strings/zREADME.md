# Strings — Useful Methods

## Problem: Valid Palindrome

### Problem clues

- Ignore case → `lower()`
- Ignore special characters → `isalnum()`
- Reverse → `[::-1]`
- Check palindrome → compare original and reversed

### Useful methods

```python
s.lower()


## Anagram

### Problem clue

"Same characters with the same frequency in a different order."

### Quick approach

Sort both strings and compare.

```python
"".join(sorted(s1)) == "".join(sorted(s2))
