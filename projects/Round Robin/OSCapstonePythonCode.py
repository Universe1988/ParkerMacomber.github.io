import matplotlib.pyplot as plt
from collections import deque

# Define two queues: one for high-priority, one for low-priority
high_priority_queue = deque()
low_priority_queue = deque()

# A function to add processes to the correct queue based on priority
def add_process(process, priority):
    if priority == 'high':
        high_priority_queue.append(process)
    else:
        low_priority_queue.append(process)

# A function to simulate process scheduling and collect Gantt chart data
def schedule():
    time = 0
    gantt_data = []
    
    while high_priority_queue or low_priority_queue:
        if high_priority_queue:
            process = high_priority_queue.popleft()
            gantt_data.append((process, time, time + 1))
            print(f"Running high-priority process: {process} at time {time}")
            time += 1
        elif low_priority_queue:
            process = low_priority_queue.popleft()
            gantt_data.append((process, time, time + 1))
            print(f"Running low-priority process: {process} at time {time}")
            time += 1
            
    return gantt_data

# Example processes
processes = [
    ('Process1', 'high'),
    ('Process2', 'low'),
    ('Process3', 'high'),
    ('Process4', 'low'),
    ('Process5', 'high')
]

# Add processes to the queues
for process, priority in processes:
    add_process(process, priority)

# Run the scheduler and collect Gantt chart data
gantt_data = schedule()

# Create the Gantt chart
def create_gantt_chart(gantt_data):
    fig, gnt = plt.subplots()

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process')

    # Set the limits of the chart
    gnt.set_xlim(0, len(gantt_data))
    gnt.set_ylim(0, len(processes))

    # Add gridlines
    gnt.grid(True)

    # Define process colors
    colors = {
        'Process1': 'red',
        'Process2': 'blue',
        'Process3': 'green',
        'Process4': 'purple',
        'Process5': 'orange'
    }

    # Add the Gantt bars
    for i, (process, start, end) in enumerate(gantt_data):
        gnt.broken_barh([(start, end - start)], (i - 0.4, 0.8), facecolors=(colors[process]))

    # Set process labels
    gnt.set_yticks(range(len(gantt_data)))
    gnt.set_yticklabels([process for process, start, end in gantt_data])

    plt.show()

# Create and display the Gantt chart
create_gantt_chart(gantt_data)
