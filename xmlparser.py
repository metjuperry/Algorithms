from xml.dom import minidom


def add(_graph, node, neighbour, distance):
    try:
        _graph[node].update({neighbour: int(distance)})
    except KeyError:
        _graph[node] = {}
        _graph[node].update({neighbour: int(distance)})


def xml_to_dictionary(xml):
    table = []
    graph = {}

    xmldoc = minidom.parse(xml)
    rows = xmldoc.getElementsByTagName('Row')

    for each in range(0, len(rows)):
        table.append([])

    for x, row in enumerate(rows):
        cells = row.getElementsByTagName('Cell')
        for y, cell in enumerate(cells):
            value = cell.childNodes[0].nodeValue
            table[x].append(str(value))

    for i, item in enumerate(table[0]):
        for data in range(1, len(table)):
            if table[data][i + 1] != '-':
                add(graph, item, table[data][0], table[data][i + 1])

    return graph

print xml_to_dictionary('table.xml')
