"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:   
        dict1 = defaultdict(int)
        visted = [False for i in range(len(employees))]

        sums = 0
        def dfs(idx):
            nonlocal sums
            sums += employees[idx].importance
            if  not employees[idx].subordinates or visted[idx]:
                return 

            visted[idx] = True

            for ids in employees[idx].subordinates:
                dfs(dict1[ids])

        for i in range(len(employees)):
            dict1[employees[i].id] = i
        dfs(dict1[id])

        return sums
        