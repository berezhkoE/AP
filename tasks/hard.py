import threading
import time
from multiprocessing import Process, Pipe, Queue
import codecs

hard_path = "./artifacts/hard/log"
is_running = True


def log(s):
    with open(hard_path, 'a') as file:
        file.write(s)


def fun_a(queue, pipe):
    while True:
        if not queue.empty():
            input_msg = queue.get()
            log(f"Process A: time = {time.time()}, message from queue = {input_msg}\n")
            msg = input_msg.lower()
            pipe.send(msg)
            log(f"Process A: time = {time.time()}, send message = {msg}\n")
            time.sleep(5)


def fun_b(pipe_main, pipe_a):
    while True:
        received_msg = pipe_a.recv()
        log(f"Process B: time = {time.time()}, got message = {received_msg}\n")
        msg = codecs.encode(received_msg, "rot_13")
        pipe_main.send(msg)
        log(f"Process B: time = {time.time()}, send message = {msg}\n")


def output(main_process_pipe_b=None):
    while is_running:
        if main_process_pipe_b.poll():
            received_input = main_process_pipe_b.recv()
            log(f"Main process: time = {time.time()}, got message = {received_input}\n")
            print(received_input)


def do_task():
    open(hard_path, 'w').close()
    queue = Queue()
    main_process_pipe_b, b_process_pipe = Pipe()
    a_process_pipe_b, b_process_pipe_a = Pipe()

    a = Process(target=fun_a, name="A", args=(queue, a_process_pipe_b,))
    b = Process(target=fun_b, name="B", args=(b_process_pipe, b_process_pipe_a))
    stdout_thread = threading.Thread(target=output, args=(main_process_pipe_b,))

    a.start()
    b.start()
    stdout_thread.start()

    while True:
        s = input()
        if s == "exit":
            break
        log(f"Main process: time = {time.time()}, input = {s}\n")
        queue.put(s)
        log(f"Main process: time = {time.time()}, message in queue = {s}\n")

    global is_running
    is_running = False
    a.terminate()
    b.terminate()
    a.join()
    b.join()
    stdout_thread.join()
