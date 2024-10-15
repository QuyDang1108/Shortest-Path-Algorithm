import pygame
from maze import SearchSpace, Node 
from const import RED, BLUE, RES, GREY
from collections import deque

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')
    open_set = [g.start.id]  #tạo mảng open_set với giá trị ban đầu là node bắt đầu (các mảng đều chứa id node chứ không chứa node) 
    closed_set = [] # chưa có node nào được duyệt nên tạo nó rỗng
    father = [-1] * g.get_length() # tạo tất cả các id node cha là -1, sau này cập nhật dần, node bắt đầu có id node cha là -1

    while open_set: # chạy đến khi mảng open_set rỗng
        current_node_id = open_set.pop()  # lấy id node cuối cùng trong mảng open_set
        current_node = g.grid_cells[current_node_id] # lấy node tương ứng với id
        closed_set.append(current_node_id) # thêm id của node này vào cuối danh sách đã được duyệt 

        if current_node_id == g.goal.id: # nếu đã tìm được tới đích thì tiến hành xây dụng đường đi (khối lệnh này không thay đổi trong 4 thuật toán) 
            path = [current_node] # tạo mảng đường đi
            while father[current_node.id] != -1:  # gặp id là -1 (id node cha của node bắt đầu) thì dừng
                current_node = g.grid_cells[father[current_node.id]] # chuyển node cha của node hiện tại thành node hiện tại mới 
                path.append(current_node) # thêm node hiện tại vào mảng đường đi.

            path.reverse() # nãy lần ngược lên thì giờ đảo lại cho đúng chiều
            for node in path: # tô màu cho đường đi
                node.set_color(BLUE, sc)
                pygame.time.delay(10)
                pygame.display.update()
            return
        
        # nếu id node hiện tại chưa phải là id của node đích thì sẽ kiểm tra các hàng xóm của node hiện tại
        neighbors = g.get_neighbors(current_node)  # mảng này chứa tất cả các node hàng xóm của node hiện tại
        for neighbor in neighbors: # duyệt từng hàng xóm trong mảng
            if neighbor.id not in closed_set and neighbor.id not in open_set: # nếu node này chưa có trong open_set và closed_set, nghĩa là node này chưa được đụng đến
                open_set.append(neighbor.id) # do đó sẽ thêm nó vào cuối mảng open_set để duyệt sau
                father[neighbor.id] = current_node.id # gắn id node cha của tất cả các node hàng xóm là node hiện tại (vì node hiện tại dẫn đến các node hàng xóm)

        # node nào được duyệt rồi thì tô màu đỏ
        current_node.set_color(RED, sc)
        pygame.time.delay(10)
        pygame.display.update()
    
    # in ra No path found nếu không tìm thấy đường đi
    print("No path found.") 

def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')
    open_set = [g.start.id]
    closed_set = []
    father = [-1] * g.get_length()

    # về cơ bản, code vẫn khá giống DFS
    while open_set:
        current_node_id = open_set.pop(0) # lấy node đầu tiên trong open_set (DFS lấy node cuối danh sách)
        current_node = g.grid_cells[current_node_id]
        closed_set.append(current_node_id) 

        # khối lệnh xây dựng đường đi
        if current_node_id == g.goal.id:
            path = [current_node]
            while father[current_node.id] != -1:
                current_node = g.grid_cells[father[current_node.id]]
                path.append(current_node)
            path.reverse()
            for node in path:
                node.set_color(BLUE, sc)
                pygame.time.delay(10)
                pygame.display.update()
            return

        # khối lệnh kiểm tra các node hàng xóm
        neighbors = g.get_neighbors(current_node) 
        for neighbor in neighbors: 
            if neighbor.id not in closed_set and neighbor.id not in open_set:
                open_set.append(neighbor.id)
                father[neighbor.id] = current_node.id

        current_node.set_color(RED, sc)
        pygame.time.delay(10)
        pygame.display.update()

    print("No path found.")

# hàm tính khoảng cách (dùng nó để tính trọng số giữa các node và ước lượng chi phí ngắn nhất cho thuật toán A*)
def Distance(A_id, B_id, g: SearchSpace):
    A = g.grid_cells[A_id]
    B = g.grid_cells[B_id]
    return ((B.rect.x-A.rect.x)**2+(B.rect.y-A.rect.y)**2)**0.5

