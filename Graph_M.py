class Graph_M:
    def __init__(self)->None:
        # string number->key value/
        self.vtcs={}  # name : sr no
        self.graph={}   #source :[ destination , distance ]
        self.vertx={}  #sr no: name 
    def addVertex(self,name):
        vts=len(self.vtcs)
        self.vtcs[name]=vts
        self.vertx[vts]=name
    def getAll_station(self):
        for i,j in self.vtcs.items():
            print(" SrNo ",j," Name : ",i)
    def addEdge(self,name1,name2,weight):
        if name1 not in self.graph:self.graph[name1]=[]
        if name2 not in self.graph:self.graph[name2]=[]
        self.graph[name1].append([name2,weight])   #city distance
        self.graph[name2].append([name1,weight])   #city distance
    def show_map(self):
        for i,j in self.graph.items():
            print(i,"=>")
            for city,distance in j:
                print("\t\t\t",city,"  ",distance)
            print()
    def get_Name(self,a):
        return self.vertx[a]
    def dijkstra(self,src1,src2):
        import heapq
        distance=[float('inf')]*(len(self.vtcs)+1)
        distance[self.vtcs[src1]]=0
        stack=[]
        heapq.heappush(stack,[0,src1])
        while(stack):
            dis,city=heapq.heappop(stack)
            if city==src2:return "Shortest path from "+src1+" to "+src2+" is "+str(dis)+" KM."
            for i,j in self.graph[city]:
                if dis+j<distance[self.vtcs[i]]:
                    distance[self.vtcs[i]]=dis+j
                    heapq.heappush(stack,[dis+j,i])
    def shortest_time(self,src1,src2):
        import heapq
        distance=[float('inf')]*(len(self.vtcs)+1)
        distance[self.vtcs[src1]]=0
        stack=[]
        heapq.heappush(stack,[0,src1])
        while(stack):
            dis,city=heapq.heappop(stack)
            if city==src2:return "Fare from "+src1+" to "+src2+" is "+str(dis)+" MIN."
            for i,j in self.graph[city]:
                if dis+j<distance[self.vtcs[i]]:
                    distance[self.vtcs[i]]=dis+j
                    heapq.heappush(stack,[dis+j,i])
        
    def print_path(self,src1,src2):
        def bfs(graph,parent,n,src1):
            def print_graph(parent,n,city,path):
                if city==-1:
                    print("Source:- ",end="")
                    for i in range(len(path)-1,-1,-1):
                        print(path[i],end=" -> ")
                    print("Destination")
                    print()
                    return
                for i in parent[self.vtcs[city]]:
                    print_graph(parent,n,i,path+[city])
            parent[self.vtcs[src1]].append(-1)
            distance=[float('inf')]*(n)
            distance[self.vtcs[src1]]=0
            from collections import deque
            q=deque()
            q.append(src1)
            while(q):
                city=q.popleft()
                for i,j in graph[city]:
                    if distance[self.vtcs[city]]+j<distance[self.vtcs[i]]:
                        parent[self.vtcs[i]].clear()
                        parent[self.vtcs[i]].append(city)
                        distance[self.vtcs[i]]=distance[self.vtcs[city]]+j
                        q.append(i)
                    elif distance[self.vtcs[city]]+j==distance[self.vtcs[i]]:
                        parent[self.vtcs[i]].append(city)
            print_graph(parent,n,src2,[])
        n=len(self.vtcs)+1
        parent=[[] for _ in range(n)]
        bfs(self.graph,parent,n,src1)
