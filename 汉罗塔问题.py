def main():
    n = eval(input("Enter number of disks:"))

    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')


def moveDisks(n, fromTower, toTower, auxTower):
    if n == 1:
        print("Move disk", n, "from", fromTower, "to", toTower)
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)


main()
