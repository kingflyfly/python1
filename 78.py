import csv
with open("data.csv","a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id","name","age"])
    writer.writerow(["1001","yanzhe","29"])
    writer.writerow(["1002","shanshan","28"])
    writer.writerows([["1002","shanshan","28"],["1002","shanshan","28"]])