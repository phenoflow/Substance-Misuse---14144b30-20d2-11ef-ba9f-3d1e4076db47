# Hayley C Gorton, Roger T Webb, Mathew J Carr, Marcos Delpozo-Banos, Ann John, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"Eu15.00","system":"readv2"},{"code":"Eu13400","system":"readv2"},{"code":"Eu11400","system":"readv2"},{"code":"Eu12200","system":"readv2"},{"code":"Eu11500","system":"readv2"},{"code":"Eu16.00","system":"readv2"},{"code":"Eu14.00","system":"readv2"},{"code":"Eu15200","system":"readv2"},{"code":"Eu12z00","system":"readv2"},{"code":"Eu15500","system":"readv2"},{"code":"Eu1Az00","system":"readv2"},{"code":"Eu13100","system":"readv2"},{"code":"Eu12.00","system":"readv2"},{"code":"Eu12500","system":"readv2"},{"code":"Eu1A.00","system":"readv2"},{"code":"Eu14500","system":"readv2"},{"code":"Eu16500","system":"readv2"},{"code":"Eu13300","system":"readv2"},{"code":"1V...00","system":"readv2"},{"code":"Eu12300","system":"readv2"},{"code":"Eu13200","system":"readv2"},{"code":"Eu16200","system":"readv2"},{"code":"Eu1A100","system":"readv2"},{"code":"Eu11z00","system":"readv2"},{"code":"Eu15000","system":"readv2"},{"code":"Eu11y00","system":"readv2"},{"code":"Eu11200","system":"readv2"},{"code":"Eu16000","system":"readv2"},{"code":"Eu1A200","system":"readv2"},{"code":"Eu15100","system":"readv2"},{"code":"Eu13.00","system":"readv2"},{"code":"Eu14000","system":"readv2"},{"code":"Eu15z00","system":"readv2"},{"code":"Eu14200","system":"readv2"},{"code":"Eu11300","system":"readv2"},{"code":"Eu12000","system":"readv2"},{"code":"Eu14300","system":"readv2"},{"code":"Eu13500","system":"readv2"},{"code":"Eu14100","system":"readv2"},{"code":"Eu16z00","system":"readv2"},{"code":"Eu15300","system":"readv2"},{"code":"Eu11600","system":"readv2"},{"code":"Eu13000","system":"readv2"},{"code":"1V6..00","system":"readv2"},{"code":"Eu12y00","system":"readv2"},{"code":"Eu1A300","system":"readv2"},{"code":"Eu1A000","system":"readv2"},{"code":"Eu12100","system":"readv2"},{"code":"Eu16300","system":"readv2"},{"code":"Eu1A500","system":"readv2"},{"code":"Eu12600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["substance-misuse-behaviour---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["substance-misuse-behaviour---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["substance-misuse-behaviour---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
