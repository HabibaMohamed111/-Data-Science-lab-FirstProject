# Import the CSV file brasil-real-estate-2.csv into the DataFrame df2.

df2 =pd.read_csv("data/brasil-real-estate-2.csv")
df2.head()
df2.info()

# output

    property_type	   state   	   region	       lat	        lon	     area_m2	  price_brl
0	  apartment     Pernambuco	  Northeast	   -8.134204	-34.906326	  72.0	   414222.98
1	  apartment   	Pernambuco	  Northeast    -8.126664	-34.903924	  136.0	   848408.53
2	 apartment	    Pernambuco	  Northeast	   -8.125550	-34.907601	  75.0	   299438.28
3	 apartment	    Pernambuco	  Northeast	   -8.120249	-34.895920	  187.0	   848408.53
4	 apartment	    Pernambuco	  Northeast  	 -8.142666	-34.906906	  80.0	   464129.36

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12833 entries, 0 to 12832
Data columns (total 7 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   property_type  12833 non-null  object 
 1   state          12833 non-null  object 
 2   region         12833 non-null  object 
 3   lat            12833 non-null  float64
 4   lon            12833 non-null  float64
 5   area_m2        11293 non-null  float64
 6   price_brl      12833 non-null  float64
dtypes: float64(4), object(3)
memory usage: 701.9+ KB
#----------------------------------------------------------------------------------------------------------------------------

# Use the "price_brl" column to create a new column named "price_usd". 
# (Keep in mind that, when this data was collected in 2015 and 2016, a US dollar cost 3.19 Brazilian reals.)

df2["price_usd"] = (df2["price_brl"] / 3.19).round(2)
df2.head()

# output

      property_type	    state	      region	       lat	        lon	     area_m2	     price_brl	 price_usd
0	    apartment	      Pernambuco	Northeast	     -8.134204	-34.906326	  72.0	       414222.98	  129850.46
1	    apartment	      Pernambuco	Northeast	     -8.126664	-34.903924	  136.0	       848408.53	  265958.79
2	    apartment     	Pernambuco	Northeast	     -8.125550	-34.907601	  75.0	       299438.28	  93867.80
3	    apartment	      Pernambuco	Northeast	     -8.120249	-34.895920	  187.0	       848408.53	  265958.79
4	    apartment	      Pernambuco	Northeast	     -8.142666	-34.906906	  80.0	       464129.36	  145495.10
#-------------------------------------------------------------------------------------------------------------------------------
# Drop the "price_brl" column from df2, as well as any rows that have NaN values.

df2.drop(columns=["price_brl"] , inplace=True)
df2.dropna(inplace=True)
df2.info()

# output

<class 'pandas.core.frame.DataFrame'>
Int64Index: 11293 entries, 0 to 12832
Data columns (total 7 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   property_type  11293 non-null  object 
 1   state          11293 non-null  object 
 2   region         11293 non-null  object 
 3   lat            11293 non-null  float64
 4   lon            11293 non-null  float64
 5   area_m2        11293 non-null  float64
 6   price_usd      11293 non-null  float64
dtypes: float64(4), object(3)
memory usage: 705.8+ KB
#------------------------------------------------------------------------------------------------------------------------------------------
# Concatenate df1 and df2 to create a new DataFrame named df.

df =pd.concat([df1,df2])
print("df shape:", df.shape)

# output
df shape: (22844, 7)
