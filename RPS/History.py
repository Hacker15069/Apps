import csv, datetime

def insert(scores="0-0", status="Draw", date="0000-00-00, 00-00-00", file="History.csv"):
    time = datetime.datetime.now()
    year = time.strftime("%Y")
    month = time.strftime("%b")
    day = time.strftime("%d")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    date = f"{year} {month} {day}. {hour}:{minute}"
    
    with open(file, "a", newline="") as file:

        csv_writer = csv.writer(file, delimiter=" ")

        csv_writer.writerow([scores, status, date])

def read(key="Scores", file="History.csv", Dict = {"Scores":0, "Status":1, "Date":2}):
    Values = []
    
    with open(file, "r", newline="") as file:

        csv_reader = csv.reader(file, delimiter=" ")
        
        for line in csv_reader:
            Values.append(line[Dict[key]])
        return Values

if __name__ == "__main__":    
    for line in range(10):
        insert(f"{line}-{line+1}", "Win")
    print(read())
