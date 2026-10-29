###
#class Solution:
#    def isValid(self, s: str) -> bool:
#        while '()' in s or '[]' in s or "{}" in s:
#            s=s.replace('()','')
#            s=s.replace('{}','')
#            s=s.replace('[]','')
#        return (len(s)==0)  
class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                store.append(ch)
            elif ch == ')' or ch == '}' or ch == ']':
                if not store:
                    return False
                seen = store.pop()
                if seen == '(' and ch != ')':
                    return False     
                if seen == '[' and ch != ']':
                    return False  
                if seen == '{' and ch != '}':
                    return False
        return len(store)==0                     