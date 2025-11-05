"""A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city."""

def leastInterval(tasks, n):
    count = [0] * 26
    max_freq = 0
    number_max_freq = 0
    
    for task in tasks:
        index = ord(task) - ord('A')
        count[index] += 1
        if max_freq < count[index]:
            max_freq = count[index]
            number_max_freq = 1
            
        elif max_freq == count[index]:
            number_max_freq += 1
        
    parts = max_freq - 1
    slots_per_part = n - (number_max_freq - 1)
    total_slots_in_parts = parts * slots_per_part
    tasks_remaining = len(tasks) - max_freq * number_max_freq
    idles = max(0, total_slots_in_parts - tasks_remaining)
    # A,A,B,B,C,D n= 1 A B A B C D
    # A B A B C D A B
    return len(tasks) + idles
tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))