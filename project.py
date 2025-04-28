import numpy as np
import pandas as pd
#load the dataset
df = pd.read_csv("meghalayasoil.csv")
#basic EDA
print("Dataset Shape (Rows,Columns):",df.shape)
print("Column names:",df.columns.tolist())
print("Data type and non null counts:")
print(df.info())
print("Statitical Summary of numeric columns:")
print(df.describe(include="all"))


import numpy as np. 
import pandas as pd 
#load the dataset 
df pd.read_csv("meghalayasoil.csv") 
#check for missing values 
print("Missing Values in Bach columns:") 
print(df.isnull().sum()) 
#optionally: drop rows with too many missing values or fill them 
df_cleaned df.dropna () #or use dr.fillina (value) 
print("Shape After Removing Missing Values:", df cleaned.shape)


import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
#load the dataset 
df = pd.read_csv("meghalayasoil.csv") 
#Clean column names (remove leading/trailing spaces) 
df.columns = df.columns.str.strip() 
#1 data cleaning 
print("Missing Values:\n",df.isnull().sum()) 
print("\nDuplicate Rows:",df.duplicated().sum()) 
df.drop_duplicates (inplace=True) 
#2. descriptive Statitics 
print("\nDataset Overview") 
df.info() 
print("\nStatical Summary:") 
print(df.describe()) 
#3. Top 5 highest Moister Level 
print("\nTop 5 moister level:") 
print(df.sort_values (by="Volume Soil-moisture percentage (at 15cm)", ascending=False).head())



import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 
#Load dataset 
df = pd.read_csv("meghalayasoil.csv") 
sns.set(style="whitegrid") 
plt.figure(figsize=(12, 6)) 
sns.boxplot( 
    x='srcDistrictName', 
    y='Average Soil-moisture Level (at 15cm)', 
    data=df, 
    palette='YlGn'
)
plt.title('Soil Moisture Distribution Across Districts') 
plt.xlabel('District') 
plt.ylabel('Average Soil Moisture Level (at 15cm)') 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show()


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
df=pd.read_csv("meghalayasoil.csv") 
sns.set(style="whitegrid") 
plt.figure(figsize=(12, 6)) 
sns.violinplot( 
x='srcDistrictName', 
y='Average Soil-moisture Level (at 15cm)', 
data=df, 
palette='pastel', 
inner-'quartile' 
) 
plt.title('Soil Moisture Variation by District') 
plt.xlabel('District') 
plt.ylabel('Average Soil Moisture Level (at 15cm)') 
plt.xticks(rotation=45) 
plt.tight layout() 
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("meghalayasoil.csv")

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Date'])

daily_avg = df.groupby('Date')['Average Soil-moisture Level (at 15cm)'].mean().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(daily_avg['Date'], daily_avg['Average Soil-moisture Level (at 15cm)'], color='teal', linewidth=2)

plt.title('Trend of Average Soil Moisture Over Time')
plt.xlabel('Date')
plt.ylabel('Average Soil Moisture Level (at 15cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("meghalayasoil.csv")
# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
daily_avg = df.groupby('Date')['Average Soil-moisture Level (at 15cm)'].mean().reset_index()
plt.figure(figsize=(12, 5))
plt.plot(daily_avg['Date'], daily_avg['Average Soil-moisture Level (at 15cm)'], color='teal', linewidth=2)
plt.title('Trend of Average Soil Moisture Over Time')
plt.xlabel('Date')
plt.ylabel('Average Soil Moisture Level (at 15cm)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()



