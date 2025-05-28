class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Membuat linked list kosong
head = None

# Fungsi append di-inline tanpa def
data_to_add = [1, 2, 3, 4]

for data in data_to_add:
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

def print_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

print("List sebelum penghapusan:")
print_list(head)

# Menghapus node awal (head)
if head is not None:
    if head.next is None:
        head = None
    else:
        head = head.next
        head.prev = None

print("List setelah menghapus node pertama:")
print_list(head)

# Menghapus node akhir
if head is not None:
    if head.next is None:
        head = None
    else:
        current = head
        while current.next:
            current = current.next
        # current adalah node terakhir
        if current.prev:
            current.prev.next = None

print("List setelah menghapus node terakhir:")
print_list(head)

# Menghapus node berdasarkan nilai tertentu (misal nilai 2)
value = 2
current = head
while current:
    if current.data == value:
        # Jika node yang dihapus adalah head
        if current == head:
            head = current.next
            if head:
                head.prev = None
        else:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        break
    current = current.next

print("List setelah menghapus node dengan nilai 2:")
print_list(head)