import pandas as pd
from functions import combine_nps_csvs, calculate_nps, calculate_nps_by_source

mobile = "datasets/nps_mobile.csv"
web = "datasets/nps_web.csv"
email = "datasets/nps_email.csv"

dict_csv = {mobile: "mobile", web: "web", email: "email"}


""" 
To make sure our code is scalable, we're going to write a function
called combine_nps_csvs() that takes in a dictionary. 
In our case, the CSV's name and source type will be the key and value, respectively.
That way, we can define a dictionary with as many NPS files as we have and run it through combine_nps_csvs()
"""

combined_csvs = combine_nps_csvs(dict_csv)
print(combined_csvs)


""" 
Now we're in a good place to calculate the Net Promoter Score!
This is calculated by subtracting the percentage of detractor ratings from the percentage of promoter ratings.
"""
nps = calculate_nps(combined_csvs)
print(nps)


"""
The product team concludes that majorly increasing NPS across customer base is a priority. 
Luckily, we have this NPS data that we can analyze more so we can find data-driven solutions. 
A good start would be breaking down the NPS score by the source type. For instance, 
if people are rating lower on the web than mobile, that's some evidence we need to improve the browser experience.
"""
nps_by_source = calculate_nps_by_source(combined_csvs)
print(nps_by_source)





