#!/usr/bin/env python
# coding: utf-8

# # Importing libraries

# In[301]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Read in the dataset

# In[4]:


data = pd.read_csv("Desktop/fifa.csv")
pd.set_option("display.max_columns",None)
data.head(n=3)


# In[5]:


data.shape


# In[6]:


data.columns


# In[7]:


data.info()


# # Data Cleaning

# # Creating a copy of the Dataframe

# In[8]:


fifa = data.copy()
fifa.sample(2)


# # 1.Club 

# In[9]:


fifa["Club"].dtype


# In[10]:


fifa["Club"].unique()


# In[11]:


fifa["Club"] = fifa["Club"].str.strip()
fifa["Club"].unique()


# In[12]:


fifa.head()


# # 2.Contract

# In[13]:


fifa["Contract"].dtype


# In[14]:


fifa["Contract"].unique()


# In[15]:


for index,row in fifa.iterrows():
    if "On Loan"in row["Contract"] or "Free" in row ["Contract"]:
        print (row["Contract"])


# In[16]:


def extract_contract_info(contract):
    if contract == "Free" or "On Loan" in contract:
        start_date = np.nan
        end_date = np.nan
        contract_length = 0
    else:
        start_date,end_date = contract .split(" ~ ")
        start_year = int(start_date[:4])
        end_year = int(end_date[:4])
        contract_length = end_year - start_year
    return start_date,end_date,contract_length

#Applying function to Contract column and create new column

new_cols = ["Contract start","Contract End","Contract Length(years)"]
new_data = fifa["Contract"].apply(lambda x:pd.Series(extract_contract_info(x)))
            
for i in range(len(new_cols)):
    fifa.insert(loc = fifa.columns.get_loc("Contract")+1+i,column = new_cols[i],value=new_data[i])
                   


# In[156]:


fifa.sample(4)


# In[17]:


fifa[["Contract","Contract start","Contract End","Contract Length(years)"]].sample(4)


# In[18]:


# Creating contract categories
def categories (contract):
    if contract =="Free":
        return "Free"
    elif "On Loan" in contract:
        return "On Loan"
    else:
        return "Contract"

#Adding the contract status column
fifa.insert(fifa.columns.get_loc("Contract Length(years)")+1,"Contract Status",fifa["Contract"].apply(categories))
fifa.sample(3)
    


# In[19]:


fifa[["Contract","Contract start","Contract End","Contract Length(years)","Contract Status"]].sample(5)


# # 3.Height

# In[20]:


fifa["Height"].dtype


# In[21]:


def convert_height(height):
    if "cm" in height:
        return int(height.strip("cm"))
    else:
        feet,inches =height.split("'")
        total_inches = int(feet)*12 + int(inches.strip('"'))
        return round(total_inches * 2.54)
        
#Apllying the function in the height column
fifa["Height"] = fifa["Height"].apply(convert_height)
fifa["Height"].unique()     


# In[22]:


fifa["Height"].unique()


# In[23]:


#Renaming the Height column
fifa = fifa.rename(columns={"Height":"Height(cm)"})
fifa.sample(4)


# # 4.Weight

# In[24]:


fifa["Weight"].dtype


# In[25]:


fifa["Weight"].unique()


# In[26]:


def converting_weight(weight):
    if "kg" in weight:
        return int(weight.strip("kg"))
    else:
        pounds = int(weight.strip("lbs"))
        return round(pounds/2.205)
#Applying function to weight column
fifa["Weight"] = fifa["Weight"].apply(converting_weight)
fifa["Weight"].unique()
        


# In[27]:


#Renaming the Weight column in the database
fifa = fifa.rename(columns= {"Weight":"Weight(kg)"})
fifa.tail(n=5)


# # 5.Loan Date End

# In[28]:


fifa["Loan Date End"].dtype


# In[29]:


fifa["Loan Date End"].unique()


# In[30]:


on_loan = fifa[fifa["Contract Status"]=="On Loan"]
on_loan[["Contract","Contract Status","Loan Date End"]]


# # 6.w/f

# Players weak foot rating (out of 5)

# In[31]:


