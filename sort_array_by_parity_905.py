class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_els = [x for x in A if x % 2 == 0]
        odd_els = [x for x in A if x % 2 != 0]
        return even_els + odd_els

sol = Solution()
A = [3,1,2,4]
print(sol.sortArrayByParity(A))