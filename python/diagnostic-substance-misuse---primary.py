# Hayley C Gorton, Roger T Webb, Mathew J Carr, Marcos Delpozo-Banos, Ann John, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"E25z.00","system":"readv2"},{"code":"E245z00","system":"readv2"},{"code":"E240z00","system":"readv2"},{"code":"L183z00","system":"readv2"},{"code":"E259z00","system":"readv2"},{"code":"E256z00","system":"readv2"},{"code":"E258z00","system":"readv2"},{"code":"Eu19211","system":"readv2"},{"code":"E253z00","system":"readv2"},{"code":"E244z00","system":"readv2"},{"code":"E243z00","system":"readv2"},{"code":"E246z00","system":"readv2"},{"code":"E255z00","system":"readv2"},{"code":"E257z00","system":"readv2"},{"code":"E248z00","system":"readv2"},{"code":"E252z00","system":"readv2"},{"code":"E249z00","system":"readv2"},{"code":"E242z00","system":"readv2"},{"code":"E244z11","system":"readv2"},{"code":"E25yz00","system":"readv2"},{"code":"E254z00","system":"readv2"},{"code":"E24z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diagnostic-substance-misuse---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diagnostic-substance-misuse---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diagnostic-substance-misuse---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
