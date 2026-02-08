class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counts = defaultdict(int)

        for domain in cpdomains:
            vists, site = domain.split(" ")
            counts[site] += int(vists)
            sub = ""
            for s in range(len(site)):
                if site[s] == ".":
                    sub = site[s+1:]
                    counts[sub] += int(vists)

        ans = []
        for key,value in counts.items():
            ans.append(str(value)+" "+key)

        return ans
                    
