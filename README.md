# Personalization in Political Search Results Based on Location
## Authors: Simon Arends, Wessel Kamphuis, Romy Bosgoed

### Table of content
0. [Installation](#installation-requirements)
1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Input](#input)
4. [Experimental Setup](#experimental-setup)
5. [Output](#output)
6. [Validation](#validation)
7. [Conclusion](#conclusion)

### Installation requirements
When wanting to use this project, one has to do 2 things. The first is to add the chromedriver for Selenium to their 
Path, using environmental variables. Second, one has to install the packages stated in the [requirements file](Requirements.txt). 

### Abstract
This project is related to an article that analyzed the potential effect of personalization, based on user’s location in
web search. In particular, search results related to policy of Dutch political parties will be further investigated. The
location of a user will be used as a variable to see whether or not it influences political search results. Analyzing 
if location has effect on search results is important, as it can be used to influence political behaviour. This could
be especially important in the light of the upcoming Dutch parliamentary elections of March2021. Locations have been 
handpicked by differences in political party preferences. Google’s search engine is used as the primary source and is 
automated by Selenium using Python. The results show that there is some degree of personalization due to different 
locations. 

### Introduction
As discussed before, this project is designed with the intention of measuring what the effect is of a user's location, 
on the results returned by Google, when using political related queries.
For this purpose, we designed a project which takes an [excel file](Experiment/Input/Coordinates.xlsx), executes queries
where the location is used of the excel file, and then saves the results of the page by writing it into a folder as a 
text file. The execution of the program is conducted on two machines at the save time to be able to detect possible 
noise.
The next step is to validate the results. This is done using three metrics: Cohen's Kappa, Jaccard similarity and 
Kendall_Tau. The meaning of these metrics can be found in [Validation](#validation)

### Input
As an input we provide an [excel file](Experiment/Input/Coordinates.xlsx). 
This file has a political party on each sheet. A sheet then consists of 5 columns; 
Municipality, Percentage, Latitude, Longitude and Aggregate. This last column has the structure that can be used as 
input for the geo locations of the driver.
   
### Experimental setup
For this we use the [browser file](Experiment/Code/browser.py), and we use the [experimentor file](experimentor.py) to 
run it. Experimentor contains a dictionary of directory names and search queries in key, value pairs. The value is then
modified into a query by adding 'standpunten' to the value. The key and value are then passed to the [browser file](Experiment/Code/browser.py).
The key is the directory and the value is converted into a query.

The [browser file](Experiment/Code/browser.py) has 4 main functions. 1. It loads the coordinates excel file, 2. it loads the 
Selenium driver, 3. it uses a passed query in combination with the coordinates, which modified the driver, 4. and it s
saves the results in a passed directory. 

#### 1. Coordinates file
The [coordinates excel file](Experiment/Input/Coordinates.xlsx), mentioned in the previous section, is convirted into a 
pandas dataframe for easier processing. Where each sheet is also a dataframe. This is done with [the book_to_table defintion](Experiment/Code/browser.py).

#### 2. Selenium driver
For this experiment we work with selenium to automatically execute the queries. More specifically, we use the 
chromedriver. For this to work, one has to add the ChromeDriver() to their path, since it is loaded from there.

#### 3. Query search
We use the queries from the [experimentor file](experimentor.py). These are passed to browser. First the Selenium driver 
and the coordinates are loaded. Then for each query, we loop over all locations, from the different sheets. These coordinates
are then set using a command for the ChromeDriver. A new instance of the chromedriver is launched for each location, after 
which the cookies are deleted. We then go to www.google.com, enter the query, wait 2 seconds and then save the results

#### 4. result saver
After executing a query, we want to save the results

### Output

### Validation
We filter out the possible noise by determining [Cohen's Kappa](Validation/Code/cohens_kappa.py).
The Cohen's Kappa meassures the inter-rater reliability. It does this by comparing two labels, or in our case, two lists 
of labels. If the two lists are identical, a coefficient of 1.0 is returned. If the lists are of equal length but 
contain different elements, a value between 0.0 and 1.0 is returned. If either one of the files is empty or of unequal 
length (yes, this does sometimes happen), a value of 0.0 is set.
By using the Cohen's Kappa, we can easily filter on files that only have a coefficient of 1. Because these files were 
thus the same on two machines at the same time and are then most likely to be shown to the most users. Due to limited 
time is step is done manually. Otherwise, a method would have been added to the [Validation folder](Validation/Code) to 
do this automatically.
After preprocessing the results, we can look at the most important and stable files, and use the [Jaccard similarity score and the Kendall_Tau score](Validation/Code/jaccard_and_kendall.py)
The jaccard similarity looks at two sets and returns a score based on their overlap. A score of 1.0 meaning that both 
files contain the same elements (unordered), a score between 0.0 and 1.0 if their intersetion is smaller than their 
union, and a score of 0 if they do not contain any of the same elements, or the files are not used due to missing values.
The Kendall_Tau coefficient looks whether or not the ranking of two lists is the same. A value of 1.0 meaning they are 
identical. For a value between 0.0 and 1.0 the list A needs to be ordered in a different way, where a value closer to 1.0 
represent smaller modifications than a value closer than 0.0. 
Since both metrics require an input of two lists, they need a 'base value' or list to compare to. We choose Nijmegen as 
a base value since the University is located here and we are only interested in the differences. 

### Conclusion