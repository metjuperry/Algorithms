import tkMessageBox
from Tkinter import *
from idlelib.ToolTip import ListboxToolTip

from algorithm import *

mode = 0
paths = {}

resultpath = "None"
resultdist = 0


# ------------------------------------

def isnumber(char):
    try:
        int(char) + 1 - 1
    except ValueError:
        return False
    return True


def addbox():
    print "Added"

    frame = Frame(entries)
    frame.pack()

    ent1 = Entry(frame, width=5)
    ent1.grid(row=1, column=0)

    ent2 = Entry(frame, width=5)
    ent2.grid(row=1, column=1)

    all_entries.append((ent1, ent2))


def delbox():
    all_entries.pop()[0].master.pack_forget()


# ------------------------------------


def late():
    global mode
    mode = 0
    subHeader.config(text="Now using Lateness Algorithm")
    left.config(text="Process. time")
    right.config(text="Deadline")
    print mode


def john():
    global mode
    mode = 1
    subHeader.config(text="Now using Johnson's Algorithm")
    left.config(text="PT M1")
    right.config(text="PT M2")
    print mode


def djik():
    global mode
    mode = 2
    subHeader.config(text="Now using Dijkstra's Algorithm")
    left.config(text=" ")
    right.config(text=" ")

    window = Toplevel(root)
    GraphicD(window)
    print mode


def sales():
    global mode
    mode = 3
    subHeader.config(text="Now using Traveling salesman Algorithm")
    left.config(text=" ")
    right.config(text=" ")

    window = Toplevel(root)
    GraphicD(window)
    print mode


def color():
    global mode
    mode = 4
    subHeader.config(text="Now using coloring Algorithm")
    left.config(text=" ")
    right.config(text=" ")

    window = Toplevel(root)
    GraphicC(window)
    print mode


# ------------------------------------
def dijkstra(graph, src, dest, visited=None, distances=None, predecessors=None):
    # calculates a shortest path tree routed in src
    global resultpath
    global resultdist
    # a few sanity checks
    if visited is None:
        visited = []
    if predecessors is None:
        predecessors = {}
    if distances is None:
        distances = {}
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')
        # ending condition
    if src == dest:
        # We build the shortest path and display it
        path = []
        pred = dest
        while pred is not None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        resultpath = str(list(reversed(path)))
        resultdist = str(distances[dest])
        print "Done"
    else:
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijkstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


# ------------------------------------

def getEntries():
    global entries_numerated
    entries_numerated = []
    res = 0
    for number, (ent1, ent2) in enumerate(all_entries):
        try:
            small = [int(ent1.get()), int(ent2.get())]
        except ValueError:
            tkMessageBox.showinfo('Error message', "You are supposed to input numbers")
            return False
        entries_numerated.append(small)

    if mode == 0:
        res = lateness(entries_numerated)
    elif mode == 1:
        res = johnson(entries_numerated)
    elif mode == 2:
        last = str(len(paths))
        first = str(paths.keys()[0])
        dijkstra(paths, first, last)
        res = resultpath
    elif mode == 3:
        try:
            res = salesman(paths)[0]
        except ValueError:
            res = "All nodes must be connected"
        except KeyError:
            res = "Something went wrong..."
    elif mode == 4:
        mapa_colored = color_algor(paths)
        mapa_list = sort_dictionary(mapa_colored)

        res = ""

        for number, colour in enumerate(mapa_list):
            res = str(res) + str(str((number + 1)) + ":" + mapa_colored[colour])
            res = str(res) + " "

    if mode == 4:
        outro.config(outro.config(text="The colors are: ", font=("Helvetica", 28)))
    else:
        outro.config(outro.config(text="The correct order is: ", font=("Helvetica", 28)))
    result.config(text=res, font=("Helvetica", 28))
    if mode == 2:
        dijk.config(text="(this path is " + str(resultdist) + " long)")
    elif mode == 3:
        dijk.config(text="(the path(s) is/are " + str(salesman(paths)[1]) + " long)")
    else:
        dijk.config(text=" ")

# ------------------------------------


