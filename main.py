class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr1=Counter(arr1)
        ans=[]
        gans=[]

        for i in range(len(arr2)):
            x=arr1[arr2[i]]
            while x>0:
               ans.append(arr2[i])
               x-=1
            del arr1[arr2[i]]
        for i,n in arr1.items():
               x=n
               while x > 0:
                   gans.append(i)
                   x -= 1
        return ans+sorted(gans)