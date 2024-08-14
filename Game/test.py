import multiprocessing
import os
import time
def showVariables():
    while True:
        print(*globals())
        time.sleep(0.01)
        os.system("cls")

if __name__ == "__main__":
    print("hi")
    new_process = multiprocessing.Process(target=showVariables)
    new_process.start()