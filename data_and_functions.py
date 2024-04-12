import csv

dataset = []

with open("insurance.csv") as ins_dat:
    insurance_data = csv.DictReader(ins_dat)
    for row in insurance_data:
        dataset.append(row)

# - how much on average does smoking increase insurance costs? if we control for number of children can we see if the 
# costs associated with both BMI and smoker status behave independantly or if they compound on one another?

def smoking_cost(dataset, max_children = 0):
    smoker_total_cost = float(0)
    smoker_total_num = 0
    smoker_sum_age = 0
    non_smoker_total_cost = float(0)
    non_smoker_total_num = 0
    non_smoker_sum_age = 0

    for record in dataset:
        if int(record["children"]) > max_children:
            pass
        elif record["smoker"] == "yes":
            smoker_total_num += 1
            smoker_total_cost += float(record["charges"])
            smoker_sum_age += int(record["age"])
        else:
            non_smoker_total_num += 1
            non_smoker_total_cost += float(record["charges"])
            non_smoker_sum_age += int(record["age"])

    smoker_avg_cost = round((smoker_total_cost/smoker_total_num), 2)
    smoker_avg_age = round((smoker_sum_age/smoker_total_num))

    non_smoker_avg_cost = round((non_smoker_total_cost/non_smoker_total_num), 2)
    non_smoker_avg_age = round((non_smoker_sum_age/non_smoker_total_num), 1)

    cost_of_smoking = round((smoker_avg_cost - non_smoker_avg_cost), 2)

    return print(f"\n \nThe average child-free non-smoker is {non_smoker_avg_age} years old and \npays ${non_smoker_avg_cost} for coverage, while the average child-free smoker is {smoker_avg_age} years old and \npays ${smoker_avg_cost} for coverage. \nThe annual added financial burden of smoking averages ${cost_of_smoking}.\n\n")
    
smoking_cost(dataset)




# can we see if the age of a person affects the size of the added cost of being a smoker? (that last one I may incorporate elsewhere)