import pandas as pd
import plotly.express as px

#extract data

gas_inflation_data = pd.read_excel("data/energy (1).xlsx", "Gas inflation")
gas_inflation_data= gas_inflation_data[4:]
gas_inflation_data.columns=gas_inflation_data.iloc[0]
gas_inflation_data = gas_inflation_data.iloc[1:]
print(gas_inflation_data.columns)


motor_fuel = pd.read_excel("data/energy (1).xlsx", "Motor fuel inflation")

motor_fuel=motor_fuel[4:]
motor_fuel.columns=motor_fuel.iloc[0]
motor_fuel = motor_fuel.iloc[1:]
print(motor_fuel.columns)
inflation_df = pd.merge(right=gas_inflation_data, left=motor_fuel, how="outer", on=["Date "])


inflation_df_melt=pd.melt(inflation_df, id_vars="Date ", value_vars=["Motor fuels","Gas "])
print(inflation_df_melt)

fig = px.line(inflation_df_melt, x="Date ", y="value", color=4, title="Fuel Inflation 2012-2023", labels={"4": "Fuel"})

fig.show()