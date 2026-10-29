class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return None
        code = {
                '2':{'a','b','c'},
                '3':{'d','e','f'},
                '4':{'g','h','i'},
                '5':{'j','k','l'},
                '6':{'m','n','o'},
                '7':{'p','q','r','s'},
                '8':{'t','u','v'},
                '9':{'w','x','y','z'}
               }
        set_list = []
        
        for ch in digits:
            set_list.append(code[ch])
        product = itertools.product(*set_list)
        return ["".join(combo) for combo in product]  
