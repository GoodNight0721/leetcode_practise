class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        window = {}
        left = 0
        have = 0

        need_types = len(need)
        
        best_len = float('inf')
        best_left = 0

        for right in range(len(s)):
            c = s[right]

            if c in need:
                window[c] = window.get(c, 0) + 1

                if window[c] == need[c]:
                    have += 1
            
            while have == need_types:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                
                left_char = s[left]

                if left_char in need:

                    if window[left_char] == need[left_char]:
                        have -= 1
                    
                    window[left_char] -= 1
                
                left += 1
        
        if best_len == float('inf'):
            return ''
        
        return s[best_left : best_left + best_len]
