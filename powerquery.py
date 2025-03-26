import os.path

data_dir = "Flight data"
data_file = "5d.csv"

def generate_replacer(dir: str = data_dir, filename: str = data_file) -> None:
    """
    Genererer en tekstfil med linjer, der kan indsættes i PowerQuery
    for at erstatte de femcifrede lufthavnskoder med de tilsvarende
    IATA-lufthavnskoder.

    :param dir: Mappen, hvori nøglefilen ligger.
        Standardværdi: ``data_dir``
    :type dir: str
    :param filename: Navnet på nøglefilen.
        Standardværdi: ``data_file``
    :type filename: str
    """
    num_to_iata = []
    with open(os.path.join(dir, filename), 'r', encoding="utf-8") as file:
        for line in file:
            split_line = line.split(';')
            num_to_iata.append((split_line[0], split_line[1],))

    with open(
        os.path.join(dir, f"{os.path.splitext(filename)[0]}-output.txt"),
        'w', encoding="utf-8"
    ) as file:
        for count, conv in enumerate(num_to_iata, 3):
            file.write(f"#\"Erstattet værdi{count+1}\" = Table.ReplaceValue(#\"Erstattet værdi{count}\",\"{conv[0].strip()}\",\"{conv[1].strip()}\",Replacer.ReplaceText,{{\"ORIGIN_AIRPORT\", \"DESTINATION_AIRPORT\"}}),\n")

# F.eks.
#       #"Erstattet værdi10" = Table.ReplaceValue(#"Erstattet værdi9","10155","ACT",Replacer.ReplaceText,{"ORIGIN_AIRPORT", "DESTINATION_AIRPORT"}),

if __name__ == "__main__":
    generate_replacer()