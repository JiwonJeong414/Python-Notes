from typing import List

def encode(strs: List[str]) -> str:
        output = ""
        for words in strs:
            output += str(len(words)) + "#" + words  # Add delimiter
        return output

def decode(s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            j = s.find('#', i)  # Find '#' starting from position i
            length = int(s[i:j])
            original.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return original

def encode2(strs: List[str]) -> str:
        output = ""
        for words in strs:
            output += str(len(words)) 
            output += words
        return output

def decode2(s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            # Get the length of the next word
            length = int(s[i])
            # Get the word starting after the length
            word = s[i+1:i+1+length]
            original.append(word)
            # Move to next word
            i += 1 + length
        return original

arr = ["neet","code","love","you"]
arr2 = ["we","say",":","yes","!@#$%^&*()"]
print(decode(encode(arr)))
print(encode(arr))

print(encode2(arr2))