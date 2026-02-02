import random
import math

# -----------------------------
# Parameters (EDIT THESE)
# -----------------------------
LAMBDA = 4.0   # arrival rate λ (customers per unit time)
MU = 6.0       # service rate μ (customers per unit time)
SIM_TIME = 10000  # total simulation time

# -----------------------------
# State variables
# -----------------------------
clock = 0.0
num_in_system = 0
next_arrival = random.expovariate(LAMBDA)
next_departure = math.inf

# Statistics
total_wait_time = 0.0
total_system_time = 0.0
num_customers_served = 0
area_num_in_system = 0.0
last_event_time = 0.0

# Queue to store arrival times
queue = []

# -----------------------------
# Simulation loop
# -----------------------------
while clock < SIM_TIME:
    if next_arrival < next_departure:
        # ARRIVAL EVENT
        clock = next_arrival
        area_num_in_system += num_in_system * (clock - last_event_time)
        last_event_time = clock

        num_in_system += 1
        queue.append(clock)

        # Schedule next arrival
        next_arrival = clock + random.expovariate(LAMBDA)

        # If server idle, schedule departure
        if num_in_system == 1:
            next_departure = clock + random.expovariate(MU)

    else:
        # DEPARTURE EVENT
        clock = next_departure
        area_num_in_system += num_in_system * (clock - last_event_time)
        last_event_time = clock

        num_in_system -= 1
        arrival_time = queue.pop(0)

        system_time = clock - arrival_time
        total_system_time += system_time
        num_customers_served += 1

        # Schedule next departure if queue not empty
        if num_in_system > 0:
            next_departure = clock + random.expovariate(MU)
        else:
            next_departure = math.inf

# -----------------------------
# Results
# -----------------------------
L_sim = area_num_in_system / clock
W_sim = total_system_time / num_customers_served

print("---- M/M/1 Simulation Results ----")
print(f"λ = {LAMBDA}, μ = {MU}")
print(f"Simulated L (avg in system) = {L_sim:.3f}")
print(f"Simulated W (avg time in system) = {W_sim:.3f}")

# Theoretical values for comparison
rho = LAMBDA / MU
L_theory = rho / (1 - rho)
W_theory = 1 / (MU - LAMBDA)

print("\n---- Theoretical M/M/1 Results ----")
print(f"ρ = {rho:.3f}")
print(f"Theoretical L = {L_theory:.3f}")
print(f"Theoretical W = {W_theory:.3f}")
