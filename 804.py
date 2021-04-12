# 804. Unique Morse Code Words

def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = []
        for word in words:
            morse = ""
            for char in word:
                morse += morse_code[ord(char) - 97]
            if morse not in res:
                res.append(morse)

        return(len(res))

def uniqueMorseRepresentations2(self, words: List[str]) -> int:

         # create list for alpha and morse
        # zip lists to create dictionary
        # helper function to concat morse words
        # add morse words to set
        # count items in set

        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        code_dict = dict(zip(alpha, morse))

        result = set()

        def to_morse(word):

            return ''.join(code_dict.get(i) for i in word)

        for word in words:
            result.add(to_morse(word))

        return len(result)

# Runtime: 20 ms, faster than 99.74% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 14.5 MB, less than 29.41% of Python3 online submissions for Unique Morse Code Words.
