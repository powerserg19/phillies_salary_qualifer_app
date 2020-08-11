# phillies_salary_qualifer_app version 1.0
August 11 2020
phillies_salary_qualifer_app applicaiton - written by Sergio DiVentura.
It was developed per this questionare
https://questionnaire-148920.appspot.com/swe/    section B

##################
Dependencies
##################
The application was written with Python 3.6.9 and it leverages Ploty
library version 4.9.0. Ploty is used to present the resultant data set.

##################
About
##################

phillies_salary_qualifer_app produces a scatter plot consisting of players and their respective salaries. A second trace illustrates the average of those salaries. 

Only the top 125 highest paid salaries are averaged and illustrated. The dataset is drawn from this page https://questionnaire-148920.appspot.com/swe/data.html

###############
How to run
###############
1. Download or check out the appplication from this git repository
   https://github.com/powerserg19/phillies_salary_qualifer_app

2. Run it from the command line as follows:  

> python3.6 offer-qualifier-application.py https://questionnaire-148920.appspot.com/swe/data.html

3. It will produce and htm a file in the same location called qualifying_offer.html

4. Open it with a web browser to view the results

5. You can hover over each point to get the players name and their salary

6. Ploty also offers zoom, pan, auto scale , among other controls at the type right hand corner of the browser

NOTE: At this same repo location at root dir I posted  example_qualifying_offer.html as and example run.





