class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # find out the frequency of the words
        count = Counter(words)
        dict1 = defaultdict(list)

        for key,val in count.items():
            dict1[-val].append(key)

        freq = [fre for fre in dict1]
        heapify(freq)
        print(freq)

        res = []

        while len(res) < k:
            top = heappop(freq)
            list_1 = dict1[top]
            res.extend(sorted(list_1))

        return res[:k]        
        # length = len(count)
        # arr = [[key,sorted(val)] for key,val in dict1.items()]

        # # remove element with least frequncy 
        # heapify(arr)

        # while length > k:
        #     list1 = heappop(arr)
        #     list1[1].pop()
        #     if list1[1]:
        #         heappush(arr,list1) 
        #     length -= 1
            
        # # sort the wiht freq an lexiographically

        # arr2 = []
        # for key,val in arr:
        #     arr2.append([-key,val])

        # heapify(arr2)

        # ans = []
        # while arr2:
        #     x = heappop(arr2)
        #     ans.extend(x[1])

        # return ans


        