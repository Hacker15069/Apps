import csv, datetime

def insert(scores=[0,0], status="Draw", file="History.csv"):
    # ensuring the score keyword has a valid input
    if type(scores) != type([0]) and len(scores) != 2:
        raise Exception("scores value must be a 2 length list")
    
    # ensuring the status keyword has a valid input
    if status.capitalize() not in ["Draw","Win","Lose"]:
        raise Exception("status must be Draw, Win or Lose")
    
    # ensuring the file is a csv file
    if file[-4:] != ".csv":
        raise Exception("The storage file must be a csv file")
    
    #creating a formated date that is easy to read
    scores = f"{scores[0]}-{scores[1]}"

    #creating date
    time = datetime.datetime.now()
    year = time.strftime("%Y")
    month = time.strftime("%b")
    day = time.strftime("%d")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    #creating a specific date format
    date = f"{year} {month} {day}. {hour}:{minute}"
    
    #opening CSV file and inserting inputs for storage
    with open(file, "a", newline="") as file:
        csv_writer = csv.writer(file, delimiter=" ")
        csv_writer.writerow([scores, status, date])

def read(key="Scores", file="History.csv",):
    # ensuring the key keyword has a valid input
    if key.capitalize() not in ["Scores","Status","Date"]:
        raise Exception("key keyword must be Scores, Status or Date")

    # ensuring the file is a csv file
    if file[-4:] != ".csv":
        raise Exception("The storage file must be a csv file")
    
    Values = [] # Contains all the field values
    Dict = {"Scores": 0, "Status": 1, "Date": 2} # creation this dictionary is linked to line 53

    #reading CSV file
    with open(file, "r", newline="") as file:
        csv_reader = csv.reader(file, delimiter=" ")
        
        for line in csv_reader:
            Values.append(line[Dict[key]])
            
        return Values

if __name__ == "__main__":    
    for line in range(10):
        insert([0,0], "win")
    print(read())