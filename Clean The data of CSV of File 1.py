# Drop all rows with NaN values from the DataFrame df1.

df1.dropna(inplace=True)
df1.info()

# Use the "lat-lon" column to create two separate columns in df1: "lat" and "lon". Make sure that the data type for these new columns is float

df1[["lat" , "lon"]] = df1["lat-lon"].str.split("," , expand=True).astype(float)
df1.head()
df1.info()

# Use the "place_with_parent_names" column to create a "state" column for df1. (Note that the state name always appears after "|Brasil|" in each string

df1["state"]=df1["place_with_parent_names"].str.split("|" , expand=True)[2]
df1.head()

#  Transform the "price_usd" column of df1 so that all values are floating-point numbers instead of strings

df1["price_usd"]=(
    df1["price_usd"]
    .str.replace("$" , "" , regex=False)
    .str.replace("," , "" , )
    .astype(float)
)

df1.info()

# Drop the "lat-lon" and "place_with_parent_names" columns from df1

df1.drop(columns=["place_with_parent_names" , "lat-lon"] , inplace=True)

