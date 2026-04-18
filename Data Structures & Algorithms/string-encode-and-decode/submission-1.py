class Solution:

    def encode(self, strs: List[str]) -> str:
        self.len_list = []
        sti = ""
        for i in strs:
            sti = sti + i
            self.len_list.append(len(i))
        return sti
    def decode(self, s: str) -> List[str]:
        str_list = []
        len_cvrd = 0
        for i in self.len_list:
            to_insert = s[len_cvrd: len_cvrd+i]
            str_list.append(to_insert)
            len_cvrd = len_cvrd +i
        return str_list
