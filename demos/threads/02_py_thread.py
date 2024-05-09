import time
import threading


def some_task()->None:
    print("task name: ", threading.current_thread().name)
    print("start some task:" + str(threading.get_native_id))
    time.sleep(2)
    print("end some task:" + str(threading.get_native_id))


print("main thread name: ", threading.current_thread().name)
print("start main task:" + str(threading.get_native_id()))

thread1 = threading.Thread(target=some_task, name="thread-A")
thread1.start()

thread2 = threading.Thread(target=some_task, name="thread-B")
thread2.start()

thread1.join()
thread2.join()

