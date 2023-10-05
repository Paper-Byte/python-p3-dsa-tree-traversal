class Tree:
    def __init__(self, root=None):
        self.root = root

    # breadth-first answer
    def get_element_by_id(self, id):
        nodes_to_visit = [self.root]
        while len(nodes_to_visit) > 0:
            node = nodes_to_visit.pop(0)
            if (node['id'] == id):
                return node
            nodes_to_visit += node['children']
        return None

    # depth-first search
    # def get_element_by_id(self, id):
    #     nodes_to_visit = [self.root]
    #     while len(nodes_to_visit) > 0:
    #         node = nodes_to_visit.pop(0)
    #         if (node['id'] == id):
    #             return node
    #         nodes_to_visit = node['children'] + nodes_to_visit
    #     return None
