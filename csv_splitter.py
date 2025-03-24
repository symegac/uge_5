import os.path

def main() -> None:
    with open(os.path.join("Flight data", "flights.csv"), 'r', encoding="utf-8") as file:
        part = 0
        new_file = []
        raw_data = file.readlines()
        for line, entry in enumerate(raw_data):
            new_file.append(entry)
            if line % 500000 == 0:
                with open(os.path.join("Flight data", f"flights p{part}.csv"), 'w', encoding="utf-8") as output_file:
                    output_file.writelines(new_file)
                part += 1
                new_file = []

if __name__ == "__main__":
    main()