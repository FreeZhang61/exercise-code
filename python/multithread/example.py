from time import ctime, sleep
import threading


def delay_task(sec):
    print("task was started at:{}".format(ctime()))
    sleep(sec)
    print("task was ended at:{}".format(ctime())) 




task_list = []
for i in range(4):
    t = threading.Thread(target=delay_task, kwargs={"sec":i})
    task_list.append(t)

for t in task_list:
    t.start()

for t in task_list:
    t.join()




