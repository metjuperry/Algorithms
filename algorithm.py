tableD = [[2, 3],
          [4, 5],
          [2, 6],
          [2, 6],
          [3, 7],
          [1, 8]]

tableJ = [[4, 5],
          [4, 1],
          [10, 4],
          [6, 10],
          [2, 3]]

tableL1 = [[10, 8],
           [9, 7],
           [8, 9],
           [8, 12]]

pathes = {'1': {'3': 4, '2': 5, '5': 6, '4': 3},
          '2': {'1': 5, '3': 6, '5': 1, '4': 2},
          '3': {'1': 4, '2': 6, '5': 4, '4': 3},
          '4': {'1': 3, '3': 3, '2': 2, '5': 5},
          '5': {'1': 6, '3': 4, '2': 1, '4': 5}}

testpathes = {'1': {'3': 80, '2': 100},
              '2': {'1': 100, '5': 80, '4': 140, '6': 120},
              '3': {'1': 80, '5': 130, '4': 150, '6': 190},
              '4': {'8': 250, '3': 150, '2': 140, '7': 200},
              '5': {'8': 180, '3': 130, '2': 80, '7': 200},
              '6': {'8': 110, '3': 190, '2': 120, '7': 150},
              '7': {'9': 120, '5': 200, '4': 200, '6': 150},
              '8': {'9': 130, '5': 180, '4': 250, '6': 110},
              '9': {'8': 130, '7': 120}}

test_color = {'11': {'9': 1, '10': 1},
              '10': {'9': 1, '8': 1, '11': 1},
              '1': {'3': 1, '2': 1, '4': 1},
              '3': {'1': 1, '2': 1, '5': 1, '4': 1, '6': 1},
              '2': {'1': 1, '3': 1, '5': 1},
              '5': {'9': 1, '8': 1, '3': 1, '2': 1, '6': 1},
              '4': {'1': 1, '6': 1, '3': 1, '7': 1},
              '7': {'8': 1, '4': 1, '6': 1},
              '6': {'8': 1, '3': 1, '5': 1, '7': 1, '4': 1},
              '9': {'11': 1, '8': 1, '5': 1, '10': 1},
              '8': {'10': 1, '5': 1, '7': 1, '6': 1, '9': 1}}


# --------------End of test cases------------------


def lateness(arr):
    # This is the algorithm for the first task. It returns the order in least tardiness and lateness
    ordered = []
    rest = []
    endofs = 0
    for i in range(0, len(arr)):
        endofs += arr[i][0]
        if arr[i][1] >= endofs:
            ordered.append(i + 1)
        else:
            endofs -= arr[i][0]
            rest.append(i + 1)

    for m in rest:
        ordered.append(m)
    return ordered


# ------------------------------------


def removekey(d, key):
    # Removes a key from a dictionary. Changes the dictionary itself
    r = dict(d)
    del r[key]
    return r


def removeall(graph, number):
    # Anihilates every mention of the number in the records
    for thing in graph:
        try:
            graph[thing] = removekey(graph[thing], number)
        except KeyError:
            continue
    return graph


# ------------------------------------


def sumlist(graph):
    # Takes a list of lists, sums the numbers in the sub lists and returns a list with results
    suma = 0
    for trial in graph:
        for numb in trial:
            suma += numb
        trial[:] = []
        trial.append(suma)
        suma = 0
    return graph


# ------------------------------------


def minimum(arr):
    # Finds the minimal value in a 2D list and returs it's coordinates
    mini = 100
    x = 0
    y = 0
    for i in range(0, len(arr)):
        if mini > min(arr[i]):
            mini = min(arr[i])
            x = i
            if arr[i][0] == mini:
                y = 0
            else:
                y = 1
    return x, y


# ------------------------------------


def johnson(arr):
    original = []
    for i in arr:
        original.append(i)
    final = []
    front = 0
    helper = 0
    # Johnsons algorithm: if the smalest time is on the right, add it from the back, else add it from the front
    for i in range(0, len(arr)):
        back = len(final)
        mini = minimum(arr)
        tup = arr[mini[0]]
        numb = original.index(tup)

        if mini[1] == 0:
            final.insert(front, numb + 1)
            front += 1
            arr.pop(mini[0])

        elif mini[1] == 1:
            final.insert((back - helper), numb + 1)
            helper += 1
            arr.pop(mini[0])
    return final


# ------------------------------------


