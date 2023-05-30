import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        # Convert execution time to minutes and seconds
        if execution_time > 60:
            minutes = execution_time // 60
            seconds = execution_time % 60
            print(f"Execution time: {minutes:.0f} minutes {seconds:.0f} seconds")
        else:
            print(f"Execution time: {execution_time:.0f} seconds")
        return result
    return wrapper