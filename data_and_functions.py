import csv

dataset = []

with open("insurance.csv") as ins_dat:
    insurance_data = csv.DictReader(ins_dat)
    for row in insurance_data:
        dataset.append(row)

def max_children(dataset):
    most_children = 0
    for record in dataset:
        if int(record["children"]) > most_children:
            most_children = int(record["children"])
    return most_children
most_kids = max_children(dataset)
# print(most_kids)



# - how much on average does smoking increase insurance costs? i am making the assumptions that children are expensive
# and smoking increases the cost of insurance, so if we control for number of children do we see the cost of insurance
# rise as expected? by how much on average? i opted to include average age of both groups as an indication that these
# groups are complex and this insight is influenced by a number of variables that are not apparent.



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

# - what is the average cost of having one child? two? three through five?

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

cost_of_children(dataset)
# the averages returned here are not telling the whole story, we either do not have a large enough dataset (very likely) or there is a very
# significant error in the data collection methods meaning this dataset is not representative of the population as a whole, so we will have to dig
# deeper to see if there is another variable having an overriding impact on the cost of insurance.


###################################################################################################################################################
#
# after writing the following function i realized i needed to learn about dynamic variables because this is getting a bit out of hand. i will try
# my hand at writing a variable generator to make this less complicated (and in the real world there is no hard cap of 5 kids, so this would get
# very messy very quick) once i finish this, but for now i'm going to lean into the absurd and make this very specific.
# yes i know i made it even worse after writing this. no i am not changing it (for now).
#
###################################################################################################################################################


