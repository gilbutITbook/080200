import threading
import queue
import time

q = queue.Queue()
orders_done = False

def order_service():
    global orders_done
    for i in range(1, 11):
        food_number = int(input(f"{i} 번째 주문 음식을 고르세요(1: 피자, 2~:치킨) : "))
        prefix = str(i) + " 번째 음식 "
        message = prefix + '피자' if food_number == 1 else prefix + '치킨'
        q.put(message)
        thread_name = threading.current_thread().name
        print(f'[{thread_name}] : {message} 주문 완료')
    q.join()
    print('모든 주문 처리 완료')
    orders_done = True

def cooking_service():
    while True:
        try:
            message = q.get(timeout=5)
            thread_name = threading.current_thread().name
            print(f'[{thread_name}] : {message} 요리 시작')
            time.sleep(10)
            print(f'[{thread_name}] : {message} 요리 완성')
            q.task_done()
        except queue.Empty:
            if orders_done:
                break
            else:
                continue
        
services = []
services.append(threading.Thread(target=order_service, name="order_service"))
for i in range(1, 4):
    cooking_service_name = "coocking_service " + str(i)
    services.append(threading.Thread(target=cooking_service, name=cooking_service_name))

for service in services:
    service.start()
