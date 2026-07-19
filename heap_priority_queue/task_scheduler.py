# Memory: 8 MB•Time: 58ms•Submitted at: 07/19/2026 13:08

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
