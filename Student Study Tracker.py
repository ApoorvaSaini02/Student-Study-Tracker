# ==========================================
# SMART STUDY TIME TRACKER
# Python Project
# ==========================================


import datetime


FILE_NAME = "study_data.txt"


records = []


# ------------------------------------------
# Load data from file
# ------------------------------------------

def load_data():

    global records

    records = []

    try:

        file = open(FILE_NAME, "r")


        for line in file:

            line = line.strip()


            if line != "":

                data = line.split(",")


                record = {

                    "date": data[0],

                    "subject": data[1],

                    "start": data[2],

                    "end": data[3],

                    "hours": float(data[4]),

                    "note": data[5]

                }


                records.append(record)



        file.close()


    except:


        file = open(FILE_NAME,"w")

        file.close()



# ------------------------------------------
# Save data
# ------------------------------------------

def save_data():


    file = open(FILE_NAME,"w")


    for r in records:


        line = (

            r["date"] + "," +

            r["subject"] + "," +

            r["start"] + "," +

            r["end"] + "," +

            str(r["hours"]) + "," +

            r["note"]

        )


        file.write(line+"\n")



    file.close()





# ------------------------------------------
# Calculate study hours
# ------------------------------------------

def calculate_hours(start,end):


    start_time = datetime.datetime.strptime(
        start,
        "%H:%M"
    )


    end_time = datetime.datetime.strptime(
        end,
        "%H:%M"
    )


    difference = end_time - start_time


    hours = difference.seconds / 3600


    return round(hours,2)







# ------------------------------------------
# Add Study Session
# ------------------------------------------

def add_record():


    print("\n------ ADD STUDY SESSION ------")


    date = input("Date (DD-MM-YYYY): ")


    subject = input("Subject: ")


    start = input("Start Time (HH:MM): ")


    end = input("End Time (HH:MM): ")


    note = input("What did you study today?: ")




    hours = calculate_hours(start,end)



    record = {


        "date":date,

        "subject":subject,

        "start":start,

        "end":end,

        "hours":hours,

        "note":note


    }



    records.append(record)



    save_data()



    print("\nSession Saved!")

    print("Study Time:",hours,"hours")








# ------------------------------------------
# View Records
# ------------------------------------------

def view_records():


    print("\n========== STUDY HISTORY ==========")


    if len(records)==0:


        print("No records found")

        return



    print("-"*85)


    print(

        "{:<5}{:<15}{:<18}{:<10}{:<10}{:<10}".format(

            "No",

            "Date",

            "Subject",

            "Start",

            "End",

            "Hours"

        )

    )


    print("-"*85)



    count=1



    for r in records:


        print(

            "{:<5}{:<15}{:<18}{:<10}{:<10}{:<10}".format(

                count,

                r["date"],

                r["subject"],

                r["start"],

                r["end"],

                r["hours"]

            )

        )


        count=count+1



    print("-"*85)







# ------------------------------------------
# Search Subject
# ------------------------------------------

def search_subject():


    name=input("\nEnter subject name: ")



    found=False



    for r in records:


        if r["subject"].lower()==name.lower():


            print("\nDate:",r["date"])

            print("Start:",r["start"])

            print("End:",r["end"])

            print("Hours:",r["hours"])

            print("Notes:",r["note"])


            found=True



    if found==False:


        print("No record found")






# ------------------------------------------
# Start Program
# ------------------------------------------


load_data()# ==========================================
# PART 2
# Analysis + Graph + Final Menu
# ==========================================


import matplotlib.pyplot as plt



# ------------------------------------------
# Total Study Hours
# ------------------------------------------

def total_hours():

    total = 0


    for r in records:

        total = total + r["hours"]


    print("\nTotal Study Time:")

    print(round(total,2),"hours")





# ------------------------------------------
# Average Study Hours
# ------------------------------------------

def average_hours():


    if len(records)==0:

        print("No data")

        return



    total = 0


    for r in records:

        total = total + r["hours"]



    average = total / len(records)



    print("\nAverage Session Time:")

    print(round(average,2),"hours")







# ------------------------------------------
# Most Studied Subject
# ------------------------------------------

def best_subject():


    subjects = {}



    for r in records:


        name = r["subject"]



        if name in subjects:


            subjects[name] = subjects[name] + r["hours"]



        else:


            subjects[name] = r["hours"]






    highest = ""

    maximum = 0



    for s in subjects:


        if subjects[s] > maximum:


            maximum = subjects[s]

            highest = s




    print("\nMost Studied Subject:")

    print(highest)

    print("Total Hours:",maximum)








# ------------------------------------------
# Weekly Goal Tracker
# ------------------------------------------

def goal_tracker():


    goal = float(input("\nEnter weekly goal hours: "))



    total = 0



    for r in records:


        total = total + r["hours"]




    percentage = (total / goal) * 100




    print("\nGoal Progress")

    print("----------------")

    print("Completed:",round(total,2),"hours")

    print("Goal:",goal,"hours")

    print("Progress:",round(percentage,2),"%")




    if percentage >=100:


        print("Goal Completed!")



    elif percentage >=70:


        print("Almost there!")



    else:


        print("Keep improving!")







# ------------------------------------------
# Subject Graph
# ------------------------------------------

def subject_graph():


    subjects={}



    for r in records:


        name=r["subject"]



        if name in subjects:


            subjects[name]=subjects[name]+r["hours"]



        else:


            subjects[name]=r["hours"]






    names=[]

    hours=[]



    for s in subjects:


        names.append(s)

        hours.append(subjects[s])





    plt.bar(names,hours,color="purple")


    plt.xlabel("Subjects")

    plt.ylabel("Hours")

    plt.title("Study Time By Subject")


    plt.show()







# ------------------------------------------
# Final Menu
# ------------------------------------------


while True:


    print("\n================================")

    print(" SMART STUDY TIME TRACKER")

    print("================================")


    print("1. Add Study Session")

    print("2. View Study History")

    print("3. Search Subject")

    print("4. Total Study Hours")

    print("5. Average Study Time")

    print("6. Most Studied Subject")

    print("7. Weekly Goal Tracker")

    print("8. Subject Graph")

    print("9. Exit")



    choice=input("\nEnter choice: ")




    if choice=="1":


        add_record()



    elif choice=="2":


        view_records()



    elif choice=="3":


        search_subject()



    elif choice=="4":


        total_hours()



    elif choice=="5":


        average_hours()



    elif choice=="6":


        best_subject()



    elif choice=="7":


        goal_tracker()



    elif choice=="8":


        subject_graph()



    elif choice=="9":


        print("\nThank you for using Smart Study Tracker")

        break



    else:


        print("Invalid Choice")
