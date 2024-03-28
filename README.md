# FIFA-PROJECT
## Data -Fifa dataset with over 5000 rows 
## Data cleaning - Jupyter Notebook
## Tools - Pandas, python, Numpy, Matplotlib.
# PROJECT OVERVIEW
The provided dataset contains information about football (soccer) players, including various attributes that describe their characteristics, abilities, and career details. The data is typically sourced from football databases .The dataset offers a comprehensive view of individual players, encompassing their personal details, physical attributes, performance ratings, and contract information.
# PROJECT CLEANING
This is the process i took to ensure my data is clean and ready for analysing:
- Starting with the Club column the values had characters that were unnecessary and I had to drop them and after stripping them the values were now clean and visible easily.
- The contract column had different values where some players were free,others on loan and the rest had effective contracts.
- The players had to be differentiated using the contract status to get the glimpse of where each player belonged in terms of contract
- The players who had active contracts ,I calculated their contract length in years .  
- The height column had different values where some players height was in "cm" while others were just integers making pandas interpret the values as strings.
- I started by striping the “cm” in the values so as they can be uniform with values that do not have the cm 
- After all the values were the same i changed the date type from string to integers.
- Some players had their Weight in “kg '' while others had their weight in ‘lbs'
- Ideally the Weight should be the datatype of integers but in this case the weight were objects ,so to solve this I had to strip the “kg” in the values that had kg.
- Some of the values were “lbs” that is in pounds I first had to strip the lbs to be left with a value
- With only the value to convert to kg I had the pounds divided by 2.205 and then changed the whole data type to integer .
- When checking the data info i noticed the column “Loan Date End” had less values and they were in object datatype of which i would expect it to be dates , to determine why i checked the values and since i had - cleaned the contract column the players that were on loan were the ones that had the “Load  Date End’ values , the rest were either free or completing year.This explains the less values and the NaN values.
- The weak foot rating column W/F had values accompanied with a star. I replaced that to drop the star.
- The Hits column had missing values which I replaced with zero
# ANALYSING QUESTIONS

 *Players analysis*
- Which top 5 players has the highest overall rating (OVA)?
- Who is the youngest and the oldest player in the dataset?
- What is the distribution of player ages?
- How many players prefer their left foot over their right foot?
- What is the distribution of players heights and weights?
- What is the most common nationality among players?
- How many players are currently on loan?
  
 *Club analysis*    
- Which club has the highest average OVA?
- How many players does each club have?
- How many players from each team are on loan?
- What are the most common positions played by the players?
  # FINDINGS
- L.messi and Christano Ronaldo have the highest overall rating of 93 and 92 respectively.
- Most players have a tie when it comes to the overall rating , we have four players with a rating of 91 ,they are J.Oblak,K.De Bruyne,Neymar Jr and Rlewandowski.
- We have over 35 players with the youngest age of 16 while the oldest is K.Miura  the at age of 35.
- When it comes to the distribution of the players' ages ,we have over 8515 middle aged with a range of 26 to 40 years ,the young aged players are 9198 with a range of 16 to 25 years and lastly we only have 27 players with a range of 40 to 60 years.
- Over 14445 players prefer their Right foot while 4534 prefer the left foot.
- This is the breakdown of the Height and Weight distribution:
  
| Descriptor | Height (cm) | Weight (kg) |
|------------|-------------|-------------|
| Mean       | 181         | 75          |
| Std        | 7           | 7           |
| Min        | 155         | 50          |
| 25%        | 176         | 70          |
| 50%        | 181         | 75          |
| 75%        | 186         | 80          |
| Max        | 206         | 110         |


- Most players are from England with a count of 1705 players followed by Germany with 1195 players.
- 1013 players are on Loan ,17729 players are on Contract and 237 are Free.
- FC Barcelona has the highest average OVA of 93 .
- Most players have No Club, total of 237 have No Club whereas 33 players belong to FC Barcelona tieng with Burnley and others.
- There are 1013 players who are On Loan contracts.
- The most common played position by the players is Center Back (CB) with 2441 players followed by Goalkeeper (GK) with 2074 players.
  
# VISUALIZATION
- After cleaning ,transforming and analyzing the data I was curious about the visualization of the distribution of players age,using the plot function and choosing the kind of visualization style of a bar chart I was able to come up with the bar chart of the distribution of age among the players.
- Using a pie chart i was able to visualize the distribution  of players contract.
# LIMITATION
-  Inconsistencies in data formats across different columns due to this,columns had to be modified.
- Some columns were added for better viewing of the data
- Some columns were dropped .
- Alot of values had to changed due to their data types.



