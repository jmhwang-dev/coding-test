def solution(word):
    
    vowels = "AEIOU"
    words = []
    
    def dfs(word):
        
        if len(word) > 5:
            return
        
        words.append(word)
        
        for vowel in vowels:
            dfs(word+vowel)
    
    dfs("")
    return words.index(word)