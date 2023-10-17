
# This file will contain all the functions which will use in flask route

import json
import pickle
import numpy as np

__all_columns = None
__load_city_names = None
__load_type_names = None
__model = None

def read_data():
    print("Loading Data......! \n")
    global __load_city_names   # <-- Making global to use outside the function (Encapsulation..!)
    global __all_columns
    global __model
    global __load_type_names

    # Getting details from files
    print("Opening JSON File..!")
    with open('C:/Users/handa/Desktop/Functionup/Machine Learning/Project/Server/items/Real_Estate_Input_data_details.json','r') as f:        # <-- Opening JSON file to load columns data
        __all_columns = json.load(f)['columns']                             # <-- This will load all the column names from the opened file

        # Getting City names
        # To take only the city names
        __load_city_names = __all_columns[7:12]                             # <-- loading only city names using slicing method

        # Getting Types
        # To take only the types
        __load_type_names = __all_columns[13:]                              # <-- loading only types using slicing method

    print("JSON data copied..!")

    # Loading model
    print("\nOpening Model.Pickle File..!")                                 # <-- Opening our model file to load model data
    with open('C:/Users/handa/Desktop/Functionup/Machine Learning/Project/Server/items/Real_Estate_Price_Prediction.pickle','rb') as o:
        __model = pickle.load(o)                                            # <-- This will load all the data of the model for the calculation (eg : intercept, coefficient)
    print("Model Copied..! \n")

def all_data():
    return __all_columns

def get_city_names():
    return __load_city_names

def get_property_types():
    return __load_type_names

# We will make a function which will take the input and use __model file to predict the price

# To calculate the Predicted Value
# def predict_price(Total_Area, Baths, Balcony, BHK, BH, RK, R, City, Type):
#     city_index = np.where(x.columns == City)[0][0]  # This will return the index of entered City
#     type_index = np.where(x.columns == Type)[0][0]  # This will return the index of entered Type
#
#     l = np.zeros(len(x.columns))  # Making list of length = input column length
#     l[0] = Total_Area
#     l[1] = Baths
#     l[2] = Balcony
#     l[3] = BHK
#     l[4] = BH
#     l[5] = RK
#     l[6] = R
#     if city_index >= 0:
#         l[city_index] = 1
#     if type_index >= 0:
#         l[type_index] = 1

#     return model.predict([l])[0]


def prediction(Total_Area, Baths, Balcony, BHK, BH, RK, R, City, Type):
    try:
        city_index = __all_columns.index(City.lower())   # Getting index of input City from JSON list ".lower()" to convert input values lower case to match the JSON data
        type_index = __all_columns.index(Type.lower())   # Similar .......!
    except Exception as e:
        print("Error :",e)

    l = np.zeros(len(__all_columns))                     # Making list of length = input column length
    l[0] = Total_Area
    l[1] = Baths
    l[2] = Balcony
    l[3] = BHK
    l[4] = BH
    l[5] = RK
    l[6] = R
    if city_index >= 0:    # If user has entered a city then its obvious that "city_index" will be >0 hence we will put make that index = input value
        l[city_index] = 1
    if type_index >= 0:
        l[type_index] = 1
 
    return round(__model.predict([l])[0],2)    # Pickle file predict will give us the array, hence we only need the 1st element


if __name__ == "__main__":

    read_data()                 # Getting data
    print(all_data())
    print(get_city_names())
    print(get_property_types(),"\n")


    # Let's predict the value
    print(prediction(1000, 2, 1, 3, 0, 0, 0, 'mumbai', 'independent house'))
















    # print("************* Predict the property price ****************")
    # print("DISCLAIMER RELATED TO INPUTS ....!")
    # print('''
    #     You should select any one among the ("BHK, BH, RK, R")
    #     For Eg : if you want to have a price for Nos of BHK then only select BHK value and enter "0" in the rest of "BH, RK, R"
    #              similar if you want to have a price for Nos of BH then only select BH value and enter "0" in the rest of "BHK, RK, R"
    #              Vice versa....!
    #     ''')
    # Total_Area = float(input("Enter the Desirable Area : "))
    # Baths = input("Enter the nos of Bathrooms : ")
    # Balcony = input("Enter 1 if you want balcony Else Enter 0 : ")
    # BHK = input("If you want to select from (BH, RK, R) then enter 0 else Enter the nos of BHK : ")
    # BH = input("If you want to select from (BHK, RK, R) then enter 0 else Enter the nos of BH : ")
    # RK = input("If you want to select from (BHK, BH , R) then enter 0 else Enter the nos of RK : ")
    # R = input("If you want to select from (BHK, BH, RK) then enter 0 else Enter the nos of R : ")
    # City = input("Choose a City from above : ")
    # Type = input("Choose a Property Type from above : ")

    # pr = prediction(Total_Area, Baths, Balcony, BHK, BH, RK, R, City, Type)
    # print(pr)