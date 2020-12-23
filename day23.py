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

    def move(self):
        self.moves += 1
        pickup1 = self.current.next
        pickup2 = pickup1.next
        pickup3 = pickup2.next
        self.current.next = pickup3.next
        pickup_labels = [pickup1.label, pickup2.label, pickup3.label]

        dest_node = None
        dest = self.current.label
        while not dest_node:
            dest = (dest - 1) % self.n
            dest = dest if dest > 0 else self.n
            if dest not in pickup_labels:
                dest_node = self.bylabel[dest]
        temp = dest_node.next
        dest_node.next = pickup1
        pickup3.next = temp

        self.current = self.current.next


elements = 1000000
moves = 10000000
original = list(map(lambda x: int(x), real))
print(original)
total = original+list(range(len(original)+1, elements+1))
cups = Cups(total)
for _ in range(moves):
    cups.move()

a = cups.bylabel[1].next
b = a.next
print(a.label, b.label, a.label*b.label)