def salesman(graph):
    # Pseudo code:
    # 1. Select a random city.
    # 2. Find the nearest unvisited city and go there.
    # 3. Are there any unvisitied cities left? If yes, repeat step 2.
    # 4. Return to the first city.

    # But actually not random but start at each

    calc = 0
    result_path = []
    result_dist = []
    final = []
    alt_graph = dict(graph)
    for node in graph:
        result_path.append([])
        result_dist.append([])
        result_path[calc].append(node)

        curr_node = node
        while alt_graph is not None:
            prev_node = curr_node
            try:
                curr_node = min(alt_graph[curr_node], key=alt_graph[curr_node].get)
                result_dist[calc].append(alt_graph[prev_node][curr_node])
            except ValueError:
                break
            alt_graph = removeall(alt_graph, prev_node)
            alt_graph = removekey(alt_graph, prev_node)

            result_path[calc].append(curr_node)
        alt_graph = dict(graph)
        result_dist[calc].append(alt_graph[curr_node][node])
        calc += 1

    result_dist = sumlist(result_dist)
    for result in range(0, len(result_dist)):
        if result_dist[result] == min(result_dist):
            final.append(result_path[result])
    return final, min(result_dist)


# ------------------------------------


def tocolumns(graph):
    # Pseudo code:
    # 1. Select a node and add it to the column
    # 2. Check it's neighbours
    # 3. If the neighbour is already in a column, skip it, else add it to the next one

    columns = []
    visited = []
    used = 0
    for node in graph:
        columns.append([])
        if node not in visited:
            columns[used].append(node)
            visited.append(node)
            columns.append([])
        for neighbour in graph[node]:
            if neighbour not in visited:
                columns[used + 1].append(neighbour)
                visited.append(neighbour)
        used += 1
    semiresult = [x for x in columns if x != []]
    result = []

    for sublist in semiresult:
        result.append(sorted(sublist))

    return result


def nextcol(coord):
    coord = (coord[0] + 60, coord[1])
    return coord


def nextrow(coord, row):
    coord = (coord[0], coord[1] + row * 40)
    return coord


def get_graph(graph, canvas, lines):
    row_graph = 0
    coords_x = (20, 20)
    coords_y = (40, 40)

    connect_dict = {}

    box_graph = tocolumns(graph)

    for column in box_graph:
        for row in column:
            coords_x = nextrow(coords_x, row_graph)
            coords_y = nextrow(coords_y, row_graph)

            # noinspection PyUnusedLocal
            box = canvas.create_rectangle(coords_x, coords_y)
            connect_dict[row] = [coords_x, coords_y]

            # noinspection PyUnusedLocal
            label = canvas.create_text(coords_x[0] + 10, coords_x[1] + 10, text=str(row))

            coords_x = (coords_x[0], 20)
            coords_y = (coords_y[0], 40)
            row_graph += 1
        row_graph = 0

        coords_x = nextcol(coords_x)
        coords_y = nextcol(coords_y)

    already_connected = []
    for rectangle in sorted(graph):
        already_connected.append(rectangle)
        rec_coords = (connect_dict[rectangle][0][0] + 20, connect_dict[rectangle][0][1] + 10)
        for neighbour in graph[rectangle]:
            neig_coords = (connect_dict[neighbour][0][0], connect_dict[neighbour][0][1] + 10)
            if neighbour not in already_connected:
                # noinspection PyUnusedLocal
                line = canvas.create_line(rec_coords, neig_coords)

                if lines:
                    # noinspection PyUnusedLocal
                    distance = canvas.create_text(rec_coords[0] + (neig_coords[0] - rec_coords[0]) / 3,
                                                  rec_coords[1] + (neig_coords[1] - rec_coords[1]) / 3,
                                                  text=str(graph[rectangle][neighbour]),
                                                  font=("Helvetica", 10),
                                                  fill="red")


# this point is coords_x[0], coords_x[1] + 10 -> [] <-- and this point is coords_y[0], coords_y[1] - 10

# ------------------------------------


def sort_dictionary(graph):
    sort_graph = []
    for i in graph:
        sort_graph.append(int(i))
    sort_graph = sorted(sort_graph)

    for i, x in enumerate(sort_graph):
        sort_graph[i] = str(x)
    return sort_graph


def color_algor(graph):
    colors = ["red", "blue", "yellow", "green"]
    colored_graph = {}

    for i in sort_dictionary(graph):
        for neighbour in graph[i]:
            if neighbour in colored_graph:
                if colored_graph[neighbour] == "red":
                    try:
                        colors.remove("red")
                    except ValueError:
                        pass
                if colored_graph[neighbour] == "blue":
                    try:
                        colors.remove("blue")
                    except ValueError:
                        pass
                if colored_graph[neighbour] == "yellow":
                    try:
                        colors.remove("yellow")
                    except ValueError:
                        pass
                if colored_graph[neighbour] == "green":
                    try:
                        colors.remove("green")
                    except ValueError:
                        pass
        colored_graph.update({i: colors[0]})
        colors = ["red", "blue", "yellow", "green"]
    return colored_graph