def smoker_vs_parent_vs_age(dataset):
    zero_nonsmoke = 0
    zero_smoke = 0
    zero_nonsmoke_cost = float(0)
    zero_smoke_cost = float(0)
    zero_nonsmoke_age = 0
    zero_smoke_age = 0

    one_nonsmoke = 0
    one_smoke = 0 
    one_nonsmoke_cost = float(0)
    one_smoke_cost = float(0)
    one_nonsmoke_age = 0
    one_smoke_age = 0

    two_nonsmoke = 0
    two_smoke = 0 
    two_nonsmoke_cost = float(0)
    two_smoke_cost = float(0)
    two_nonsmoke_age = 0
    two_smoke_age = 0

    three_nonsmoke = 0
    three_smoke = 0 
    three_nonsmoke_cost = float(0)
    three_smoke_cost = float(0)
    three_nonsmoke_age = 0
    three_smoke_age = 0

    four_nonsmoke = 0
    four_smoke = 0 
    four_nonsmoke_cost = float(0)
    four_smoke_cost = float(0)
    four_nonsmoke_age = 0
    four_smoke_age = 0

    five_nonsmoke = 0
    five_smoke = 0 
    five_nonsmoke_cost = float(0)
    five_smoke_cost = float(0)
    five_nonsmoke_age = 0
    five_smoke_age = 0     

    for record in dataset:
        if record["children"] == "0":
            if record["smoker"] == "yes":
                zero_smoke += 1
                zero_smoke_cost += float(record["charges"])
                zero_smoke_age += int(record["age"])
            else:
                zero_nonsmoke += 1
                zero_nonsmoke_cost += float(record["charges"])
                zero_nonsmoke_age += int(record["age"])
        elif record["children"] == "1":
            if record["smoker"] == "yes":
                one_smoke += 1
                one_smoke_cost += float(record["charges"])
                one_smoke_age += int(record["age"])
            else:
                one_nonsmoke += 1
                one_nonsmoke_cost += float(record["charges"])
                one_nonsmoke_age += int(record["age"])
        elif record["children"] == "2":
            if record["smoker"] == "yes":
                two_smoke += 1
                two_smoke_cost += float(record["charges"])
                two_smoke_age += int(record["age"])               
            else:
                two_nonsmoke += 1
                two_nonsmoke_cost += float(record["charges"])
                two_nonsmoke_age += int(record["age"])
        elif record["children"] == "3":
            if record["smoker"] == "yes":
                three_smoke += 1
                three_smoke_cost += float(record["charges"])
                three_smoke_age += int(record["age"])
            else:
                three_nonsmoke += 1
                three_nonsmoke_cost += float(record["charges"])
                three_nonsmoke_age += int(record["age"])
        elif record["children"] == "4":
            if record["smoker"] == "yes":
                four_smoke += 1
                four_smoke_cost += float(record["charges"])
                four_smoke_age += int(record["age"])
            else:
                four_nonsmoke += 1
                four_nonsmoke_cost += float(record["charges"])
                four_nonsmoke_age += int(record["age"])
        elif record["children"] == "5":
            if record["smoker"] == "yes":
                five_smoke += 1
                five_smoke_cost += float(record["charges"])
                five_smoke_age += int(record["age"])               
            else:
                five_nonsmoke += 1
                five_nonsmoke_cost += float(record["charges"])
                five_nonsmoke_age += int(record["age"])
        else:
            print("this must be the wrong data, cause these people cant have more than five kids") 
    
    zero_nonsmoke_avg_cost = zero_nonsmoke_cost/zero_nonsmoke
    zero_nonsmoke_avg_age = zero_nonsmoke_age/zero_nonsmoke
    zero_smoke_avg_cost = zero_smoke_cost/zero_smoke
    zero_smoke_avg_age = zero_smoke_age/zero_smoke

    one_nonsmoke_avg_cost = one_nonsmoke_cost/one_nonsmoke
    one_nonsmoke_avg_age = one_nonsmoke_age/one_nonsmoke
    one_smoke_avg_cost = one_smoke_cost/one_smoke
    one_smoke_avg_age = one_smoke_age/one_smoke

    two_nonsmoke_avg_cost = two_nonsmoke_cost/two_nonsmoke
    two_nonsmoke_avg_age = two_nonsmoke_age/two_nonsmoke
    two_smoke_avg_cost = two_smoke_cost/two_smoke
    two_smoke_avg_age = two_smoke_age/two_smoke

    three_nonsmoke_avg_cost = three_nonsmoke_cost/three_nonsmoke
    three_nonsmoke_avg_age = three_nonsmoke_age/three_nonsmoke
    three_smoke_avg_cost = three_smoke_cost/three_smoke
    three_smoke_avg_age = three_smoke_age/three_smoke    

    four_nonsmoke_avg_cost = four_nonsmoke_cost/four_nonsmoke
    four_nonsmoke_avg_age = four_nonsmoke_age/four_nonsmoke
    four_smoke_avg_cost = four_smoke_cost/four_smoke
    four_smoke_avg_age = four_smoke_age/four_smoke

    five_nonsmoke_avg_cost = five_nonsmoke_cost/five_nonsmoke
    five_nonsmoke_avg_age = five_nonsmoke_age/five_nonsmoke
    five_smoke_avg_cost = five_smoke_cost/five_smoke
    five_smoke_avg_age = five_smoke_age/five_smoke


    num_children_bool_smoker = {}
    num_children_bool_smoker["zero"] = {"no": [zero_nonsmoke_avg_age, zero_nonsmoke_avg_cost], "yes": [zero_smoke_avg_age, zero_smoke_avg_cost]}
    num_children_bool_smoker["one"] = {"no": [one_nonsmoke_avg_age, one_nonsmoke_avg_cost], "yes": [one_smoke_avg_age, one_smoke_avg_cost]}
    num_children_bool_smoker["two"] = {"no": [two_nonsmoke_avg_age, two_nonsmoke_avg_cost], "yes": [two_smoke_avg_age, two_smoke_avg_cost]}
    num_children_bool_smoker["three"] = {"no": [three_nonsmoke_avg_age, three_nonsmoke_avg_cost], "yes": [three_smoke_avg_age, three_smoke_avg_cost]}
    num_children_bool_smoker["four"] = {"no": [four_nonsmoke_avg_age, four_nonsmoke_avg_cost], "yes": [four_smoke_avg_age, four_smoke_avg_cost]}
    num_children_bool_smoker["five"] = {"no": [five_nonsmoke_avg_age, five_nonsmoke_avg_cost], "yes": [five_smoke_avg_age, five_smoke_avg_cost]}

    for num_kids, is_smoker in num_children_bool_smoker.items():
        for key, value in is_smoker.items():
            if key == "no":
                if num_kids != "one":
                    print(f"The average non-smoker who has {num_kids} children is {round(value[0], 1)} years old, and pays ${round(value[1], 2)} per year for insurance.")
                else:
                    print(f"The average non-smoker who has {num_kids} children is {round(value[0], 1)} years old, and pays ${round(value[1], 2)} per year for insurance.")
            else:
                if num_kids != "one":
                    print(f"The average smoker who has {num_kids} children is {round(value[0], 1)} years old, and pays ${round(value[1], 2)} per year for insurance.")
                else:
                    print(f"The average smoker who has {num_kids} children is {round(value[0], 1)} years old, and pays ${round(value[1], 2)} per year for insurance.")


smoker_vs_parent_vs_age(dataset)
                
# this is some interesting data, and shows me that my assumptions about the significance of the added cost of children is far outweighed 
# by other factors, but also that my assumption about the significance of the added cost of smoking was more correct than not.

# next things to look into:





# in further instances of this type of project i will definitely make a point of structuring my data more effectively from the start, followed by
# building helper functions that will generate the variables needed directly from the data which can be used in the analysis functions to speed up
# the process of writing the functions, while also leaving less clutter for my other errors to hide in (and making it easier for fresh eyes to catch up)