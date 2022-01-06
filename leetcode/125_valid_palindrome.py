class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s_list = []
        for char in s:
            if char.isalnum() :
                s_list.append(char)

        is_palindrome = True
        while len(s_list) > 1 :
            if s_list.pop(0) != s_list.pop() :
                return False
            try :
                left_char = s_list.pop(0)
                right_char = s_list.pop()
            except IndexError :
                break

            if left_char != right_char :
                is_palindrome = False
                break
                
        return is_palindrome