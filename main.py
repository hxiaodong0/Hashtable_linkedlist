class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while (current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while (current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()


class HashMap:
    def __init__(self,size):
        self.size = size
        self.array = [LinkedList() for i in range(self.size)]
    def hash(self,key):  #takes String as input and hash it
        n = 0
        for item in "hello": n += ord(item)

        return n

    def compress(self, hash_code):
        return (hash_code % self.size)

    def assign(self,key,value):

        array_index = self.compress(self.hash(key))
        payload = Node([key,value])
        list_at_array = self.array[array_index]
        activation = False
        for item in (list_at_array):
            if item[0] == key:
                item[1] == value
                activation = True
                break
        if activation is False:
            list_at_array.insert(payload)


    def retrieve(self,key):
        array_index = self.compress(self.hash(key))
        list_at_index =  self.array[array_index]

        activation = False
        for item in (list_at_index):
            if item[0] == key:
                activation = True
                return item[1]
                break
        if activation == False:
            return None


flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]
blossom = HashMap(len(flower_definitions))
blossom.assign("key","value")
for item in flower_definitions:
    blossom.assign(item[0],item[1])