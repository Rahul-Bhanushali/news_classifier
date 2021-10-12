# news_classifier
In today’s world, data is power. With News companies having terabytes of data stored in servers, everyone is in the quest to discover insights that add value to the organization. With various examples to quote in which analytics is being used to drive actions, one that stands out is news article classification. Nowadays on the Internet there are a lot of sources that generate immense amounts of daily news. In addition, the demand for information by users has been growing continuously, so it is crucial that the news is classified to allow users to access the information of interest quickly and effectively. This way, the machine learning model for automated news classification could be used to identify topics of untracked news and/or make individual suggestions based on the user’s prior interests.

**Objective: **
To build a solution that should recognize and classify the news articles based on their labels.
 
**Benefits:**
Easy and fast classification of news articles for better user experience.


**Data Sharing Agreement :**
Sample file name (ex news_20062021_101010)
Length of ArticleId (8 digits)
Number of Columns
Column names 
Column data type


**Architecture**
![image](https://user-images.githubusercontent.com/83774739/136933364-4c35322a-7c02-4f16-b724-a236c7e6809a.png)


**Data Validation and Data Transformation :**
Name Validation - Validation of files name as per the DSA. We have created a regex pattern for validation. After it checks for date format and time format if these requirements are satisfied, we proceed else, we reject the file.
Number of Columns – Validation of number of columns present in the files, and if it doesn't match then the file is rejected.
Name of Columns - The name of the columns is validated and should be the same as given in the schema file. If not, then the file is rejected.
Data type of columns - The data type of columns is given in the schema file. It is validated when we insert the files into Database. If the datatype is wrong, then the file is rejected.
Null values in columns - If any of the columns in a file have all the values as NULL or missing, we discard such a file.

**Model Training:**
Data Export from Db :
     The accumulated data from db is exported in csv format for model training
Data Preprocessing   
Performing EDA to get insight of data like  identifying distribution , outliers ,trend
      among data etc.
Remove Stopwords and Numbers from news article text.
Check for null values in the columns. If present impute the null values.
Encode the categorical values with numeric values.

**Prediction:**
The testing files are shared in the batches and we perform the same Validation operations ,data transformation and data insertion on them.
The accumulated data from db is exported in csv format for  prediction
We perform data pre-processing techniques on it.
Naïve Bayes model created during training is loaded and clusters for the preprocessed data is predicted
Once the prediction is done for all the clusters. The predictions  are saved in csv format and shared.







