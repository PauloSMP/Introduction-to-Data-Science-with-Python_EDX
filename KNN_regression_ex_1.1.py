import pandas as pd
import sklearn as sk




data  = pd.DataFrame({
    "TV": [230.1, 44.5, 17.2, 151.5, 180.8],
    "Radio": [37.8, 39.3, 45.9, 41.3, 10.8],
    "Newspaper": [69.2, 45.1, 69.3, 58.5, 58.4],
    "Sales": [22.1, 10.4, 9.3, 18.5, 12.9]
})

# Original DataFrame
print (data)
print (data.shape)
print (data.dtypes)
# Single column as Series
print (data["TV"])
print (data["TV"].shape)
print (data["TV"].dtypes)
# Single column as DataFrame
print (data[["TV"]])
print (data[["TV"]].shape)
print (data[["TV"]].dtypes)
