def towers_of_hanoi(n, source, auxiliary, destination):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        towers_of_hanoi(n - 1, source, destination, auxiliary)

        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")

        # Move the n-1 disks from auxiliary peg to destination peg
        towers_of_hanoi(n - 1, auxiliary, source, destination)


# Test the Towers of Hanoi problem
num_disks = 3
towers_of_hanoi(num_disks, 'A', 'B', 'C')