fifa["W/F"].dtype


# In[32]:


fifa["W/F"].unique()


# In[33]:


fifa["W/F"] = fifa["W/F"].str.replace("★","")
fifa["W/F"].unique()


# # 7.Hits

# In[34]:


fifa.head()
fifa["Hits"].unique()


# In[35]:


fifa["Hits"].unique()
fifa["Hits"].fillna(0, inplace=True)
fifa["Hits"].unique()


# # Dropping columns that are not needed

# In[54]:


fifa.head()
new_fifa = fifa.drop(columns =["photoUrl","playerUrl","LongName"])
new_fifa.head()


# # ANALYSIS

# # 1.Player analysis

# # 1.1 Which top 5 players has the highest overall rating (OVA)?

# In[56]:


new_fifa.head()


# In[70]:


new_fifa["↓OVA"].value_counts().tail(10)


# In[75]:


new_fifa.sort_values("↓OVA",ascending = False).head(10)


# # 1.2 Who is the youngest and the oldest player in the dataset

# In[77]:


new_fifa.head()


# In[92]:


new_fifa.sort_values("Age",ascending = True).head(3)


# In[101]:


new_fifa.value_counts("Age",ascending = True)


# In[87]:


new_fifa.sort_values("Age",ascending = False).head(3)


# # 1.3 What is the distribution of player ages?

# In[123]:


age_categories = {
    'Young-age': range(16, 25),
    'Middle-aged': range(26, 40),
    'Old-age': range(40, 60)}

def categorize_age(age):
    for category, age_range in age_categories.items():
        if age in age_range:
            return category
category_counts = new_fifa["categories"].value_counts().sort_index()
print(category_counts)


#  # 1.4 How many players prefer their left foot over their right foot

# In[166]:


new_fifa.head()


# In[169]:


new_fifa["Preferred Foot"].value_counts()


# # 1.5 What is the distribution of player heights and weights?

# In[177]:


new_fifa.head()


# In[182]:


round(new_fifa['Height(cm)'].describe())


# In[183]:


round(new_fifa["Weight(kg)"].describe())


# |           | Height(cm) | Weight(kg) |
# |-----------|------------|-----------|
# | Mean| 181| 75 |
# |Std  | 7  |7   |
# |Min  |155 |50
# |25%  |176 |70
# |50%  |181 |75
# |75%  |186 |80
# |Max  |206 |110
# 

# # 1.6 What is the most common nationality among players?

# In[184]:


new_fifa.head()


# In[186]:


new_fifa["Nationality"].value_counts()


# # 1.7 How many players are currently on loan?

# In[187]:


new_fifa.sample()


# In[189]:


new_fifa["Contract Status"].value_counts()


# # 2. Club

# # 2.1 Which club has the highest average OVA ?

# In[214]:


new_fifa.sample(n=3)


# In[213]:


new_fifa[['Club','↓OVA']]


# # 2.2 How many players does each club have?

# In[216]:


new_fifa.head(n=3)


# In[227]:


new_fifa["Club"].value_counts()


# In[229]:


new_fifa[new_fifa["Club"]=="No Club"].head()


# # 2.3 How many players from each club are on loan?

# In[249]:


len(new_fifa[new_fifa["Contract Status"] == "On Loan"])


# In[252]:


new_fifa[new_fifa["Contract Status"] == "On Loan"].groupby("Club").size()


# # 2.4 What are the most common positions played by the players?

# In[254]:


new_fifa.sample()


# In[258]:


new_fifa["Positions"].value_counts()


# # 3 Visualization

# # 3.1 visualize the distribution of player Age

# In[274]:


new_fifa.head(n=2)


# In[276]:


new_fifa["Age"].value_counts()


# In[273]:


new_fifa["Age"].value_counts().plot(kind = "bar")


# # 3.2 Pie chart to visualize the distribution of players contract

# In[281]:


new_fifa.sample()


# In[280]:


new_fifa["Contract Status"].value_counts()


# In[288]:


new_fifa["Contract Status"].value_counts().plot(kind = "pie",legend = True)


# In[ ]:





# In[ ]:




