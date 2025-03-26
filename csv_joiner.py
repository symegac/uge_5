import os
import os.path

data_dir = "Flight data"
filename = "flights.csv"

def find_files(dir: str = data_dir, origin: str = filename) -> list[tuple[int, str]]:
    """
    Finder de opsplittede filer ud fra originalens navn.
    """
    join_files = []
    split_filename = os.path.splitext(origin)

    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)) and file.startswith(f"{split_filename[0]} p"):
            # Finder heltallet i filnavnet og tilknytter som index
            index = int(file[len(split_filename[0])+2:-len(split_filename[1])])
            join_files.append((index, file,))
    # Sorterer efter index, fordi rækkefølgen fundet af os.listdir()
    # er [1, 10, 11, 12, 13, 2, 3, ...]
    join_files.sort(key=lambda x: x[0])

    print("Fandt opdelte filer.")

    return join_files

def join_files(file_list: list[tuple[int, str]], dir: str = data_dir, origin: str = filename) -> list[str]:
    """
    Samler de opsplittede filer til en enkelt .csv-fil.
    """
    full_data = []
    split_filename = os.path.splitext(origin)

    # Læser data fra alle opsplittede filer
    for join_file in file_list:
        with open(os.path.join(dir, join_file[1]), 'r', encoding="utf-8") as file:
            raw_data = file.readlines()
            full_data.extend(raw_data)

    # Skriver dataen til en fil
    joined_name = f"{split_filename[0]}-joined{split_filename[1]}"
    with open(
        os.path.join(dir, joined_name),
        'w' if joined_name in os.listdir(dir) else 'a',
        encoding="utf-8"
    ) as file:
        file.writelines(full_data)

    print("Opdelte filer er blevet samlet.")

def verify_data(
    dir: str = data_dir,
    origin: str = filename,
    copy: str = f"{os.path.splitext(filename)[0]}-joined{os.path.splitext(filename)[1]}"
) -> bool:
    """
    Verificerer, at originalen og den sammenhæftede kopi
    indeholder identisk data, og at intet er gået tabt.
    """
    with open(os.path.join(dir, origin), 'r', encoding="utf-8") as file1:
        data1 = file1.readlines()
    with open(os.path.join(dir, copy), 'r', encoding="utf-8") as file2:
        data2 = file2.readlines()

    if data1 == data2:
        return True
    else:
        return False

def main() -> None:
    files_to_join = find_files()
    join_files(files_to_join)
    print("Originalen og kopien er ens:", "Sandt" if verify_data() else "Falsk")

if __name__ == "__main__":
    main()