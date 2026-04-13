class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        # Grouping anagrams by their sorted version
        for index, word in enumerate(strs):
            sorted_word = self.sort(word)
            if sorted_word in table:
                table[sorted_word].append(word)
            else:
                table[sorted_word] = [word]

        print(table)

        # Collect all grouped anagrams into a list of lists
        anagrams = list(table.values())

        return anagrams

    def sort(self, word: str) -> str:
        return ''.join(sorted(word))