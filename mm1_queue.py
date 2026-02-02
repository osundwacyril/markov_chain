import simpy
import random
import statistics

# -----------------------------
# Parameters
# -----------------------------
LAMBDA = 4.0   # arrival rate λ
MU = 6.0       # service rate μ
SIM_TIME = 10000

# -----------------------------
# Customer process
# -----------------------------
def customer(env, name, server, service_rate, results):
    arrival_time = env.now

    with server.request() as request:
        yield request
        service_time = random.expovariate(service_rate)
        yield env.timeout(service_time)

        departure_time = env.now
        system_time = departure_time - arrival_time
        results.append(system_time)

# -----------------------------
# Arrival process
# -----------------------------
def arrival_process(env, server, arrival_rate, service_rate, results):
    i = 0
    while True:
        interarrival = random.expovariate(arrival_rate)
        yield env.timeout(interarrival)
        i += 1
        env.process(customer(env, f"Cust-{i}", server, service_rate, results))

# -----------------------------
# Main simulation
# -----------------------------
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)  # M/M/1 → 1 server
results = []

env.process(arrival_process(env, server, LAMBDA, MU, results))
env.run(until=SIM_TIME)

# -----------------------------
# Results
# -----------------------------
W_sim = statistics.mean(results)

rho = LAMBDA / MU
W_theory = 1 / (MU - LAMBDA)

print("---- SimPy M/M/1 Results ----")
print(f"λ = {LAMBDA}, μ = {MU}")
print(f"Simulated W (time in system) = {W_sim:.3f}")
print(f"Theoretical W = {W_theory:.3f}")
print(f"Utilization ρ = {rho:.3f}")
