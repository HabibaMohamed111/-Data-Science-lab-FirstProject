# Import Matplotlib, pandas, and plotly

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

#Import the CSV file data/brasil-real-estate-1.csv into the DataFrame df1.

df1 =pd.read_csv("data/brasil-real-estate-1.csv")
df1.head()

# OutPut

	property_type	 place_with_parent_names	 region	         lat-lon	        area_m2	   price_usd
0 	apartment	  |Brasil|Alagoas|Maceió|	  Northeast	 -9.6443051,-35.7088142 	110.0	  $187,230.85
1	 apartment	  |Brasil|Alagoas|Maceió|	  Northeast	 -9.6430934,-35.70484	    65.0	  $81,133.37
2	 house	      |Brasil|Alagoas|Maceió|	  Northeast	 -9.6227033,-35.7297953 	211.0	  $154,465.45
3 	apartment	  |Brasil|Alagoas|Maceió|	  Northeast	 -9.622837,-35.719556	   99.0	    $146,013.20
4	 apartment	  |Brasil|Alagoas|Maceió| 	Northeast	 -9.654955,-35.700227	   55.0	    $101,416.71
