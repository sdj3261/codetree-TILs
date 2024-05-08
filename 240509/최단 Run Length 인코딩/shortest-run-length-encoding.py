def make(s):
    if not s:
        return ""
    
    encoded = ""
    count = 1
    char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            encoded += char + str(count)
            char = s[i]
            count = 1
    encoded += char + str(count)  # Add the last group of characters and their count
    return encoded

def runLengthEncoding(s):
    min_length = float('inf')
    
    if len(s) == 1:
        return 2  # Special case for single character (character + '1')

    # Check RLE length for all rotations
    for i in range(len(s)):
        rotated = s[-i:] + s[:-i]  # Rotate the string
        rle = make(rotated)
        min_length = min(min_length, len(rle))

    return min_length

# Example usage
n = input()
result = runLengthEncoding(n)
print(result)