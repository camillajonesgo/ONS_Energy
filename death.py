#imports

import pandas as pd
import plotly.express as px

#extract data

business_death_quarterly_geo = pd.read_excel("data/finalq42022qdemtables.xlsx", "Deaths Geography Counts")
business_death_quarterly_geo  = business_death_quarterly_geo .iloc[2:]
business_death_quarterly_geo.columns=business_death_quarterly_geo.iloc[0]
business_death_quarterly_geo = business_death_quarterly_geo .iloc[1:]

print(business_death_quarterly_geo)


business_death_2023=pd.read_excel("data/finalq22023lowlevelgeobreakdown.xlsx", "Deaths 2022-2023")

business_death_2023 = business_death_2023.iloc[2:]
business_death_2023.columns=business_death_2023.iloc[0]
business_death_2023 = business_death_2023.iloc[1:]
business_death_2023= business_death_2023.replace(to_replace='^(.*?): ', value ='', regex=True)


# remove unwanted rows
rows_to_keep=['United Kingdom', 'Great Britain', 'England and Wales',
       'England', 'North East', 'North West', 'Yorkshire and The Humber',
       'East Midlands', 'West Midlands', 'East', 'London', 'South East',
       'South West', 'Wales', 'Scotland', 'Northern Ireland', 'Unspecified']

business_death_2023= business_death_2023[business_death_2023['Geography'].isin(rows_to_keep)]

business_death_2023=business_death_2023.transpose()
business_death_2023=business_death_2023.reset_index()
business_death_2023.columns=business_death_2023.iloc[0]
business_death_2023 = business_death_2023.iloc[1:]

business_death_2023=business_death_2023.rename(columns={"Geography": "Quarter"})

business_death_quarterly_geo= business_death_quarterly_geo[:-4]

frames=[business_death_quarterly_geo, business_death_2023]
business_death_quarterly_geo=pd.concat(frames)


#data visualtion
business_death_quarterly_geo_melt=pd.melt(business_death_quarterly_geo, id_vars=["Quarter"], value_vars=[ 'United Kingdom', 'Great Britain', 'England and Wales',
       'England', 'North East', 'North West', 'Yorkshire and The Humber',
       'East Midlands', 'West Midlands', 'East', 'London', 'South East',
       'South West', 'Wales', 'Scotland', 'Northern Ireland', 'Unspecified'])
#print(business_birth_quarterly_geo_melt)
fig = px.line(business_death_quarterly_geo_melt, x="Quarter", y="value", color="variable", title="Business Death by Quarter", labels={"variable": "Area"})

fig.show()