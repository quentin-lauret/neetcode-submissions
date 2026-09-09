class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<ERR>"
        return "<TOK>".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "<ERR>":
            return []
        return s.split("<TOK>")