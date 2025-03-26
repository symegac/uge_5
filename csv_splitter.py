import os.path

data_dir = "Flight data"
filename = "flights.csv"
split_filename = os.path.splitext(filename)

def main() -> None:
    with open(os.path.join(data_dir, filename), 'r', encoding="utf-8") as file:
        part = 0
        new_file = []
        raw_data = file.readlines()
        for line, entry in enumerate(raw_data):
            new_file.append(entry)
            if line % 450000 == 0 or line == len(raw_data) - 1:
                with open(
                    os.path.join(data_dir, f"{split_filename[0]} p{part}{split_filename[1]}"),
                    'w', encoding="utf-8"
                ) as output_file:
                    output_file.writelines(new_file)
                part += 1
                new_file = []

if __name__ == "__main__":
    main()