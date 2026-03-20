# # ==============================
# # IMPORT LIBRARIES
# # ==============================
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Seaborn style
# sns.set()

# # ==============================
# # NUMPY (Numerical Operations)
# # ==============================
# print("----- NUMPY -----")

# arr = np.array([10, 20, 30, 40, 50])
# print("Array:", arr)

# print("Mean:", np.mean(arr))
# print("Sum:", np.sum(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))

# arr2 = np.arange(1, 10).reshape(3, 3)
# print("2D Array:\n", arr2)

# # ==============================
# # PANDAS (Data Handling)
# # ==============================
# print("\n----- PANDAS -----")

# data = {
#     "Name": ["A", "B", "C", "D", "E"],
#     "Marks": [85, 90, 78, 92, 88],
#     "Age": [20, 21, 19, 22, 20]
# }

# df = pd.DataFrame(data)

# print("DataFrame:\n", df)

# print("\nDescribe:\n", df.describe())

# # ==============================
# # SEABORN VISUALIZATION
# # ==============================
# print("\n----- SEABORN -----")

# # Line Plot
# plt.figure()
# sns.lineplot(x="Name", y="Marks", data=df)
# plt.title("Marks Line Chart")
# plt.show()

# # Bar Plot
# plt.figure()
# sns.barplot(x="Name", y="Marks", data=df)
# plt.title("Marks Bar Chart")
# plt.show()

# # Scatter Plot
# plt.figure()
# sns.scatterplot(x="Age", y="Marks", data=df)
# plt.title("Age vs Marks")
# plt.show()

# # Histogram
# plt.figure()
# sns.histplot(df["Marks"], kde=True)
# plt.title("Marks Distribution")
# plt.show()

# # Box Plot
# plt.figure()
# sns.boxplot(x="Marks", data=df)
# plt.title("Box Plot of Marks")
# plt.show()

# # ==============================
# # HEATMAP (Correlation)
# # ==============================
# plt.figure()
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True)
# plt.title("Correlation Heatmap")
# plt.show()




# # ==============================
# # IMPORT LIBRARIES
# # ==============================
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Seaborn style
# sns.set()

# # ==============================
# # NUMPY (Numerical Operations)
# # ==============================
# print("----- NUMPY -----")

# arr = np.array([10, 20, 30, 40, 50])
# print("Array:", arr)

# print("Mean:", np.mean(arr))
# print("Sum:", np.sum(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))

# arr2 = np.arange(1, 10).reshape(3, 3)
# print("2D Array:\n", arr2)

# # ==============================
# # PANDAS (Data Handling)
# # ==============================
# print("\n----- PANDAS -----")

# data = {
#     "Name": ["A", "B", "C", "D", "E"],
#     "Marks": [85, 90, 78, 92, 88],
#     "Age": [20, 21, 19, 22, 20]
# }

# df = pd.DataFrame(data)

# print("DataFrame:\n", df)

# print("\nDescribe:\n", df.describe())

# # ==============================
# # SEABORN VISUALIZATION
# # ==============================
# print("\n----- SEABORN -----")

# # Line Plot
# plt.figure()
# sns.lineplot(x="Name", y="Marks", data=df)
# plt.title("Marks Line Chart")
# plt.show()

# # Bar Plot
# plt.figure()
# sns.barplot(x="Name", y="Marks", data=df)
# plt.title("Marks Bar Chart")
# plt.show()

# # Scatter Plot
# plt.figure()
# sns.scatterplot(x="Age", y="Marks", data=df)
# plt.title("Age vs Marks")
# plt.show()

# # Histogram
# plt.figure()
# sns.histplot(df["Marks"], kde=True)
# plt.title("Marks Distribution")
# plt.show()

# # Box Plot
# plt.figure()
# sns.boxplot(x="Marks", data=df)
# plt.title("Box Plot of Marks")
# plt.show()

# # ==============================
# # HEATMAP (Correlation)
# # ==============================
# plt.figure()
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True)
# plt.title("Correlation Heatmap")
# plt.show()




# import seaborn as sns 
# import matplotlib.pyplot as plt
# import numpy as np

# data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
# plot=['histogram','KERNAL_DENSITY']
# for plots in plot:
#     if plots =='Histogram':
#         sns.histplot(data)
#         plt.title("Histogram chart")
#         plt.show()
#     elif plots =='KERNAL_DENSITY':
#         sns.kdeplot(data)
#         plt.title("KERNAL_DENSITY")
#         plt.show()

# data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
# plot=['histogram','KERNAL_DENSITY']
# for plots in plot:
#     if plots =='Histogram':
#         sns.histplot(data)
#         plt.title("Histogram chart")
#         plt.show()
#     elif plots =='KERNAL_DENSITY':
#         sns.kdeplot(data)
#         plt.title("KERNAL_DENSITY")
#         plt.show()
# data1=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
# data2=[11,14,3,14,25,67,31,23,64,65,64,84,44,65,56,0,23,43,69,1,2,34,45]
# data3=[11,14,3,4,5,67,31,3,64,5,4,84,44,65,56,0,23,43,69,1,2,34,45]
# group=[data1,data2,data3]
# sns.violinplot(data=group)
# plt.title("example of violin plot")
# plt.show()


# ******************************************************************



# import seaborn as sns
# import matplotlib.pyplot as plt 
# import pandas as pd
# data={'advertisement':[1,2,3,4,6,7,9,10],
#      'sales':[5,8,7,8,10,11,12,22],
#      'temerature':[22,21,33,35,36,37,39,40]}
# df=pd.DataFrame(data)
# sns.scatterplot(x="advertisement",y="sales",data=df)
# plt.show()

# sns.scatterplot(x="advertisement",y="sales",data=df)
# plt.title("advertisement and sales scattering chart")
# plt.show()
# data={'advertisement':[1,2,3,4,6,7,9,10],
#      'sales':[5,8,7,8,10,11,12,22],
#      'temerature':[22,21,33,35,16,21,20,20]}
# coorelation_matrix=df.corr()
# sns.heatmap(coorelation_matrix,annot=True,cmap='coolwarm',fmt='.2f')
# plt.show()