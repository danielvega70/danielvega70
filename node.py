class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, problem):
        """Return a list of child nodes resulting from applying each legal move."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Return a child node from this node by applying the given action."""
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    self.path_cost + problem.step_cost(self.state, action))

    def solution(self):
        """Return the sequence of actions to go from the initial state to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

def depth_first_search(problem):
    """Search the deepest nodes in the search tree first."""
    frontier = [Node(problem.initial)]
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None
