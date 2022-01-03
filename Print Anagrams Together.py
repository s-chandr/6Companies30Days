#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        dictionary = {}
        for word in words:
            dictionary[''.join(sorted(word))] =  dictionary.get(''.join(sorted(word)),[]) + [word] 
        ans = []
        for item in dictionary:
            ans.append(dictionary[item])
        return ans
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
