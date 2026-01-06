def generate_report():
    total = 0
    count = 0

    with open("data.txt", "r") as file:
        for line in file:
            name, department, value = line.strip().split(",")
            total += int(value)
            count += 1

    average = total / count if count > 0 else 0
    print("Total Value:", total)
    print("Average Value:", average)
