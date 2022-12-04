input_file = open('day3_dummyinput.txt')
input_file = open('day3_input.txt')

input = list(input_file.read())

locations_visited = set()

current_location = (0,0)
locations_visited.add(current_location)

def process_location(direction, curr):
    # new_location = (0,0)
    if direction == '^':
        new_location = (curr[0], curr[1] + 1)
    elif direction == 'v':
        new_location = (curr[0], curr[1] - 1)
    elif direction == '>':
        new_location = (curr[0] + 1, curr[1])
    else:
        new_location = (curr[0] - 1, curr[1])
    return new_location


for d in input:
    current_location = process_location(d, current_location)
    locations_visited.add(current_location)
    # print(d, current_location, len(locations_visited))

print("Part 1:", len(locations_visited))

locations_visited = set()
current_location_santa = (0,0)
current_location_robo = (0,0)

for i in range(len(input)):
    if i % 2 == 0:
        # santa
        current_location_santa = process_location(input[i], current_location_santa)
        locations_visited.add(current_location_santa)
    else:
        # robo
        current_location_robo = process_location(input[i], current_location_robo)
        locations_visited.add(current_location_robo)


print("Part 2:", len(locations_visited))