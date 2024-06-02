# Hayley C Gorton, Roger T Webb, Mathew J Carr, Marcos Delpozo-Banos, Ann John, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"13c..00","system":"readv2"},{"code":"13c5.00","system":"readv2"},{"code":"13cF.00","system":"readv2"},{"code":"13cH.00","system":"readv2"},{"code":"13c7.00","system":"readv2"},{"code":"13cB.00","system":"readv2"},{"code":"1V0..00","system":"readv2"},{"code":"13c4.00","system":"readv2"},{"code":"13c1.00","system":"readv2"},{"code":"1V26.00","system":"readv2"},{"code":"13c3.00","system":"readv2"},{"code":"13c8.00","system":"readv2"},{"code":"13c6.00","system":"readv2"},{"code":"1V00.00","system":"readv2"},{"code":"1V64.00","system":"readv2"},{"code":"1V0E.00","system":"readv2"},{"code":"1V63.00","system":"readv2"},{"code":"13c9.00","system":"readv2"},{"code":"1V01.00","system":"readv2"},{"code":"E259400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["substance-misuse---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["substance-misuse---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["substance-misuse---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
