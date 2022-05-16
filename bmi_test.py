import json
import pandas as pd

try:
    print(" process satrted ")
    with open('C:/Users/mohantyb/bmi_input.json', encoding="utf8") as f:
        data = f.readlines()
    data_json_str = "[" + ','.join(data) + "]"
    data_df = pd.read_json(data_json_str)
    print("json file converted to dataframe ....: ",data_df)

    # creating 2 new varibale
    # converting the height from CM to M 
    # Calculating the BMI 

    data_df['HeightM'] = data_df['HeightCm']/100
    data_df['BMI_Calc'] = data_df['WeighKg']/(data_df['HeightM']**2)

    # def function to develop bmi category & bmi health risk 
    def calculate_bmi_category(data):
        if data['BMI_Calc'] <=18.4:
            return "Under Weight"
        elif data['BMI_Calc'] >=18.5 and data['BMI_Calc']<=24.9:
            return "Normal Weight"
        elif data['BMI_Calc'] >=25 and data['BMI_Calc']<=29.9:
            return "Over Weight"
        elif data['BMI_Calc'] >=30 and data['BMI_Calc']<=34.9:
            return "Moderately Obese"
        elif data['BMI_Calc'] >=35 and data['BMI_Calc']<=39.9:
            return "Severely Obese"
        elif data['BMI_Calc'] >=40:
            return "Very Severely Obese"

    def calculate_bmi_healthrisk(data):
        if data['BMI_Calc'] <=18.4:
            return "Malnutrition Risk"
        elif data['BMI_Calc'] >=18.5 and data['BMI_Calc']<=24.9:
            return "Low Risk"
        elif data['BMI_Calc'] >=25 and data['BMI_Calc']<=29.9:
            return "Enhanced Risk"
        elif data['BMI_Calc'] >=30 and data['BMI_Calc']<=34.9:
            return "Medium Risk"
        elif data['BMI_Calc'] >=35 and data['BMI_Calc']<=39.9:
            return "High Risk"
        elif data['BMI_Calc'] >=40:
            return "Very High Risk"

    # Calling the function defined above
    data_df['BMI Category'] = data_df.apply(calculate_bmi_category, axis=1)
    data_df['Health Risk'] = data_df.apply(calculate_bmi_healthrisk, axis=1)

    print(data_df)

    # Calculate the count of overweight people

    data_df["overweight_count"] = data_df['BMI Category'].value_counts()['Over Weight']
    print(data_df)

except Exception as e:
        print('Exception in the bmi test code: ', exc_info=True)
        bmi_test = {'error':'in bmi_test'}
        print(data-df)



