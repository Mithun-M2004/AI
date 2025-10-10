def vacuum_cleaner():
    environment = {
        'A': 'dirty',
        'B': 'dirty'
    }

    current_location = 'A'
    steps = 0

    while 'dirty' in environment.values():
        print(f"Step {steps}:")
        print(f"Location: Room {current_location}")
        print(f"Status: {environment[current_location]}")

        if environment[current_location] == 'dirty':
            print("Action: CLEAN")
            environment[current_location] = 'clean'
        else:
            print("Action: MOVE")
            current_location = 'B' if current_location == 'A' else 'A'

        print(f"Environment: {environment}")
        print("-" * 30)
        steps += 1

    print("All rooms are clean. Done!")

vacuum_cleaner()
