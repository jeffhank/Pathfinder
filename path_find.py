class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.max_len = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, state_dict):
        in_open = False
        for item in self.queue:
            if item['state'] == state_dict['state']:
                in_open = True
                if state_dict['f'] < item['f']:
                    item['g'] = state_dict['g']
                    item['f'] = state_dict['f']
                    item['parent'] = state_dict['parent']

        if not in_open:
            self.queue.append(state_dict)

        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def requeue(self, from_closed):
        """ Re-queue a dictionary from the closed list (see lecture slide 21)
        """
        self.queue.append(from_closed)

        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def pop(self):
        """ Remove and return the dictionary with the smallest f(n)=g(n)+h(n)
        """
        minf = 0
        for i in range(1, len(self.queue)):
            if self.queue[i]['f'] < self.queue[minf]['f']:
                minf = i
        state = self.queue[minf]
        del self.queue[minf]
        return state


def generate_board(length, x, y, end_x, end_y):
    board = []
    for row in range(length):
        side = []
        for num in range(length):
            side.append(0)
        board.append(side)
    board[x][y] = 1
    board[end_x][end_y] = 2
    return board


def generate_succ(x, y):
    succ_list = []
    if x == 0:
        # if both the x and y are zero only 3 succs
        if y == 0:
            succ_list.append(1, 1)
            succ_list.append(0, 1)
            succ_list.append(1, 0)
        else:
            # only x is zero, 5 possbile succs
            succ_list.append(x, y + 1)
            succ_list.append(x, y - 1)
            succ_list.append(x + 1, y + 1)
            succ_list.append(x + 1, y)
            succ_list.append(x + 1, y - 1)


def calc_heuristic(x, y, goal_x, goal_y):
    one = abs(x - goal_x)
    two = abs(y - goal_y)
    return max(one, two)


def solve(start_x, start_y, goal_x, goal_y):
    open_list = PriorityQueue()
    closed_list = []
    startDict = {'state': (start_x, start_y), 'h': calc_heuristic(start_x, start_y, goal_x, goal_y), 'g': 0,
                 'parent': None, 'f': calc_heuristic(start_x, start_y, goal_x, goal_y) + 0}
    gCount = 0
    open_list.enqueue(startDict)
    while not open_list.is_empty():
        q = open_list.pop()
        succ_list = generate_succ(q)
        for item in succ_list:
            if item['state'][0] == goal_x and item['state'][1] == goal_y:
                goal = item
                break
            item['g'] = q['g'] + calc_g()



