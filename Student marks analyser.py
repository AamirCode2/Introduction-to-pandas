import pandas as pd
 
print("================================")
print("student marks analyser")
print("================================")

 
print("Part 1: Pandas series")
 
marks = [88, 76, 92, 67, 85]
 
student_marks = pd.Series(
    marks,
    index=["aarav", "meera", "kabir", "anaya", "rohan"]
)
 
print(student_marks)

 
print("Part 2: Pandas dataFrame")
 
data = {
    "Student": ["aarav", "meera", "kabir", "anaya", "rohan"],
    "Math": [88, 76, 92, 67, 85],
    "Science": [91, 80, 89, 72, 87],
    "English": [84, 78, 95, 70, 82],
    "Attendance": [96, 90, 98, 85, 92]
}
 
df = pd.DataFrame(data)
 
print(df)

 
print("Part 3: Reading data from a CSV file")
 
df.to_csv("student_marks.csv", index=False)
 
student_data = pd.read_csv("student_marks.csv")
 
print("CSV file read successfully!")
print(student_data)
 

print("Part 4: viewing data")
 
print("First 3 rows:")
print(student_data.head(3))
 
print("Last 2 rows:")
print(student_data.tail(2))
 
print("Data information:")
print(student_data.info())

 
print("Part 5: Cleaning data")
 
messy_data = {
    "Student": ["aarav", "meera", "kabir", "anaya", "rohan"],
    "Math": [88, None, 92, 67, 85],
    "Science": [91, 80, None, 72, 87],
    "English": [84, 78, 95, None, 82]
}
 
messy_df = pd.DataFrame(messy_data)
 
print("Data with missing values:")
print(messy_df)
 
cleaned_df = messy_df.fillna(0)
 
print("Cleaned data:")
print(cleaned_df)
 
print("Part 6: Student total and average marks")
 
cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["Science"] + cleaned_df["English"]
cleaned_df["Average"] = cleaned_df["Total"] / 3
 
print(cleaned_df)

#i used a little help from the example on the bottom of the project description page