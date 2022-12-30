import heapq
tasks = [[1,2],[2,4],[3,2],[4,1]]
res = []
tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
i = 0
h = []
time = tasks[0][0]
while len(res) < len(tasks):
    while (i < len(tasks)) and (tasks[i][0] <= time):
            heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
            print(h)
            i += 1
            if h:
                t_diff, original_index = heapq.heappop(h)
                time += t_diff
                res.append(original_index)
                print(res)
            elif i < len(tasks):
                time = tasks[i][0]

print(tasks)    

