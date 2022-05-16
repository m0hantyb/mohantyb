def test_case(input1, input2):
    weight= float(input1)
    height= float(input2) 
    bmi=(weight)/((height/100)**2)
    if bmi<=18.4:
        return "Underweight"
    elif bmi >=18.5 and bmi <=24.9:
        return "Normal Weight"
    elif bmi>=25 and bmi <=29.9:
        return "Over Weight"
    elif bmi>=30 and bmi <=34.9:
        return "Moderately Obese"
    elif bmi>=35 and bmi <=39.9:
        return "Severely Obese"
    elif bmi>=40:
        return "Very Severely Obese"
test_case_result = test_case(96, 171)

expected_output = "Moderately Obese"
if test_case_result == expected_output:
    print("test_case_part1...:","its a succeess")
else:
    print("test_case_part1...:","There is a bug")


expected_output = "Normal Weight"
if test_case_result == expected_output:
    print("test_case_part2...:","its a succeess")
else:
    print("test_case_part2...:","There is a bug")
