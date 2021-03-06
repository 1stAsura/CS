import math
from min_heap import Element, MinHeap

class GNode:
    def __init__(self, vertex=None, weight=None):
        self.vertex=vertex
        self.weight=weight
        self.link=None

class Edge:
    def __init__(self, v1, v2, weight):
        self.v1=v1
        self.v2=v2
        self.weight=weight

class Graph:
    def __init__(self):
        self.adjacency_list=[]
        self.edge_list=[]

        self.vertex_num=0

    def add_vertex(self, vnum=1):
        self.adjacency_list.extend([None for _ in range(vnum)])
        self.vertex_num+=vnum
    
    def __add_node(self, vertex, node):
        cur=self.adjacency_list[vertex]
        if not cur:
            self.adjacency_list[vertex]=node
        else:
            while cur.link:
                cur=cur.link
            cur.link=node

    def insert_edge(self, u, v, weight):
        unode=GNode(u, weight)
        vnode=GNode(v, weight)

        self.__add_node(u, vnode)
        self.__add_node(v, unode)

        self.edge_list.append(Edge(u, v, weight))

    def get_min_v(self, w):
        _min=math.inf
        min_v=None
        for i in range(self.vertex_num):
            if w[i] < _min:
                _min=w[i]
                min_v=i
        return min_v

    def MST_prim1(self):
        #TE={}
        mst=Graph(); mst.add_vertex(self.vertex_num)
        #TV={}
        TV=set()

        w=[math.inf for _ in range(self.vertex_num)]
        _from=[None for _ in range(self.vertex_num)]

        w[0]=0
        #|TV| < |V|
        while len(TV) < self.vertex_num:
            v=self.get_min_v(w)
            #TV <- TV U {v}
            TV.add(v)
            #TE <- TE U {(v, from[v])}
            if _from[v]!=None:
                mst.insert_edge(v, _from[v], w[v])
            #trick
            w[v]=math.inf
            #u adjacent to v
            u=self.adjacency_list[v]
            while u:
                if u.vertex not in TV and u.weight < w[u.vertex]:
                    w[u.vertex]=u.weight
                    _from[u.vertex]=v
                u=u.link
        return mst

    def MST_prim2(self):
        #최종적으로 만들어질 MST
        mst=Graph(); mst.add_vertex(self.vertex_num)
        #TV={} : MST 정점의 집합, 시작 노드부터 하나씩 채워나간다
        TV=set()

        #w_list : 각 정점의 w 값을 담아두기 위한 배열
        w_list=[None for _ in range(self.vertex_num)]
        #min heap에 w와 from을 가진 정점을 담아둔다
        #heap 초기화 : w->inf, from->None
        h=MinHeap()
        for i in range(1, self.vertex_num):
            w_list[i]=math.inf
            h.push(Element(i, math.inf, None))
        #시작 노드인 0은 w->0, from->None
        w_list[0]=0
        h.push(Element(0, 0, None))

        while not h.is_empty():
            #가중치가 가장 작은 에지 (from, v) : w
            #정보를 가진 정점 Element v
            v=h.pop()
            #TV에 정점을 추가
            TV.add(v.v)
            #TE에 에지 추가
            if v._from != None:
                mst.insert_edge(v.v, v._from, v.w)
            
            #TV에 정점이 추가되면 인접 정점 중 
            #트리 밖에 있는 정점에 대해 업데이트 시도
            #u는 새로 추가된 정점 v에 인접한 정점 노드
            u=self.adjacency_list[v.v]
            while u:
                #u가 트리 밖의 정점이고
                #기존 w 값보다 w(u, v)이 작다면 업데이트
                if u.vertex not in TV and u.weight < w_list[u.vertex]:
                    #w_list 업데이트
                    w_list[u.vertex]=u.weight
                    h.decrease_weight(Element(u.vertex, u.weight, v.v))
                u=u.link

        return mst

    def print_edges(self):
        for edge in self.edge_list:
            print("({}, {}) : {}".format(edge.v1, edge.v2, edge.weight))

if __name__=="__main__":
    g=Graph()
    g.add_vertex(6)

    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 2)
    g.insert_edge(0, 3, 8)
    g.insert_edge(1, 2, 5)
    g.insert_edge(1, 4, 12)
    g.insert_edge(2, 3, 7)
    g.insert_edge(2, 4, 17)
    g.insert_edge(3, 4, 4)
    g.insert_edge(3, 5, 14)

    #mst=g.MST_prim1()
    mst=g.MST_prim2()

    mst.print_edges()
    
