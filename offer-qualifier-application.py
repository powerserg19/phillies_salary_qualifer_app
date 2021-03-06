import webbrowser
import operator
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import requests
import lxml.html as lh
import sys
import re
DEFAULT_PLAYER_LIMIT=125

############################################
#
#  This application reads in one argument parameter that
#  loads this page https://questionnaire-148920.appspot.com/swe/data.html,
#
#  It then extracts the top 125 salaried players, computes the average of their salaries then plots the players vs salary
#  on one trace along with the average salary on a second trace.
#
#  It then saves it to a file called qualifying_offer.html in the same dirctory as this run time script.
#
#  Using Python Versionsys.version_info(major=3, minor=6, micro=9, releaselevel='final', serial=0)
#  Using Plotly Version 4.9.0
#
#  Author: Sergio DiVentura
#  REV 1.0, August 11 2020
#
############################################



##
## plot the data points player vs salary
## got code samples from https://plotly.com/
##
def plot(players, average,num_players=DEFAULT_PLAYER_LIMIT):

    try:

        player_names = list(players.keys())
        player_salaries = list(players.values())

        #set the player vs salary trace
        salaries =  go.Scatter(x=list(range(0,num_players)), y=player_salaries,mode="lines+markers+text",hovertext=player_names,
                               name="player's salaries" ,line=dict(color='red'));
        #set the average trace
        average =  go.Scatter(x=[0, num_players], y=[average,average],name="average")
        #overlay the sub plots and write to html file
        data =  [average , salaries]

        fig = go.Figure(data=data)
        fig.update_layout(title_text="Players and Their Salaries with Average")
        fig.write_html("qualifying_offer.html")
        webbrowser.open('qualifying_offer.html', new=2)
    except:
        print ("failed writing resultant data!")
        raise



#
#  reads the html page and saves the players name
#  and their salary in  dictionary.   The data changes with each page load!
#  Got this code snippet from here
#  https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
#
#
def get_players_from_html(url):
    player_and_salalries = {}
    player_and_salalries_sorted = {}
    try:
        page = requests.get(url)
        #Store the contents of the website under doc
        doc = lh.fromstring(page.content)
        #Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')
    except:
        print ("could not load players salaries!")
        raise Exception

    for j in range(0,len(tr_elements)):
        #T is our j'th row
        T=tr_elements[j]
        #If row is not of size 4, the //tr data is not from our table
        if len(T)!=4:
            break
        #i is the index of our column
        i=0
        try:
            #Iterate through the first two columns player name and salary
            for t in T.iterchildren():
                data=t.text_content()
                if i==0:
                    player_name = str(data)
                #Check if row is empty
                if i == 1:
                    ###strip out non numericals in a string
                    #https://stackoverflow.com/questions/1249388/removing-all-non-numeric-characters-from-string-in-python
                    salary=str(re.sub("[^0-9]", "",data))
                    #if we can get a number out of it then store it
                    if salary.isnumeric():
                        player_and_salalries[player_name] = int(salary)
                    #we only want the first two columns
                    break

                i+=1
            ### sort a dictionary by value in descending order
            #https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
            player_and_salalries_sorted = dict(sorted(player_and_salalries.items(), key=operator.itemgetter(1), reverse=True))
        except:
            print ("Failed reading salary data!")
            raise

    return player_and_salalries_sorted
#
# read in the dictiony and average the highest paid of first 125 salaries
#
def get_average_salary(player_and_salaries, numplayers=DEFAULT_PLAYER_LIMIT):
    total =0
    count =1
    for key, value in player_and_salaries.items():
        total = total + value
        if count == numplayers:
            average = total/numplayers
            break;
        count+=1
    return average
#
# main application entry
#
if __name__ == '__main__':

    print("**********Running The Phighting Phils Offer Qualifier App!....*****************************")
    print("Using Python Version" + str( sys.version_info) )
    print("Using Plotly Version " + plotly.__version__)

    try:
        player_and_salalries = get_players_from_html(str(sys.argv[1]))
        average = get_average_salary(player_and_salalries)
        plot(player_and_salalries, average)
    except:
        print ("Failed to produce offer value!")

    print("Offer qualifier Complete! Refer to file qualifying_offer.html for results")
