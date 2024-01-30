## The final project of the advanced training for Data Analysts:
### Development of a model for the prediction of the apartment price

**The main idea:**
>build a model to predict the cost of the apartment.

**Tasks:**
>Search for patterns in data.
>
>Perform a data visualization.
>
>Create a data hypothesis and perform a hypothesis check.
>
>Interpret the results obtained.

**Data cleaning:**
>Different format values and many data are not available in the source data.
>
>The missing and abnormal values were replaced with modal values during data pre-processing. 
>In the graph «number of parks in a radius of 3 km» unique statistically significant values are not found.
>
>As a result, significant parameters have been selected, based on which hypotheses will be built and tested.
>
>The parameters of «price at the time of withdrawal» and «apartment area(m<sup>2</sup>) have a high correlation, which allowed the addition of a new parameter «cost of m<sup>2</sup>», necessary for the prediction of the price of the apartment.

**Research data analysis:**
>Based on significant parameters, hypotheses were proposed:
>
>1. Prices for apartments in the center and far from the center are significantly different
>
>2. Prices for apartments near the water body and far from the water body differ significantly
>
>3. Prices for apartments with a large and small kitchen differ significantly
>
>4: Prices of apartments with high and low ceilings differ significantly
>
>5: Prices for apartments in houses with floors more and less than 5 floors differ significantly
>
>6: prices for apartments on the ground floor from apartments on other floors differ significantly
>
>7: prices for apartments with different number of rooms differ significantly
>
>**All the hypotheses put forward were accepted as a result of statistical analysis.**

**Prediction:**
>Not all parameters have been taken for estimating the price of the apartment, as when they are taken into account, the sample of data becomes unaffordable, and some parameters have ambiguous attitudes on the part of the user.
>
>The price of the apartment is calculated based on a cut-down sample created based on the parameters of the search of the apartment (total area, number of rooms, kitchen area, distance from the center). It is issued as a range from the lowest to the highest value of the apartment under these parameters.
>
>>**Example:**
>>
>>Situation: A family with kids needs a new apartment with 3 rooms near the city center. The total area is about 70 m<sup>2</sup>, the kitchen area is about 10 m<sup>2</sup>.
>>
>>Prediction:
>>
>>What is the total area of the apartment (in m2)?
>>>70
>>>
>>How many rooms in the apartment?
>>Enter values from 0 to 5
>>Enter 0 if this is a studio apartment
>>>3
>>>
>>What is the area of the kitchen (in m2)?
>>>10
>>>
>>How far is the apartment from the center (m)?
>>Enter 99999, if information does not exist
>>>3000
>>>
>>**Prognosed cost of the apartment from 2.513 to 10.044 million rubles**

**Conclusion:**
>As a result of the work, it was noted that the following parameters correlate with the value of the apartment: area of the apartment in square meters (m<sup>2</sup>), number of rooms, height of ceilings (m), total floors, living area in square meters (m²), floor, kitchen area in square meters (m<sup>2</sup>), distance to the city center (m), number of bodies of water in a radius of 3 km.
>
>A heat map illustrates the correlation of the data concerned.
>
>Based on the examination of the hypotheses put forward, it was possible to prove that the previously noted parameters affect the price of the apartment. However, not all the influencing parameters were used to forecast the price of the apartment.
>As a model for forecasting the cost of the apartment, a function calculating the range of possible value of the apartment, taking into account the wishes of the user, has been proposed.





