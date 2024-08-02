# Before you move to the next task, take a moment to inspect df1 using the info and head methods. What issues do you see in the data? 
# What cleaning will you need to do before you can conduct your analysis?

df1.info()
df1.head()

# Output

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12834 entries, 0 to 12833
Data columns (total 6 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   property_type            12834 non-null  object 
 1   place_with_parent_names  12834 non-null  object 
 2   region                   12834 non-null  object 
 3   lat-lon                  11551 non-null  object 
 4   area_m2                  12834 non-null  float64
 5   price_usd                12834 non-null  object 
dtypes: float64(1), object(5)
memory usage: 601.7+ KB

   property_type 	place_with_parent_names	    region	           lat-lon	           area_m2	      price_usd
0	apartment	 |Brasil|Alagoas|Maceió|	   Northeast	-9.6443051,-35.7088142	    110.0	       $187,230.85
1	apartment	 |Brasil|Alagoas|Maceió|       Northeast	-9.6430934,-35.70484	    65.0	       $81,133.37
2	house	     |Brasil|Alagoas|Maceió|	   Northeast	-9.6227033,-35.7297953	    211.0	       $154,465.45
3	apartment	 |Brasil|Alagoas|Maceió|	   Northeast	-9.622837,-35.719556	     99.0	       $146,013.20
4	apartment	 |Brasil|Alagoas|Maceió|       Northeast	-9.654955,-35.700227	     55.0	       $101,416.71

#_____________________________________________________________________________________________________________________________
# Drop all rows with NaN values from the DataFrame df1.

df1.dropna(inplace=True)
df1.info()

#output

<class 'pandas.core.frame.DataFrame'>
Int64Index: 11551 entries, 0 to 12833
Data columns (total 6 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   property_type            11551 non-null  object 
 1   place_with_parent_names  11551 non-null  object 
 2   region                   11551 non-null  object 
 3   lat-lon                  11551 non-null  object 
 4   area_m2                  11551 non-null  float64
 5   price_usd                11551 non-null  object 
dtypes: float64(1), object(5)
memory usage: 631.7+ KB
#______________________________________________________________________________________________________________________________________________
# Use the "lat-lon" column to create two separate columns in df1: "lat" and "lon". Make sure that the data type for these new columns is float

df1[["lat" , "lon"]] = df1["lat-lon"].str.split("," , expand=True).astype(float)
df1.info()

# output

<class 'pandas.core.frame.DataFrame'>
Int64Index: 11551 entries, 0 to 12833
Data columns (total 8 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   property_type            11551 non-null  object 
 1   place_with_parent_names  11551 non-null  object 
 2   region                   11551 non-null  object 
 3   lat-lon                  11551 non-null  object 
 4   area_m2                  11551 non-null  float64
 5   price_usd                11551 non-null  object 
 6   lat                      11551 non-null  float64
 7   lon                      11551 non-null  float64
dtypes: float64(3), object(5)
memory usage: 812.2+ KB
#_________________________________________________________________________________________________________________________________________________________
# Use the "place_with_parent_names" column to create a "state" column for df1. (Note that the state name always appears after "|Brasil|" in each string

df1["state"]=df1["place_with_parent_names"].str.split("|" , expand=True)[2]
df1.head()

# output

	property_type	 place_with_parent_names	region	       lat-lon	              area_m2	    price_usd	    lat         	lon	        state
0	apartment	   |Brasil|Alagoas|Maceió|	  Northeast	   -9.6443051,-35.7088142	  110.0	       $187,230.85	   -9.644305	-35.708814   	Alagoas
1	apartment	   |Brasil|Alagoas|Maceió|	  Northeast	   -9.6430934,-35.70484	       65.0	        $81,133.37	   -9.643093	-35.704840	    Alagoas
2	house	       |Brasil|Alagoas|Maceió|    Northeast	   -9.6227033,-35.7297953	   211.0	    $154,465.45	   -9.622703	-35.729795	    Alagoas
3	apartment	   |Brasil|Alagoas|Maceió|	  Northeast	   -9.622837,-35.719556	       99.0	        $146,013.20	   -9.622837	-35.719556	    Alagoas
4	apartment	   |Brasil|Alagoas|Maceió|	  Northeast	   -9.654955,-35.700227	       55.0	        $101,416.71	   -9.654955	-35.700227  	Alagoas
#__________________________________________________________________________________________________________________________________________________________
#  Transform the "price_usd" column of df1 so that all values are floating-point numbers instead of strings

df1["price_usd"]=(
    df1["price_usd"]
    .str.replace("$" , "" , regex=False)
    .str.replace("," , "" , )
    .astype(float)
)

df1.info()

#output
<class 'pandas.core.frame.DataFrame'>
Int64Index: 11551 entries, 0 to 12833
Data columns (total 9 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   property_type            11551 non-null  object 
 1   place_with_parent_names  11551 non-null  object 
 2   region                   11551 non-null  object 
 3   lat-lon                  11551 non-null  object 
 4   area_m2                  11551 non-null  float64
 5   price_usd                11551 non-null  float64
 6   lat                      11551 non-null  float64
 7   lon                      11551 non-null  float64
 8   state                    11551 non-null  object 
dtypes: float64(4), object(5)
memory usage: 902.4+ KB
#____________________________________________________________________________________________________________________
# Drop the "lat-lon" and "place_with_parent_names" columns from df1

df1.drop(columns=["place_with_parent_names" , "lat-lon"] , inplace=True)
df1.head()

#output
     property_type      	region	     area_m2	   price_usd	      lat	    lon	         state
0	  apartment	           Northeast	 110.0	       187230.85	  -9.644305	  -35.708814	Alagoas
1	  apartment	           Northeast	 65.0	        81133.37	  -9.643093	  -35.704840	Alagoas
2	  house	               Northeast	 211.0	        154465.45	  -9.622703	  -35.729795	Alagoas
3	  apartment            Northeast	 99.0	        146013.20	  -9.622837	  -35.719556	Alagoas
4	  apartment	           Northeast	 55.0	        101416.71	  -9.654955	  -35.700227	Alagoas


