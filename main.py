from pseudorandom_number_generator import generate_random_numbers

# Queue parameters (G/G/S/K)
S = 2                    # Number of servers
K = 5                    # Total system capacity
ArrivalMin = 2.0         # Minimum inter-arrival time
ArrivalMax = 5.0         # Maximum inter-arrival time  
ServiceMin = 3.0         # Minimum service time
ServiceMax = 5.0         # Maximum service time
SimulationTime = 1000.0  # Total simulation time

GlobalTime = 0.0
Queue = 0 
ServersOccupied = 0 
NextArrivalTime = 2.0  # First arrival time
NextDepartureTime = float('inf')

times = [0.0] * (K + 1)
random_numbers = []
current_index = 0
LastEventTime = 0.0

def main():
    global GlobalTime, Queue, ServersOccupied, NextArrivalTime, NextDepartureTime, random_numbers, LastEventTime
    
    random_numbers = generate_random_numbers(100000)
    
    GlobalTime = 0.0
    Queue = 0
    ServersOccupied = 0
    NextArrivalTime = generate_arrival_time()
    NextDepartureTime = float('inf')
    
    print(f"Queue Simulator G/G/{S}/{K}")
    print("=" * 30)
    print(f"Uniform inter-arrival time: {ArrivalMin}-{ArrivalMax}")
    print(f"Uniform service time: {ServiceMin}-{ServiceMax}")
    print(f"Servers: {S}")
    print(f"Total system capacity: {K}")
    print("=" * 30)
    
    while GlobalTime < SimulationTime:
        event = NextEvent()

        # Calcular tempo decorrido desde o último evento e acumular no estado atual
        current_state = Queue + ServersOccupied
        next_event_time = min(NextArrivalTime, NextDepartureTime)
        time_in_state = next_event_time - LastEventTime
        if current_state <= K and time_in_state > 0:
            times[current_state] += time_in_state
        LastEventTime = next_event_time

        if event == "arrival":
            Arrival()
        elif event == "departure":
            Departure()

    print_statistics()

def NextEvent():
    global NextArrivalTime, NextDepartureTime
    
    if NextArrivalTime < NextDepartureTime:
        return "arrival"
    else:
        return "departure"

def Arrival():
    global GlobalTime, Queue, ServersOccupied, NextArrivalTime, NextDepartureTime
    
    GlobalTime = NextArrivalTime
    
    current_state = Queue + ServersOccupied
    # Removido: contabilização do tempo do estado aqui, pois agora é feito no loop principal
    
    print(f"Arrival at time {GlobalTime:.2f}, Queue: {Queue}, Servers occupied: {ServersOccupied}")
    
    if ServersOccupied < S:
        ServersOccupied += 1
        NextDepartureTime = GlobalTime + generate_service_time()
        print(f"  Server served immediately, Next departure: {NextDepartureTime:.2f}")
    else:
        if Queue < (K - S):
            Queue += 1
            print(f"  Client added to queue, Queue size: {Queue}")
        else:
            print(f"  Client lost (system full)")
    
    NextArrivalTime = GlobalTime + generate_arrival_time()

def Departure():
    global GlobalTime, Queue, ServersOccupied, NextDepartureTime
    
    GlobalTime = NextDepartureTime
    
    current_state = Queue + ServersOccupied
    # Removido: contabilização do tempo do estado aqui, pois agora é feito no loop principal
    
    print(f"Departure at time {GlobalTime:.2f}, Queue: {Queue}, Servers occupied: {ServersOccupied}")
    
    if Queue > 0:
        Queue -= 1
        NextDepartureTime = GlobalTime + generate_service_time()
        print(f"  Next client served, Next departure: {NextDepartureTime:.2f}")
    else:
        ServersOccupied -= 1
        if ServersOccupied > 0:
            NextDepartureTime = GlobalTime + generate_service_time()
            print(f"  Server released, Next departure: {NextDepartureTime:.2f}")
        else:
            NextDepartureTime = float('inf')
            print(f"  All servers are free")

def generate_arrival_time():
    global current_index, random_numbers
    if current_index < len(random_numbers):
        u = random_numbers[current_index]
        current_index += 1
        return ArrivalMin + u * (ArrivalMax - ArrivalMin)
    else:
        random_numbers.extend(generate_random_numbers(1000))
        u = random_numbers[current_index]
        current_index += 1
        return ArrivalMin + u * (ArrivalMax - ArrivalMin)

def generate_service_time():
    global current_index, random_numbers
    if current_index < len(random_numbers):
        u = random_numbers[current_index]
        current_index += 1
        return ServiceMin + u * (ServiceMax - ServiceMin)
    else:
        random_numbers.extend(generate_random_numbers(1000))
        u = random_numbers[current_index]
        current_index += 1
        return ServiceMin + u * (ServiceMax - ServiceMin)

def print_statistics():
    print("\n" + "=" * 50)
    print("FINAL STATISTICS")
    print("=" * 50)
    print(f"Total simulation time: {GlobalTime:.2f}")
    print(f"Configuration: G/G/{S}/{K}")
    print(f"Uniform inter-arrival time: {ArrivalMin}-{ArrivalMax}")
    print(f"Uniform service time: {ServiceMin}-{ServiceMax}")
    print("\nTime in each system state:")
    
    for i in range(K + 1):
        percentage = (times[i] / GlobalTime * 100) if GlobalTime > 0 else 0
        print(f"{i}: {times[i]:.2f} ({percentage:.2f}%)")

if __name__ == "__main__":
    main()