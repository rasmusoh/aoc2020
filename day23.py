import time

test = '389125467'
real = '589174263'


class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None

    def __str__(self):
        return f'{str(self.label)}'

class Cups:
    def __init__(self, labels):
        labelsiter = iter(labels)
        self.current = Cup(next(labelsiter))
        self.moves = 0
        self.bylabel = {}
        self.bylabel[self.current.label] = self.current
        last = self.current
        for label in labelsiter:
            last.next = Cup(label)
            last = last.next
            self.bylabel[label] = last
        self.n = len(self.bylabel.keys())
        last.next = self.current

    def __str__(self):
        nodes = [str(self.current)]
        node = self.current.next
        while node != self.current:
            nodes.append(str(node))
            node = node.next
        return ' '.join(nodes)

    def move(self, moves):
        for _ in range(moves):
            self.moves += 1
            pickup1 = self.current.next
            pickup2 = pickup1.next
            pickup3 = pickup2.next
            self.current.next = pickup3.next
            pickup_labels = [pickup1.label, pickup2.label, pickup3.label]

            dest_node = None
            dest_label = self.current.label
            while not dest_node:
                dest_label -= 1 
                dest_label = dest_label if dest_label > 0 else self.n
                if dest_label not in pickup_labels:
                    dest_node = self.bylabel[dest_label]
            dest_node.next, pickup3.next = pickup1, dest_node.next

            self.current = self.current.next


elements = 1000000
moves = 10000000
original = list(map(lambda x: int(x), real))
print(original)
total = original+list(range(len(original)+1, elements+1))
cups = Cups(total)
start = time.time()
cups.move(moves)
print(f'elapsed time: {time.time() -start}')

a = cups.bylabel[1].next
b = a.next
print(a.label, b.label, a.label*b.label)
