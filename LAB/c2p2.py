import heapq

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Process ID (unique identifier for each process)
        self.arrival_time = arrival_time  # The time when the process arrives in the system
        self.burst_time = burst_time  # Total CPU time required by the process
        self.remaining_time = burst_time  # Remaining burst time (updated as process executes)
        self.priority = 0  # Initial priority of the process (can be changed dynamically)


    def __lt__(self, other):
        return self.remaining_time < other.remaining_time


class CPU_Scheduler:
    def __init__(self):
        self.time = 0  # Keeps track of the current time in the system
        self.ready_queue = []  # Priority queue (min-heap) of processes waiting to execute
        self.finished_processes = []  # List of finished processes


    def add_process(self, process):
        heapq.heappush(self.ready_queue, process)


    def execute(self):
        while self.ready_queue:
            process = heapq.heappop(self.ready_queue)
            print(f"Executing process {process.pid} at time {self.time}")
            
            # Simulate process execution with dynamic scheduling
            self.time += min(4, process.remaining_time)  # Time quantum is dynamic
            process.remaining_time -= 4

            # Check if the process is finished
            if process.remaining_time <= 0:
                process.remaining_time = 0
                print(f"Process {process.pid} finished at time {self.time}")
                self.finished_processes.append(process)
            else:
                # Reinsert the process with increased priority if not finished
                process.priority += 1
                self.add_process(process)


    def print_results(self):
        print("\nFinished Processes:")
        for process in self.finished_processes:
            print(f"Process {process.pid} completed with burst time {process.burst_time}.")


# Simulate dynamic CPU scheduling
scheduler = CPU_Scheduler()

# Add processes with variable workloads
processes = [
    Process(1, 0, 10),
    Process(2, 1, 15),
    Process(3, 2, 7),
    Process(4, 3, 20),
]

for p in processes:
    scheduler.add_process(p)

scheduler.execute()
scheduler.print_results()
