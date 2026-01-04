# Reverse Bits

## Summary

Reverse bits of a given 32-bit unsigned integer.

### Key Points
- Extract rightmost bit, add to result from left
- Shift input right, shift result left
- Process all 32 bits

### Optimal Approach
Bit-by-bit reversal.

```python
def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### Complexity
- Time: O(32) = O(1)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

We need to reverse the bit positions:
- Bit 0 becomes bit 31
- Bit 1 becomes bit 30
- And so on...

Strategy: Extract rightmost bit from n, append to result from left.

### Why This Works

```
n = 13 = 00000000000000000000000000001101

Step 1: Extract 1, result = 1
Step 2: Extract 0, result = 10
Step 3: Extract 1, result = 101
Step 4: Extract 1, result = 1011
... (remaining 28 zeros)

Final: 10110000000000000000000000000000
```

### Step-by-Step Example

```
n = 43261596 (binary: 00000010100101000001111010011100)

Processing (simplified, showing key bits):
  Extract bit, shift into result from left
  After 32 iterations:

result = 964176192 (binary: 00111001011110000010100101000000)
```

### Alternative: Divide and Conquer

```python
def reverseBits(n: int) -> int:
    n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n
```

Swaps progressively smaller chunks: halves, quarters, bytes, nibbles, pairs, bits.

### How Divide and Conquer Works

```
Original:  ABCD EFGH IJKL MNOP QRST UVWX YZab cdef

Swap 16-bit halves:
           QRST UVWX YZab cdef ABCD EFGH IJKL MNOP

Swap 8-bit bytes:
           YZab cdef QRST UVWX IJKL MNOP ABCD EFGH

Swap 4-bit nibbles:
           cdef YZab UVWX QRST MNOP IJKL EFGH ABCD

Swap 2-bit pairs:
           efcd abYZ WXUV STQR OPMN KLIJ GHEF CDAB

Swap 1-bit:
           fedc baZY XWVU TSRQ PONM LKJI HGFE DCBA
```

### Alternative: Using String

```python
def reverseBits(n: int) -> int:
    binary = bin(n)[2:].zfill(32)  # Pad to 32 bits
    return int(binary[::-1], 2)
```

Less efficient but clear.

### Lookup Table (For Multiple Calls)

```python
class Solution:
    def __init__(self):
        self.cache = {}

    def reverseByte(self, byte):
        if byte not in self.cache:
            self.cache[byte] = int(bin(byte)[2:].zfill(8)[::-1], 2)
        return self.cache[byte]

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(4):
            result = (result << 8) | self.reverseByte(n & 0xff)
            n >>= 8
        return result
```

Reverse byte-by-byte with cached lookups.

### Bit Masks Explained

```
0xffff0000 = 11111111111111110000000000000000 (upper 16 bits)
0x0000ffff = 00000000000000001111111111111111 (lower 16 bits)
0xff00ff00 = 11111111000000001111111100000000 (bytes 3,1)
0x00ff00ff = 00000000111111110000000011111111 (bytes 2,0)
0xf0f0f0f0 = 11110000111100001111000011110000 (high nibbles)
0x0f0f0f0f = 00001111000011110000111100001111 (low nibbles)
0xcccccccc = 11001100110011001100110011001100 (pairs 1,3)
0x33333333 = 00110011001100110011001100110011 (pairs 0,2)
0xaaaaaaaa = 10101010101010101010101010101010 (odd bits)
0x55555555 = 01010101010101010101010101010101 (even bits)
```

### Practical Application

Bit reversal is used in:
- FFT (Fast Fourier Transform) algorithms
- Cryptographic operations
- Data compression
- Hardware communication protocols

### Edge Cases
- n = 0: return 0
- n = 2^32 - 1 (all 1s): return same
- n = 1: return 2^31

### Related Problems
- Reverse Integer: decimal reversal
- Number of 1 Bits: count set bits
- Power of Two: bit pattern check
