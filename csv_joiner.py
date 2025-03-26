import os
import os.path

data_dir = "Flight data"
filename = "flights.csv"
split_filename = os.path.splitext(filename)

def find_files(dir: str = data_dir) -> list[tuple[int, str]]:
    join_files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)) and file.startswith(f"{split_filename[0]} p"):
            index = int(file[len(split_filename[0])+2:-len(split_filename[1])])
            join_files.append((index, file))
    join_files.sort(key=lambda x: x[0])

    return join_files

def join_files(file_list: list[tuple[int, str]]) -> list[str]:
    full_data = []
    for join_file in join_files:
        with open(os.path.join(data_dir, join_file[1]), 'r', encoding="utf-8") as file:
            raw_data = file.readlines()
            full_data.extend(raw_data)
        # print(len(full_data))

    with open(os.path.join(data_dir, f"{split_filename[0]}-joined{split_filename[1]}"), 'a', encoding="utf-8") as file:
        file.writelines(full_data)

def main() -> None:
    files_to_join = find_files()
    join_files(files_to_join)

    # with open(os.path.join(data_dir, filename), 'r', encoding="utf-8") as file:
    #     orig_data = file.readlines()
    #     if full_data == orig_data:
    #         print(True)
    #     else:
    #         print(False)

if __name__ == "__main__":
    main()