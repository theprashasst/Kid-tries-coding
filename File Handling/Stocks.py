import csv
newdata=[]
# Open the CSV file in read mode
with open('stocks.csv', 'r') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:

        pe_ratio = round(int(row["Price"]) / int(row["Earnings Per Share"]), 2)
        pb_ratio = round(int(row["Price"]) / int(row["Book Value"]), 2)

        newrow={
            "Company Name":row["Company Name"],
            "PE Ratio": pe_ratio,
            "PB Ratio": pb_ratio
        }
        newdata.append(newrow)



print(newdata)


with open("newfile.csv","w") as newfile:

    newfiledname=["Company Name","PE Ratio","PB Ratio"]

    csv_writer= csv.DictWriter(newfile, fieldnames=newfiledname)


    # Write the header to the new CSV file
    csv_writer.writeheader()

    # Write the modified data to the new CSV file
    csv_writer.writerows(newdata)
