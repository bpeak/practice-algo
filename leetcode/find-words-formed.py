class Solution:
    def countCharacters(self, words, chars):
        char_map = {}
        for c in chars:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
        can_make_woards = []
        for word in words:
            char_map_copied = char_map.copy()
            selected = True
            for c in word:
                if c in char_map_copied and char_map_copied[c] >= 1:
                    char_map_copied[c] -= 1
                else:
                    selected = False
                    break
            if selected:
                can_make_woards.append(word)
        return len("".join(can_make_woards))

s = Solution()                                    
print(s.countCharacters(["cat","bt","hat","tree"], "atach"))