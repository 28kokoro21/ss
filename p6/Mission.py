from collections import deque

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rm < rc:
        return False

    return True


def solve():

    queue = deque()
    queue.append((3, 3, 0, []))

    visited = set()

    moves = [
        (1, 0, "1 Missionary"),
        (2, 0, "2 Missionaries"),
        (0, 1, "1 Cannibal"),
        (0, 2, "2 Cannibals"),
        (1, 1, "1 Missionary and 1 Cannibal")
    ]

    while queue:

        m, c, boat, path = queue.popleft()

        if (m, c, boat) in visited:
            continue

        visited.add((m, c, boat))

        if m == 0 and c == 0:
            print("Solution:")
            for x in path:
                print(x)
            return

        for dm, dc, name in moves:

            if boat == 0:
                nm = m - dm
                nc = c - dc
                side = "Left to Right"
                nb = 1

            else:
                nm = m + dm
                nc = c + dc
                side = "Right to Left"
                nb = 0

            if valid(nm, nc):

                new_path = path + [
                    name + " moves " + side
                ]

                queue.append(
                    (nm, nc, nb, new_path)
                )


solve()