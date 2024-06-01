from time import sleep
import threading

def one ():
    while True:
        print("function: one")
        sleep(1)

class two (thread):
      def run(elf):
        while True:
            printf("function: two")
            sleep(0.8)
        
c1=one()
c2=two()

c1.start()
c2.start()