class GraphicC:
    def __init__(self, master):
        self.node = StringVar(value=0)  # Creating the variables that will get the user's input.
        self.neigh = StringVar(value=0)
        self.dist = StringVar(value=1)
        self.sym = BooleanVar(value=True)
        self.lines = BooleanVar(value=False)

        master.title("How do they connect?")

        self.label_1 = Label(master, text="Source node:")
        self.label_2 = Label(master, text="Who is it's neighbour?")

        self.entry_1 = Entry(master, textvariable=self.node)
        self.entry_2 = Entry(master, textvariable=self.neigh)

        self.label_1.grid(row=1)
        self.label_2.grid(row=3)

        self.entry_1.grid(row=2, column=0)
        self.entry_2.grid(row=4, column=0)

        self.but1 = Button(master, text="Add to table",
                           command=lambda: addtograph(self.node.get(),
                                                      self.neigh.get(),
                                                      self.dist.get(),
                                                      self.sym.get()))
        self.but2 = Button(master, text="Save and exit", command=lambda: createGraph(self.lines.get()))
        self.but4 = Label(master, text="?", fg="blue", font=("Helvetica", 28))

        ListboxToolTip(self.but4, ["How to use: ",
                                   "Source node : 1",
                                   "Neighbour: 2",
                                   "(Use numbers, not letters)"])
        master.update()

        self.but1.grid(row=7, column=0)
        self.but2.grid(row=2, column=1)
        self.but4.grid(row=7, column=1)

        def addtograph(node, neighbour, distance, sym):
            if not isnumber(node) or not isnumber(neighbour):
                tkMessageBox.showinfo('Error message', "Read the rules (blue ?) again")
                return paths

            try:
                paths[node].update({neighbour: int(distance)})
            except KeyError:
                paths[node] = {}
                paths[node].update({neighbour: int(distance)})
            except ValueError:
                tkMessageBox.showinfo('Error message', "Distance has to be a number, obviously")
                return paths
            if sym:
                try:
                    paths[neighbour].update({node: int(distance)})
                except KeyError:
                    paths[neighbour] = {}
                    paths[neighbour].update({node: int(distance)})
            print(paths)

        def createGraph(lines):
            canvass = Canvas(root)
            canvass.pack(fill=BOTH, expand=YES)

            get_graph(paths, canvass, lines)

            master.destroy()


class GraphicD(GraphicC):
    def __init__(self, master):
        GraphicC.__init__(self, master)
        self.dist = StringVar(value=0)
        self.lines = BooleanVar(value=True)

        master.title("Make a graph")

        self.label_3 = Label(master, text="What is the distance?")
        self.entry_3 = Entry(master, textvariable=self.dist)

        self.label_3.grid(row=5)
        self.entry_3.grid(row=6, column=0)

        ListboxToolTip(self.but4, ["How to use: ",
                                   "For example: AB - 100",
                                   "Source node : 1",
                                   "Neighbour: 2",
                                   "Distance: 100",
                                   "(Use numbers, not letters)"])
        master.update()

        self.but4 = Checkbutton(master, text="Is Symetrical?", variable=self.sym, onvalue=True, offvalue=False)
        self.but4.grid(row=3, column=1)

        self.but2.grid(row=2, column=1)


# -------------------------------------

all_entries = []
entries_numerated = []

root = Tk()
root.geometry("500x650")

# ---------Menus and sub menus----------------

menu = Menu(root)
root.title("Algorithms")
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Algorithm", menu=subMenu)
subMenu.add_command(label="Lateness Algorithm", command=late)
subMenu.add_command(label="Johnson's Algorithm", command=john)
subMenu.add_command(label="Dijkstra's Algorithm", command=djik)
subMenu.add_command(label="Traveling Salesman", command=sales)
subMenu.add_command(label="Shape coloring", command=color)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

top = Frame(root)
top.pack()

# ----------Labels and texts--------------

Header = Label(top, text="Algorithms", font=("Helvetica", 28))
Header.pack(side=TOP)

subHeader = Label(top, text="Now using Lateness Alg.", )
subHeader.pack(side=BOTTOM)

showButton = Button(root, text='Calculate', command=getEntries)
showButton.pack(side=BOTTOM)

dijk = Label(root, text=" ")
dijk.pack(side=BOTTOM)

result = Label(root, text=" ")
result.pack(side=BOTTOM)

outro = Label(root, text=" ")
outro.pack(side=BOTTOM)

# ------------Buttons----------------

delBoxButton = Button(root, borderwidth=0, command=delbox)

photoM = PhotoImage(file="minus.gif")
delBoxButton.config(image=photoM)

delBoxButton.pack(side=BOTTOM)

addBoxButton = Button(root, borderwidth=0, command=addbox)

photoP = PhotoImage(file="plus.gif")
addBoxButton.config(image=photoP)

addBoxButton.pack(side=BOTTOM)

# ------------Column names---------------

labels = Frame(root)
labels.pack()

left = Label(labels, text="Pro. time", font=("Helvetica", 20))
left.grid(row=1, column=0, padx=4)

right = Label(labels, text="Deadline", font=("Helvetica", 20))
right.grid(row=1, column=1, padx=4)

entries = Frame(root)
entries.pack()

root.mainloop()
