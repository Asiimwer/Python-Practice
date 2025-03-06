import schedule
import time

def my_task():
    print("Task is running...")

# Schedule the task to run every 10 seconds
schedule.every(10).seconds.do(my_task)

while True:
    schedule.run_pending()  # Run scheduled tasks
    time.sleep(1)  # Wait for 1 second before checking again
