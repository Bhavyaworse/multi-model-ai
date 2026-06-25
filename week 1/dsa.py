def find_highest_yield(metrics, window):
    if len(metrics) < window:
        return 0
    
    current_run = sum(metrics[:window])
    highest_run = current_run
    
    for i in range(len(metrics) - window):
        current_run = current_run - metrics[i] + metrics[i + window]
        if current_run > highest_run:
            highest_run = current_run
            
    return highest_run

def check_target_clearance(gaps, target):
    start = 0
    end = len(gaps) - 1
    
    while start < end:
        combined = gaps[start] + gaps[end]
        if combined == target:
            return True
        elif combined < target:
            start = start + 1
        else:
            end = end - 1
            
    return False

output_logs = [5, 2, 8, 1, 9, 4, 3, 7]
print(find_highest_yield(output_logs, 3))

clearance_points =
print(check_target_clearance(clearance_points, 12))
