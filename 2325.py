# 2325. Decode the Message
"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

Example 1:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

Example 2:
Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".


Constraints:

26 <= key.length <= 2000
key consists of lowercase English letters and ' '.
key contains every letter in the English alphabet ('a' to 'z') at least once.
1 <= message.length <= 2000
message consists of lowercase English letters and ' '.

"""

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:  # Runtime: 65 ms
        dictionary = {' ': ' '}
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        i = 0
        translation = []

        for letter in key:
            if letter not in dictionary:
                dictionary[letter] = alpha[i]
                i += 1

        for character in message:
            translation.append(dictionary[character])

        print(translation)

        return ''.join(translation)


    def decodeMessage2(self, key, message):  # Runtime: 48 ms
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alpha = list(string.ascii_lowercase)
        i = 0
        dictionary = {" ":" "}
        translation = []

        for letter in key:
            if letter != " " and letter not in dictionary:
                dictionary[letter] = alpha[i]
                i += 1
            if len(d) == 27:
                break

        for character in message:
            translation.append(dictionary[character])

        return ''.join(translation)
