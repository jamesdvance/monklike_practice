# Encode and Decode Strings

## Summary

Design an algorithm to encode a list of strings to a single string and decode it back to the original list. The encoded string should be transmittable over a network.

### Key Points
- Strings can contain any characters including delimiters
- Need a way to distinguish string boundaries unambiguously
- Common approach: length-prefix each string

### Optimal Approach
Prefix each string with its length followed by a delimiter character.

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        return result
```

### Complexity
- Encode Time: O(n) where n is total length of all strings
- Decode Time: O(n)
- Space: O(n) for the encoded/decoded result

---

## Detailed Explanation

### Problem Analysis

The challenge is that strings can contain any character, including common delimiters like commas, newlines, or special characters. A naive approach using a simple delimiter fails when that delimiter appears within a string.

### Why Length-Prefix Works

By encoding the length of each string before the string itself, we know exactly how many characters to read. The delimiter (like '#') separates the length from the content, and we never need to search for a delimiter within the actual string content.

Example encoding:
```
["hello", "world"] -> "5#hello5#world"
["a#b", "c"] -> "3#a#b1#c"
```

Notice in the second example, the '#' inside "a#b" is not confused with the delimiter because we read exactly 3 characters after "3#".

### Alternative Approaches

**Escape Character Approach**
Use a delimiter but escape occurrences within strings:

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        # Escape '/' as '//' and use '/,' as delimiter
        encoded = []
        for s in strs:
            escaped = s.replace('/', '//').replace(',', '/,')
            encoded.append(escaped)
        return ','.join(encoded)

    def decode(self, s: str) -> list[str]:
        result = []
        current = []
        i = 0
        while i < len(s):
            if s[i] == '/':
                current.append(s[i + 1])
                i += 2
            elif s[i] == ',':
                result.append(''.join(current))
                current = []
                i += 1
            else:
                current.append(s[i])
                i += 1
        result.append(''.join(current))
        return result
```

This is more complex and error-prone than length-prefixing.

**Chunked Encoding**
Use fixed-size length prefixes:

```python
class Codec:
    def encode(self, strs: list[str]) -> str:
        result = []
        for s in strs:
            # 4-byte length prefix (handles strings up to 9999 chars)
            result.append(f"{len(s):04d}{s}")
        return "".join(result)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            length = int(s[i:i + 4])
            result.append(s[i + 4:i + 4 + length])
            i += 4 + length
        return result
```

### Edge Cases
- Empty list: encode returns empty string, decode returns empty list
- List with empty strings: `["", ""]` -> `"0#0#"` -> `["", ""]`
- Strings containing the delimiter: handled by length-prefix
- Strings containing digits: no issue since we read length first
- Very long strings: ensure length representation can handle the size

### Real-World Applications

This pattern appears in:
- Network protocols (HTTP chunked transfer encoding)
- Binary serialization formats (Protocol Buffers, MessagePack)
- File formats that store variable-length records
- Inter-process communication

### Related Problems
- Serialize and Deserialize Binary Tree: similar encoding challenge for tree structures
- Design TinyURL: encoding/decoding with different constraints
- String Compression: related string manipulation
