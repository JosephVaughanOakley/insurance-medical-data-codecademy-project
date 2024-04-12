import csv

dataset = []

with open("insurance.csv") as ins_dat:
    insurance_data = csv.DictReader(ins_dat)
    for row in insurance_data:
        dataset.append(row)

# - how much on average does smoking increase insurance costs? if we control for number of children can we see if the 
# costs associated with both BMI and smoker status behave independantly or if they compound on one another?
def max_children(dataset):
    most_children = 0
    for record in dataset:
        if int(record["children"]) > most_children:
            most_children = int(record["children"])
    return most_children
most_kids = max_children(dataset)
# print(most_kids)


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
    
# smoking_cost(dataset)

# - what is the average additional cost for 1 child? what is the average added cost of a second child? third? fourth? fifth?

def cost_of_children(dataset):
    num_zero = 0
    zero_cost = float(0)

    num_one = 0
    one_cost = float(0)

    num_two = 0
    two_cost = float(0)

    num_three = 0
    three_cost = float(0)

    num_four = 0
    four_cost = float(0)

    num_five = 0
    five_cost = float(0)

    for record in dataset:
        if record["children"] == "0":
            num_zero += 1
            zero_cost += float(record["charges"])
        elif record["children"] == "1":
            num_one += 1
            one_cost += float(record["charges"])
        elif record["children"] == "2":
            num_two += 1
            two_cost += float(record["charges"])
        elif record["children"] == "3":
            num_three += 1
            three_cost += float(record["charges"])
        elif record["children"] == "4":
            num_four += 1
            four_cost += float(record["charges"])
        elif record["children"] == "5":
            num_five += 1
            five_cost += float(record["charges"])
        else:
            print("something is wrong with the data")

    avg_zero = round(zero_cost/num_zero, 2)
    avg_one = round(one_cost/num_one, 2)
    avg_two = round(two_cost/num_two, 2)
    avg_three = round(three_cost/num_three, 2)
    avg_four = round(four_cost/num_four, 2)
    avg_five = round(five_cost/num_five, 2)

    first_child_cost = round(avg_one - avg_zero, 2)
    second_child_cost = round(avg_two - avg_one, 2)
    third_child_cost = round(avg_three - avg_two, 2)
    fourth_child_cost = round(avg_four - avg_three, 2)
    fifth_child_cost = round(avg_five - avg_four, 2)

    return print(f"The average cost of insurance ordered by number of children is: \nZero Children: ${avg_zero} \nOne Child: ${avg_one} \nTwo Children: ${avg_two} \nThree Children: ${avg_three} \nFour Children: ${avg_four} \nFive Children: ${avg_five}")
    # return print(f"The first child will cost on average ${first_child_cost}, the second \naverages an additional ${second_child_cost}, the third ${third_child_cost}, the \nfourth ${fourth_child_cost}, and the fifth ${fifth_child_cost}. Please keep \nthis in mind when planning for your future.")

cost_of_children(dataset)


# - what is the average bmi of people who have 0 children? 1 child? 2 children? 3? 4? 5?




# can we see if the age of a person affects the size of the added cost of being a smoker? (that last one I may incorporate elsewhere)