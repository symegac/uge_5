import os.path

data_dir = "Flight data"
data_file = "5d_to_iata.csv"

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
        file.write("#\"ErstatAlle\" = [")
        for count, conv in enumerate(num_to_iata):
            file.write(f"#\"{conv[0].strip()}\" = \"{conv[1].strip()}\"")
            if count < len(num_to_iata) - 1:
                file.write(',')
        file.write("]")

# Gammel metode (meget langsom, da der loopes gennem de 5,8 mio. rækker 307 gange):
#   file.write(f"#\"Erstattet værdi{count+1}\" = Table.ReplaceValue(#\"Erstattet værdi{count}\",\"{conv[0].strip()}\",\"{conv[1].strip()}\",Replacer.ReplaceText,{{\"ORIGIN_AIRPORT\", \"DESTINATION_AIRPORT\"}}),\n")
#   -1/307 outputs->        #"Erstattet værdi10" = Table.ReplaceValue(#"Erstattet værdi9","10155","ACT",Replacer.ReplaceText,{"ORIGIN_AIRPORT", "DESTINATION_AIRPORT"}),
# Ny metode (meget hurtigere, da der kun loopes gennem rækkerne 1 gang):
#   -eneste output->        #"ErstatAlle" = [#"10135" = "ABE",#"10136" = "ABI",#"10140" = "ABQ",#"10141" = "ABR",#"10146" = "ABY",#"10154" = "ACK",#"10155" = "ACT",#"10157" = "ACV",#"10158" = "ACY",#"10165" = "ADK",#"10170" = "ADQ",#"10185" = "AEX",#"10208" = "AGS",#"10257" = "ALB",#"10268" = "ALO",#"10279" = "AMA",#"10299" = "ANC",#"10333" = "APN",#"10372" = "ASE",#"10397" = "ATL",#"10408" = "ATW",#"10423" = "AUS",#"10431" = "AVL",#"10434" = "AVP",#"10469" = "AZO",#"10529" = "BDL",#"10551" = "BET",#"10561" = "BFL",#"10577" = "BGM",#"10581" = "BGR",#"10599" = "BHM",#"10620" = "BIL",#"10627" = "BIS",#"10631" = "BJI",#"10666" = "BLI",#"10685" = "BMI",#"10693" = "BNA",#"10713" = "BOI",#"10721" = "BOS",#"10728" = "BPT",#"10731" = "BQK",#"10732" = "BQN",#"10739" = "BRD",#"10747" = "BRO",#"10754" = "BRW",#"10779" = "BTM",#"10781" = "BTR",#"10785" = "BTV",#"10792" = "BUF",#"10800" = "BUR",#"10821" = "BWI",#"10849" = "BZN",#"10868" = "CAE",#"10874" = "CAK",#"10918" = "CDC",#"10926" = "CDV",#"10980" = "CHA",#"10990" = "CHO",#"10994" = "CHS",#"11003" = "CID",#"11013" = "CIU",#"11042" = "CLE",#"11049" = "CLL",#"11057" = "CLT",#"11066" = "CMH",#"11067" = "CMI",#"11076" = "CMX",#"11097" = "COD",#"11109" = "COS",#"11111" = "COU",#"11122" = "CPR",#"11140" = "CRP",#"11146" = "CRW",#"11150" = "CSG",#"11193" = "CVG",#"11203" = "CWA",#"11252" = "DAB",#"11259" = "DAL",#"11267" = "DAY",#"11274" = "DBQ",#"11278" = "DCA",#"11292" = "DEN",#"11298" = "DFW",#"11308" = "DHN",#"11315" = "DIK",#"11337" = "DLH",#"11413" = "DRO",#"11423" = "DSM",#"11433" = "DTW",#"11447" = "DVL",#"11471" = "EAU",#"11481" = "ECP",#"11503" = "EGE",#"11525" = "EKO",#"11537" = "ELM",#"11540" = "ELP",#"11577" = "ERI",#"11587" = "ESC",#"11603" = "EUG",#"11612" = "EVV",#"11617" = "EWN",#"11618" = "EWR",#"11624" = "EYW",#"11630" = "FAI",#"11637" = "FAR",#"11638" = "FAT",#"11641" = "FAY",#"11648" = "FCA",#"11695" = "FLG",#"11697" = "FLL",#"11721" = "FNT",#"11775" = "FSD",#"11778" = "FSM",#"11823" = "FWA",#"11865" = "GCC",#"11867" = "GCK",#"11884" = "GEG",#"11898" = "GFK",#"11905" = "GGG",#"11921" = "GJT",#"11953" = "GNV",#"11973" = "GPT",#"11977" = "GRB",#"11980" = "GRI",#"11982" = "GRK",#"11986" = "GRR",#"11995" = "GSO",#"11996" = "GSP",#"12003" = "GTF",#"12007" = "GTR",#"12016" = "GUM",#"12094" = "HDN",#"12129" = "HIB",#"12156" = "HLN",#"12173" = "HNL",#"12177" = "HOB",#"12191" = "HOU",#"12197" = "HPN",#"12206" = "HRL",#"12217" = "HSV",#"12255" = "HYS",#"12264" = "IAD",#"12265" = "IAG",#"12266" = "IAH",#"12278" = "ICT",#"12280" = "IDA",#"12323" = "ILM",#"12335" = "IMT",#"12339" = "IND",#"12343" = "INL",#"12389" = "ISN",#"12391" = "ISP",#"12402" = "ITO",#"12441" = "JAC",#"12448" = "JAN",#"12451" = "JAX",#"12478" = "JFK",#"12511" = "JLN",#"12519" = "JMS",#"12523" = "JNU",#"12758" = "KOA",#"12819" = "KTN",#"12884" = "LAN",#"12888" = "LAR",#"12889" = "LAS",#"12891" = "LAW",#"12892" = "LAX",#"12896" = "LBB",#"12898" = "LBE",#"12915" = "LCH",#"12945" = "LEX",#"12951" = "LFT",#"12953" = "LGA",#"12954" = "LGB",#"12982" = "LIH",#"12992" = "LIT",#"13029" = "LNK",#"13061" = "LRD",#"13076" = "LSE",#"13127" = "LWS",#"13158" = "MAF",#"13184" = "MBS",#"13198" = "MCI",#"13204" = "MCO",#"13230" = "MDT",#"13232" = "MDW",#"13241" = "MEI",#"13244" = "MEM",#"13256" = "MFE",#"13264" = "MFR",#"13277" = "MGM",#"13290" = "MHK",#"13296" = "MHT",#"13303" = "MIA",#"13342" = "MKE",#"13344" = "MKG",#"13360" = "MLB",#"13367" = "MLI",#"13377" = "MLU",#"13422" = "MOB",#"13433" = "MOT",#"13459" = "MQT",#"13476" = "MRY",#"13485" = "MSN",#"13486" = "MSO",#"13487" = "MSP",#"13495" = "MSY",#"13502" = "MTJ",#"13541" = "MVY",#"13577" = "MYR",#"13795" = "OAJ",#"13796" = "OAK",#"13830" = "OGG",#"13851" = "OKC",#"13871" = "OMA",#"13873" = "OME",#"13891" = "ONT",#"13930" = "ORD",#"13931" = "ORF",#"13933" = "ORH",#"13964" = "OTH",#"13970" = "OTZ",#"14006" = "PAH",#"14025" = "PBG",#"14027" = "PBI",#"14057" = "PDX",#"14098" = "PHF",#"14100" = "PHL",#"14107" = "PHX",#"14108" = "PIA",#"14109" = "PIB",#"14113" = "PIH",#"14122" = "PIT",#"14150" = "PLN",#"14193" = "PNS",#"14222" = "PPG",#"14252" = "PSC",#"14254" = "PSE",#"14256" = "PSG",#"14262" = "PSP",#"14307" = "PVD",#"14321" = "PWM",#"14457" = "RAP",#"14487" = "RDD",#"14489" = "RDM",#"14492" = "RDU",#"14520" = "RHI",#"14524" = "RIC",#"14543" = "RKS",#"14570" = "RNO",#"14574" = "ROA",#"14576" = "ROC",#"14588" = "ROW",#"14633" = "RST",#"14635" = "RSW",#"14674" = "SAF",#"14679" = "SAN",#"14683" = "SAT",#"14685" = "SAV",#"14689" = "SBA",#"14696" = "SBN",#"14698" = "SBP",#"14709" = "SCC",#"14711" = "SCE",#"14730" = "SDF",#"14747" = "SEA",#"14771" = "SFO",#"14783" = "SGF",#"14794" = "SGU",#"14814" = "SHV",#"14828" = "SIT",#"14831" = "SJC",#"14842" = "SJT",#"14843" = "SJU",#"14869" = "SLC",#"14893" = "SMF",#"14905" = "SMX",#"14908" = "SNA",#"14952" = "SPI",#"14960" = "SPS",#"14986" = "SRQ",#"15016" = "STL",#"15024" = "STT",#"15027" = "STX",#"15041" = "SUN",#"15048" = "SUX",#"15070" = "SWF",#"15096" = "SYR",#"15249" = "TLH",#"15295" = "TOL",#"15304" = "TPA",#"15323" = "TRI",#"15356" = "TTN",#"15370" = "TUL",#"15376" = "TUS",#"15380" = "TVC",#"15389" = "TWF",#"15401" = "TXK",#"15411" = "TYR",#"15412" = "TYS",#"15497" = "UST",#"15607" = "VLD",#"15624" = "VPS",#"15841" = "WRG",#"15919" = "XNA",#"15991" = "YAK",#"16218" = "YUM"],
#   -følges i PQ af dette-> #"Erstat værdier" = Table.TransformColumns(#"Erstattede fejl",{{"ORIGIN_AIRPORT",each Record.FieldOrDefault(ErstatAlle,_,_)},{"DESTINATION_AIRPORT",each Record.FieldOrDefault(#"ErstatAlle",_,_)}})

if __name__ == "__main__":
    generate_replacer()