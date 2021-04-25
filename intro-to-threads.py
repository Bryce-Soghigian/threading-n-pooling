from threading import Thread
"""
Threads allow our code to go from brrrrrrr
to a slightly more pleasing
prrrr
"""
def function_with_da_threading(arg):
    for i in range(arg):
        print("Python thread test")


if __name__ == "__main__":
    thread = Thread(target = function_with_da_threading,args=(3,))
    thread.start()
    thread.join()
    print("Exiting our thread :)")