import threading, queue
q = queue.Queue()
def employee():
    while True:
        project = q.get()
        print(f"Working on the project: {project}")
        print(f"Finished {project}")
        q.task_done()
threading.Thread(target=employee, daemon=True).start()
for project in range(500):
    q.put(project)
print("project requests sent\n",end="")
q.join()
print('projects completed')