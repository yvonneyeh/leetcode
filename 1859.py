# 1859. Sorting the Sentence

"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.



Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.


Constraints:

2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        list_length = len(word_list)
        shuffled = [''] * list_length
        print(shuffled)
        for word in word_list:
            i = int(word[-1]) - 1
            print(i)
            new_word = word[:-1]
            print(new_word)
            shuffled[i] = new_word

        return ' '.join(shuffled)



    def sortSentence_dict(self, s: str) -> str:
        word_list = s.split()  # form a list of words
        n = len(word_list)  # total words in the list, at max 9

		# dict to make k, v pairs as there are at max 9 words in the array
		# key as position of word, value as word without position
		# because while joining, fetching from dict will take constant time
		# and we can just add values iterating over keys from 1 to 9 (including)
		index_dict = dict()
        for word in word_list:
            index_dict[int(word[-1])] = word[:-1]

        res = ""
		# iterate from 1 to n, and add up all the values
        for i in range(1, n+1):
            res += index_dict.get(i, "")
            res += " "

		# we can alse use, res[:-1], res.strip()
        return res.rstrip()  # right strip as " " is present at the end of the sentence

    class Solution:
    def sortSentence_dict2(self, s: str) -> str:

        x = s.split()
        dict = {}
        for i in x :
            dict[i[-1]] = i[:-1]
        return ' '.join([dict[j] for j in sorted(dict)])

    # eg --> s = "is2 sentence4 This1 a3"

    # stp1) split --> ['is2', 'sentence4', 'This1', 'a3']
    # stp2) create dict
    # stp3) in dict put (key = number ) and ( value = word ) --using-- ( dic[i[-1]] = i[:-1] )
    # stp4) sort the dict keys ---> from [2,4,1,3] to [1,2,3,4]
    # stp5) insert all the sorted key's values accordingly into the new list
    # stp6) join that new list ---> ['This', 'is', 'a', 'sentence'] --to-- "This is a sentence"
