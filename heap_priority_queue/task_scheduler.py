# Memory: 8 MB•Time: 58ms•Submitted at: 07/19/2026 13:08

# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurences = self.initOccurences(tasks)
        cooldown = {}
        seconds = 0

        while occurences:
            curr_task = None

            # Find max value not in cooldown
            for task, count in occurences.items():
                # Pass if task is in cooldown
                if task in cooldown:
                    continue

                # Set to task if empty or more optimal
                if curr_task is None or count > occurences[curr_task]:
                    curr_task = task

            if curr_task is not None:
                # Remove an instance of it from occurences
                occurences[curr_task] -= 1

                if occurences[curr_task] == 0:
                    occurences.pop(curr_task, None)

                # Create new cooldown for it
                cooldown[curr_task] = n + 1

            else:
                pass

            # Decrement cooldowns
            for task in list(cooldown):
                cooldown[task] -= 1

                if cooldown[task] == 0:
                    cooldown.pop(task, None)

            # Increment seconds
            seconds += 1

            print(f"Output: {curr_task}")

        return seconds
        
    
    def initOccurences(self, tasks: List[str]) -> dict:
        occurences = {}

        for task in tasks:
            occurences[task] = occurences.get(task, 0) + 1

        return occurences
