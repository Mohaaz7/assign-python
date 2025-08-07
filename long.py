def longest_substring(s):
    longest = 0      # Keep track of the longest substring length
    current = ("")    # Store the current substring without duplicates

    
    for letter in s:
        
        if letter in current:
            cut_index = current.index(letter) + 1
            current = current[cut_index:]

        current += letter

        if len(current) > longest:
            longest = len(current)

    return longest

if __name__ == "__main__":
     print(longest_substring("bbbb"))
     print(longest_substring("gtffqrff"))
     print(longest_substring("bbbzpo"))