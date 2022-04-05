# -Assignment5
1202 Data Analysis Tools Analytics
# Introducion

The first step in creating a function that determines the distribution of
channetype data in a given data set for the top 1000 records is to import the top 1000
records into a new df1 variable in the jupyter notebook.

df1=df.head(1000)
After that, We created function called histogram_function which creates a
distribution visualization of channeltype data.
def histogram_function():

print(df_count)

fig=plt.figure(figsize=(20,20))

plt.hist(df1['channeltype'],bins=15)

plt.gca().set(title='Frequency Histogram of Channel Type',

ylabel='Frequency')

We specified the function name with def histogram_function (), and then used
the plt.hist function to visualise the histogram frequency distribution. In addition, the
axis should be labelled, and the histogram should be given a title.

Using the python script below, we imported the top 1000 records into a
separate csv file called "100 records.csv".
df1.to_csv('1000_records.csv')

