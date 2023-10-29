import heapq
import random
import string
import networkx as nx
import matplotlib.pyplot as plt
from My_exceptions import My_exceptions

class Graph:
    graph = dict()
    graph_dijkstra = dict()
    nodes = []  # A, B, C...
    node_connections = []  # сколько ребер исхоит из данной вершины
    edges_weight = None  # матрица весов графа

    # Количество вершин, минимально количество ребер из вершин, максимальное количество ребер из вершин
    def graph_generator(self, number_of_nodes, min_number_of_edge_from_node, max_number_of_edge_from_node):
        self.nodes = [char for char in string.ascii_uppercase][:number_of_nodes]
        self.node_connections = [0] * len(self.nodes)
        self.edges_weight = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        # self.graph = {key: {} for key in self.nodes}

        edged_keys, edged_values = [], []
        while self.__check_correct_graph(min_number_of_edge_from_node):
            for i in range(len(self.nodes)):
                for j in range(i, len(self.nodes)):
                    if self.nodes[i] != self.nodes[j] and not str(self.nodes[i] + self.nodes[j]) in edged_keys:
                        if random.choice([True, False]):  # рандомный пропуск
                            break
                        # if self.__node_connections[i] == max_number_of_edge_from_node - min_number_of_edge_from_node\
                        #         or self.__node_connections[j] == max_number_of_edge_from_node - min_number_of_edge_from_node:
                        #     continue  # можно ли работать с данным ребром
                        self.node_connections[i] += 1
                        self.node_connections[j] += 1
                        print(self.node_connections)
                        print()
                        edged_keys.append(self.nodes[i] + self.nodes[j])  # Создаем ребра
                        edged_values.append(random.randint(10, 20))  # Создаем вес ребер
                        self.edges_weight[i][j] = edged_values[len(edged_values) - 1]
                        if self.node_connections[i] >= max_number_of_edge_from_node - 1\
                                or self.node_connections[j] >= max_number_of_edge_from_node - 1:
                            # Если достигли максимального количества ребер из вершины, заканчиваем работу
                            break
                            # тут костыль, условно из точки A оздали 4 ребра(максимум) AB, AC, AD, AF, а потом из точки D
                            # создали ребро в А, AD, вот их уже 5(больше максимума)
                            # костыль поправлен, проблема в ровном создании min=max
                        else:
                            if self.node_connections[i] < min_number_of_edge_from_node or \
                                    self.node_connections[j] < min_number_of_edge_from_node:
                                # Если не достигли минимального количества ребер из вершины, продолжаем
                                continue
                            elif random.choice([True, False]):  # Иначе роляем вероятность
                                break
        for edged_key, edged_value in zip(edged_keys, edged_values):
            self.graph_dijkstra.setdefault(edged_key[0], {}).update({edged_key[1]: edged_value})
            self.graph_dijkstra.setdefault(edged_key[1], {}).update({edged_key[0]: edged_value})

        self.graph = dict(zip(edged_keys, edged_values))
        print(self.graph)
        print()
        print(self.graph_dijkstra)
        self.__check_revers_keys(edged_keys)
        return self

    @staticmethod
    def __check_revers_keys(edged_keys):  # Проверка созданного графа на схожесть ключей пример: AB и BA это одно ребро
        for i in range(len(edged_keys)):
            for j in range(i, len(edged_keys)):
                if edged_keys[i] == edged_keys[j][::-1]:
                    print("Печаль, тоска", edged_keys[len(edged_keys) - 1], edged_keys[len(edged_keys) - 1][::-1])

    def __check_correct_graph(self, min_number_of_edge_from_node):
        for number_links in self.node_connections:
            if min_number_of_edge_from_node <= number_links:
                continue
            else:
                break
        else:
            return False
        return True

    def paintilovka(self):
        # рисуем граф
        draw_graph = nx.Graph()

        draw_graph.add_nodes_from(self.nodes)
        for key, value in self.graph.items():
            draw_graph.add_edge(key[0], key[1])

        pos = nx.spring_layout(draw_graph)
        nx.draw(draw_graph, pos=pos, with_labels=True)
        nx.draw_networkx_edge_labels(draw_graph, pos=pos, edge_labels={(key[0], key[1]): value for key, value in self.graph.items()}, font_color='red')

        plt.show()

    @staticmethod
    def solution_task_max_flow(object_graph):
        if not isinstance(object_graph, Graph):

            raise My_exceptions.Is_not_graph_error()
        # object_graph.paintilovka()  # Если хотим рисовать раскомментировать
        source = random.randint(0, len(object_graph.nodes) - 1)
        print(source)

        while(True):
            sink = random.randint(0, len(object_graph.nodes) - 1)
            print(sink)
            if source != sink:
                break

        # Функция для выполнения поиска в ширину (BFS)
        def bfs(graph, parent, source, sink):
            visited = [False] * len(graph)
            queue = []
            queue.append(source)
            visited[source] = True

            while queue:
                u = queue.pop(0)
                for ind, val in enumerate(graph[u]):
                    if visited[ind] == False and val > 0:
                        queue.append(ind)
                        visited[ind] = True
                        parent[ind] = u
                        if ind == sink:
                            return True

            return False

        # подготовка данных, обработка
        mas = object_graph.edges_weight
        print(*mas, sep="\n")
        print()
        for i in range(len(mas)):
            for j in range(i, len(mas)):
                mas[j][i] = mas[i][j]
        print(*mas, sep="\n")
        print()

        parent = [-1] * len(mas)
        max_flow = 0

        while bfs(mas, parent, source, sink):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, mas[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                mas[u][v] -= path_flow
                mas[v][u] += path_flow
                v = parent[v]

        return max_flow

    @staticmethod
    def dijkstra(object_graph):
        if not isinstance(object_graph, Graph):
            raise My_exceptions.Is_not_graph_error()
        graph_dijkstra = object_graph.graph_dijkstra
        start = random.choice(object_graph.nodes)
        # Инициализация
        distances = {vertex: float('inf') for vertex in graph_dijkstra}  # Расстояния до вершин
        distances[start] = 0  # Расстояние до начальной вершины
        queue = [(0, start)]  # Очередь с приоритетом (расстояние, вершина)

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)  # Извлечение вершины с наименьшим расстоянием

            # Пропустить вершину, если уже найдено более короткое расстояние
            if current_distance > distances[current_vertex]:
                continue

            # Обход соседних вершин
            for neighbor, weight in graph_dijkstra[current_vertex].items():
                distance = current_distance + weight  # Расстояние до соседней вершины через текущую

                # Если найдено более короткое расстояние, обновить
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))  # Добавить в очередь с приоритетом

        output = ""
        for key, value in distances.items():
            if key != start:
                output += start + "-->" + key + "==" + str(value) + "\n"

        return output.rstrip("\n")

