#                       <--- UNION-FIND / (Disjoint Set Union or DSU)--->
'''
    Given a set of 'N' objects:
    1. union(x, y) --> merges two objects
    2. find(x) --> which set the object belongs to

    Uses:
    * to determine if the elements in the same set or connected to each other
    * each subset represented as a tree
'''
class Union_Find:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        #union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

if __name__ == "__main__":
    import sys
    # Read number of elements (N)
    try:
        n = int(input("Enter the number of elements:"))
        if n <= 0:
            raise ValueError("Give valid input")
    except ValueError as e:
        print(f'Error: {e}')
        sys.exit(1)

    uf = Union_Find(n)

    print("Enter the pair of integers, or press <Enter> to stop:")

    try:
        while True:
            line = sys.stdin.readline().strip() #used for reading multiple line of input until EOF
            if not line: #if input is empty
                break
            try:
                p, q = map(int, line.split())
                if not (0 <= p < n and 0 <= q < n):
                    print("out of range --> Try Again")
                    continue

                #if p, q are not connected, union them and print the pair
                if not uf.connected(p, q):
                    uf.union(p, q)
                    print(f'{p} --> {q}')
                else:
                    print(f"{p} and {q} are already connected.")
            except ValueError:
                print("Error: Invalid input. Enter two integers separated by a space.")
    except EOFError:
        pass