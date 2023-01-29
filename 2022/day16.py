with open('test16.txt', 'r') as file:
    valve_info = file.read()


valve_info = valve_info.split('\n')[:-1]
valves = {}

valves_to_open = set()
for valve in valve_info:
    valve, tuns = valve.split('; ')
    valve = valve.split(' ')
    valve_name, valve_rate = valve[1], int(valve[-1].split('=')[-1])
    tuns = [x.strip(', ') for x in tuns.split(' ')[4:]]
    valves[valve_name] = [valve_rate, tuns]
    valves_to_open.add(valve_name) if valve_rate != 0 else None

valves_to_open = frozenset(valves_to_open)
print(len(valves_to_open))
max_so_far = 0
seen = {}
open_valves = set()
def find_optimal(node, time, flow):
    #print(time)
    global max_so_far
    if seen.get((node, time), -1) >= flow:
        return
    seen[(node, time)] = flow
    if time == 1:
        max_so_far = max(max_so_far, flow)
        return
    net_flow = sum(valves[valve][0] for valve in open_valves)
    if valves[node][0] != 0 and node not in open_valves:
        open_valves.add(node)
        flow2 = valves[node][0]
        find_optimal(node, time-1, flow + net_flow + flow2)
        open_valves.remove(node)
    for valve in valves[node][1]:
        find_optimal(valve, time-1, flow + net_flow)


def find_optimal_with_elephant(node, time, flow, e_node):
    #print(time)
    global max_so_far
    if seen.get((node, time, e_node), -1) >= flow:
        return
    seen[(node, time, e_node)] = flow
    if time == 0:
        max_so_far = max(max_so_far, flow)
        return
    flow += sum(valves[valve][0] for valve in open_valves)

    # if vall valves open, chill
    if len(open_valves) == len(valves_to_open):
        find_optimal_with_elephant(node, time-1, flow, e_node)
        return

    # I could open valve
    if valves[node][0] != 0 and node not in open_valves:
        open_valves.add(node)
        flow2 = valves[node][0]
#        find_optimal_with_elephant(node, time-1, flow + flow2, e_node)
        # Elephant can open valve
        if valves[e_node][0] != 0 and e_node not in open_valves:
            open_valves.add(e_node)
            flow3 = valves[e_node][0]
            find_optimal_with_elephant(node, time-1, flow + flow2 + flow3, e_node)
            open_valves.remove(e_node)
        # Elephant can move
        for e_valve in valves[e_node][1]:
            find_optimal_with_elephant(node, time-1, flow + flow2, e_valve)
        open_valves.remove(node)
    # I could move
    for valve in valves[node][1]:
        # Elephant can open valve
        if valves[e_node][0] != 0 and e_node not in open_valves:
            open_valves.add(e_node)
            flow4 = valves[e_node][0]
            find_optimal_with_elephant(valve, time-1, flow + flow4, e_node)
            open_valves.remove(e_node)
        # Elephant can move
        for e_valve2 in valves[e_node][1]:
            find_optimal_with_elephant(valve, time-1, flow, e_valve2)
 

print(valves)
#print(seen)
#find_optimal('AA', 30, 0)
find_optimal_with_elephant('AA', 26, 0, 'AA')
print(max_so_far)