def Dijkstra(g: SearchSpace, sc: pygame.Surface):
    print('Implement Dijkstra algorithm')
    open_set = {g.start.id: 0} # khác với 2 thuật toán trên, open_set trong thuật toán Dijkstra, A_star là 1 từ điển với giá trị là trọng số từ node bắt đầu đêns node có id này
    closed_set = []
    father = [-1] * g.get_length()

    while open_set:
        current_node_id = next(iter(open_set.keys()))  # Lấy id node đầu tiên trong open_set
        current_node = g.grid_cells[current_node_id] # lấy node tương ứng với id 
        closed_set.append(current_node_id) # đồng thời thêm node đó vào danh sách đã duyệt 

        # khối lệnh tìm và vẽ lại đường đi
        if current_node_id == g.goal.id: 
            path = [current_node]
            while father[current_node.id] != -1:
                current_node = g.grid_cells[father[current_node.id]]
                path.append(current_node)

            path.reverse()
            for node in path:
                node.set_color(BLUE, sc)
                pygame.time.delay(10)
                pygame.display.update()
            return

        neighbors = g.get_neighbors(current_node) #tạo mảng các hàng xóm của node hiện tại
        for neighbor in neighbors: # duyệt từng node hàng xóm
            if neighbor.id not in closed_set and neighbor.id not in open_set: # nếu chưa từng đụng đến node này thì thêm vào open_set để chờ được duyệt
                open_set[neighbor.id] = open_set[current_node_id] + Distance(current_node_id, neighbor.id, g) # thêm trọng số vào id tương ứng của nó
                father[neighbor.id] = current_node.id # gắn node hiện tại là cha của node hàng xóm
                
            elif neighbor.id in closed_set: # nếu nó đã được duyệt qua thì qua duyệt node khác
                continue
            else: # nhảy xuống dưới đây nghĩa là nó đã có trong open_set để chờ duyệt
                if open_set[neighbor.id] > (open_set[current_node_id] + Distance(current_node_id, neighbor.id, g)): # nếu trọng số của node trong open_set lớn hơn node hiện tại
                    open_set.pop(neighbor.id) # thì lấy node trong open_set ra
                    open_set[neighbor.id] = open_set[current_node_id] + Distance(current_node_id, neighbor.id, g) # cập nhật node hiện tại vào cuối open_set
                    father[neighbor.id] = current_node.id # gắn id node cha

        # tô màu các node đã duyệt
        current_node.set_color(RED, sc)
        pygame.time.delay(5)
        pygame.display.update()
        open_set.pop(current_node_id)

    print("No path found.")

def A_star(g: SearchSpace, sc: pygame.Surface):
    print('Implement A* algorithm')
    open_set = {g.start.id: 0} # tương tự với thuật toán Dijkstra
    closed_set = []
    father = [-1] * g.get_length()

    while open_set:
        #lấy ra node x trong open_set sao cho giá trị của node x + giá trị từ x đến goal là nhỏ nhất
        current_node_id = min(open_set, key=lambda x: open_set[x] + Distance(x, g.goal.id, g))
        current_node = g.grid_cells[current_node_id] # lấy node tương ứng với id
        closed_set.append(current_node_id) # thêm vào mảng các node đã duyệt

        # khối lệnh tìm và vẽ lại đường đi
        if current_node_id == g.goal.id:
            path = [current_node]
            while father[current_node.id] != -1:
                current_node = g.grid_cells[father[current_node.id]]
                path.append(current_node)
            path.reverse()
            for node in path:
                node.set_color(BLUE, sc)
                pygame.time.delay(10)
                pygame.display.update()
            return

        # chưa gặp goal thì duyệt các hàng xóm (khối lệnh này giống với Dijkstra)
        neighbors = g.get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor.id not in closed_set and neighbor.id not in open_set:
                open_set[neighbor.id] = open_set[current_node_id] + Distance(current_node_id, neighbor.id, g)
                father[neighbor.id] = current_node.id
            elif neighbor.id in closed_set:
                continue
            else:
                if open_set[neighbor.id] > (open_set[current_node_id] + Distance(current_node_id, neighbor.id, g)):
                    open_set.pop(neighbor.id)
                    open_set[neighbor.id] = open_set[current_node_id] + Distance(current_node_id, neighbor.id, g)
                    father[neighbor.id] = current_node.id

        # tô màu các node đã được duyệt
        current_node.set_color(RED, sc)
        pygame.time.delay(5)
        pygame.display.update()
        open_set.pop(current_node_id)

    print("No path found.")  
    