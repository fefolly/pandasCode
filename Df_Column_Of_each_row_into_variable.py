import pandas as pd

logInfoDf = pd.read_csv("pandas_tutorial_read.csv", delimiter=';', names=['my_datetime','event','country','user_id','source','topic'])

    #In the following for loop,  "i" represents a row in a form of a list or array

for i in logInfoDf.itertuples():               #itertuples is a pandas function for row manipulation
    time = i[1]                                 #time is a variable that can be passed as a parameter to the client
    print("The time is: ", time)
    event = i[2]                                #event is a variable that can be passed as a parameter to the client
    print("The name of the event is: ", event)
    country = i[3]                              #country is a variable that can be passed as a parameter to the client
    print("The country it held in is: ", country)
    user = i[4]                                 #user is a variable that can be passed as a parameter to the client
    print("The user's is: ", user)
    source = i[5]                               #source is a variable that can be passed as a parameter to the client
    print("The source is: ", source)
    topic = i[6]                                #topic is a variable that can be passed as a parameter to the client
    print("The topic is: ", topic)
    print()
   
   #There is no need to modify the  code from the client from my point of view. Only the server code should be slightly changed.
   #You can do everything in the for loop
