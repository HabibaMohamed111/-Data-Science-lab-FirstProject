# Complete the code below to create a scatter_mapbox showing the location of the properties in df

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": -14.2, "lon": -51.9},  # Map will be centered on Brazil
    width=600,
    height=600,
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)
​
fig.update_layout(mapbox_style="open-street-map")
fig.show()

# Use the describe method to create a DataFrame summary_stats with the summary statistics for the "area_m2" and "price_usd" columns.

summary_stats = df[["area_m2" , "price_usd"]].describe()
summary_stats

# Create a histogram of "price_usd". Make sure that the x-axis has the label "Price [USD]", the y-axis has the label "Frequency",
#  and the plot has the title "Distribution of Home Prices". Use Matplotlib (plt).

# Build histogram
plt.hist(df["price_usd"])

# Label axes
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")

# Add title
plt.title("Distribution of Home Prices");

# Create a horizontal boxplot of "area_m2". Make sure that the x-axis has the label "Area [sq meters]"
#  and the plot has the title "Distribution of Home Sizes". Use Matplotlib (plt).

# Build box plot
plt.boxplot(df["area_m2"] , vert=False)
​
# Label x-axis
plt.xlabel("Area [sq meters]")
​
# Add title
plt.title("Distribution of Home Sizes");

# Use the groupby method to create a Series named mean_price_by_region that shows the mean home price 
# in each region in Brazil, sorted from smallest to largest.

mean_price_by_region =df.groupby("region") ["price_usd"].mean()
mean_price_by_region

# Use mean_price_by_region to create a bar chart. Make sure you label the x-axis as "Region" 
# and the y-axis as "Mean Price [USD]", and give the chart the title "Mean Home Price by Region". Use pandas.

# Build bar chart, label axes, add title
mean_price_by_region.plot(
    kind="bar",
    xlabel="Region",
    ylabel="Mean Price [USD]",
    title="Mean Home Price by Region"
)

# Create a DataFrame df_south that contains all the homes from df that are in the "South" region.

df_south =df[df["region"] == "South"]
df_south.head()

# Use the value_counts method to create a Series homes_by_state that contains the number of properties in each state in df_south.

homes_by_state =df_south["state"].value_counts()
homes_by_state

# Create a scatter plot showing price vs. area for the state in df_south that has the largest number of properties.
# Be sure to label the x-axis "Area [sq meters]" 
# and the y-axis "Price [USD]"; and use the title "<name of state>: Price vs. Area". Use Matplotlib (plt)

# Subset data
df_south_rgs =df_south[df_south["state"]=="Rio Grande do Sul"]

# Build scatter plot
plt.scatter(x=df_south_rgs["area_m2"] , y=df_south_rgs["price_usd"])

# Label axes
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]]")

# Add title
plt.title("Rio Grande do Sul: Price vs. Area");

# reate a dictionary south_states_corr, where the keys are the names of the three states in the "South" region of Brazil,
# and their associated values are the correlation coefficient between "area_m2" and "price_usd" in that state

south_states = ['Paraná', 'Santa Catarina', 'Rio Grande do Sul']
south_states_corr = {}
for state in south_states:
    state_data = df[df['state'] == state]
    correlation = state_data['area_m2'].corr(state_data['price_usd'])
    south_states_corr[state] = correlation
south_states_corr

# output

{'Paraná': 0.5436659935502659,
 'Santa Catarina': 0.5068121769989853,
 'Rio Grande do Sul': 0.5773267433871903}

​