if __name__=="__main__": 
    g=Graph_M()
    g.addVertex("Noida Sector 62~B")
    g.addVertex("Botanical Garden~B")
    g.addVertex("Yamuna Bank~B")
    g.addVertex("Rajiv Chowk~BY")
    g.addVertex("Vaishali~B")
    g.addVertex("Moti Nagar~B")
    g.addVertex("Janak Puri West~BO")
    g.addVertex("Dwarka Sector 21~B")
    g.addVertex("Huda City Center~Y")
    g.addVertex("Saket~Y")
    g.addVertex("Vishwavidyalaya~Y")
    g.addVertex("Chandni Chowk~Y")
    g.addVertex("New Delhi~YO")
    g.addVertex("AIIMS~Y")
    g.addVertex("Shivaji Stadium~O")
    g.addVertex("DDS Campus~O")
    g.addVertex("IGI Airport~O")
    g.addVertex("Rajouri Garden~BP")
    g.addVertex("Netaji Subhash Place~PR")
    g.addVertex("Punjabi Bagh West~P")
    
    g.addEdge("Noida Sector 62~B", "Botanical Garden~B", 8)
    g.addEdge("Botanical Garden~B", "Yamuna Bank~B", 10)
    g.addEdge("Yamuna Bank~B", "Vaishali~B", 8)
    g.addEdge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
    g.addEdge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
    g.addEdge("Moti Nagar~B", "Janak Puri West~BO", 7)
    g.addEdge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
    g.addEdge("Huda City Center~Y", "Saket~Y", 15)
    g.addEdge("Saket~Y", "AIIMS~Y", 6)
    g.addEdge("AIIMS~Y", "Rajiv Chowk~BY", 7)
    g.addEdge("Rajiv Chowk~BY", "New Delhi~YO", 1)
    g.addEdge("New Delhi~YO", "Chandni Chowk~Y", 2)
    g.addEdge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
    g.addEdge("New Delhi~YO", "Shivaji Stadium~O", 2)
    g.addEdge("Shivaji Stadium~O", "DDS Campus~O", 7)
    g.addEdge("DDS Campus~O", "IGI Airport~O", 8)
    g.addEdge("Moti Nagar~B", "Rajouri Garden~BP", 2)
    g.addEdge("Punjabi Bagh West~P", "Rajouri Garden~BP", 2)
    g.addEdge("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)
    g.addEdge("Vaishali~B", "Shivaji Stadium~O", 1)
    
    print("****WELCOME TO THE METRO APP*****")
    while(True):
        print("LIST OF ACTIONS")
        print("1. LIST ALL THE STATIONS IN THE MAP")
        print("2. SHOW THE METRO MAP")
        print("3. GET SHORTEST DISTANCE FROM A 'SOURCE' STATION TO 'DESTINATION' STATION")
        print("4. GET FARE FROM A 'SOURCE' STATION TO 'DESTINATION' STATION")
        print("5. GET ALL SHORTEST PATH (DISTANCE WISE) TO REACH FROM A 'SOURCE' STATION TO 'DESTINATION' STATION")
        print("6. EXIT THE MENU")
        choice=input("\nENTER YOUR CHOICE FROM THE ABOVE LIST (1 to 7) : ")
        if int(choice)==1:
            g.getAll_station()
        elif int(choice)==2:
            g.show_map()
        elif int(choice)==3:
            g.getAll_station()
            print("1: SrNo as one below the other line")
            print("2: Name of source and destination one below the other line") 
            TemporaryChoice=int(input("\nEnter the choice(1 to 2)  "))
            if TemporaryChoice==1:
                source=g.get_Name(int(input()))
                destination=g.get_Name(int(input()))
            else:
                source=input()
                destination=input()
            print(g.dijkstra(source,destination))
            print()
        elif int(choice)==4:
            g.getAll_station()
            print("1: SrNo as one below the other line")
            print("2: Name of source and destination one below the other line") 
            TemporaryChoice=int(input("\nEnter the choice(1 to 2)  "))
            if TemporaryChoice==1:
                source=g.get_Name(int(input()))
                destination=g.get_Name(int(input()))
            else:
                source=input()
                destination=input()
            print(g.shortest_time(source,destination))
            print()
        elif int(choice)==5:
            g.getAll_station()
            print("1: SrNo as one below the other line")
            print("2: Name of source and destination one below the other line") 
            TemporaryChoice=int(input("\nEnter the choice(1 to 2)   "))
            if TemporaryChoice==1:
                source=g.get_Name(int(input()))
                destination=g.get_Name(int(input()))
            else:
                source=input()
                destination=input()
            g.print_path(source,destination)
        elif int(choice) == 6:break
        
            
            
        
         
    
            