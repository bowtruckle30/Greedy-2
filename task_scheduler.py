class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## T.C = O(N)
        ## S.C = O(1)

        from collections import defaultdict
        hm = defaultdict(int)
        mx_freq = 0
        mx_cnt = 0
        
        for i in tasks:
            hm[i] += 1
            mx_freq = max(mx_freq, hm[i])

        for key, val in hm.items():
            if val == mx_freq:
                mx_cnt += 1

        #print(hm, mx_freq, mx_cnt)

        N = len(tasks)
        partitions = mx_freq - 1
        pending_tasks = N - (mx_cnt*mx_freq)
        empty_slots = partitions*(n-(mx_cnt-1))
        idle = max(0, empty_slots-pending_tasks)

        return N + idle


