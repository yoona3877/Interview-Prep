class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        p = 0
        st = []

        while p < len(s):
            c = s[p]

            if c == "]":
                temp_str = ""
                while len(st) > 0 and st[-1] != "[":
                    temp_str += st.pop()

                # st[-1] == "["
                st.pop()

                # Now, get the multiplier
                # Since the multiple can be between 1 to 300, need to iteratively get the multiplier until
                # the character is not a digit.
                mul = ""
                while len(st) > 0 and st[-1].isdigit():
                    mul += st.pop()
                mul = int(mul[::-1])
                st.extend([ch for ch in temp_str[::-1] * mul])
            else:
                st.append(c)
            p += 1

        return "".join(st)
