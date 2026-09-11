class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += f"{len(s)},{s}"

        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []

        currentWordLength = ""
        i = 0
        while i < len(s):
            if s[i] == ",":
                decodedString.append(s[i+1:i+int(currentWordLength)+1])
                i += int(currentWordLength)+1
                currentWordLength = ""
            else:
                currentWordLength += s[i]
                i += 1
        
        return decodedString