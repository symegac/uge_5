import os.path

data_dir = "Flight data"
filename = "flights.csv"

def split_csv(dir: str = data_dir, origin: str = filename) -> None:
    """
    Splitter en stor .csv-fil ad i bidder à <50 MB for at kunne
    uploade på GH.
    """
    split_filename = os.path.splitext(origin)
    with open(os.path.join(dir, origin), 'r', encoding="utf-8") as file:
        part = 0
        new_file = []
        raw_data = file.readlines()
        for line, entry in enumerate(raw_data):
            new_file.append(entry)
            # Holder filstørrelse under 50 MB ved at splitte ved 450k linjer
            # Ved sidste linje gemmes den sidste fil også
            if line % 450000 == 0 or line == len(raw_data) - 1:
                with open(
                    os.path.join(dir, f"{split_filename[0]} p{part}{split_filename[1]}"),
                    'w', encoding="utf-8"
                ) as output_file:
                    output_file.writelines(new_file)
                print(f"Gemte del {part} af fil.")
                # Tæller brugt til filnavn forøges
                part += 1
                # Buffer nulstilles
                new_file = []

if __name__ == "__main__":
    split_csv()