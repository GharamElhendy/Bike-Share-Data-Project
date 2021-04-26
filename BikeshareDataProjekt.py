import time
import pandas as pd
import numpy as np

#the repos: I used to finisht the project: https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py
#https://velog.io/@pss2138/Bikeshare-Project-in-Udacity
#https://github.com/diogoribeir/Investigate-bikeshare-database/commit/20cd290dc4b79bd4f2bc2a96abef54f08ff690a6

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Month_inputs = ["all", "january", "february", "march", "april", "may", "june"]
Day_inputs =  ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Here, we prompt the user to input one of the three available cities and use a while loop to prompt them to input the right items in the case that they don't
    name_of_city = ""
    while name_of_city.lower() not in CITY_DATA:
        name_of_city = input("\n What is the name of the city whose data you would like to analyze? \nEnter the name of one of the following cities: Chicago, New York City, Washington\n")
        if name_of_city.lower() in CITY_DATA:
            city = CITY_DATA[name_of_city.lower()]
        else:
            print("Please search for available data. Enter the name of one of the following cities: Chicago, New York City, Washington.")
    # Here, we prompt the user to input a month to review its data
    name_of_month = ""
    while name_of_month.lower() not in Month_inputs:
        name_of_month = input("\n Which months' data would you like to analyze? \n Enter one of the following: All, January, February, March, April, May, or June\n")
        if name_of_month.lower() in Month_inputs:
            month = name_of_month.lower()
        else:
            print("Unable to retrieve. Please enter one of the following: All, January, February, March, April, May, June\n")

    # Here, we prompt the user to input one of the days of the week, or use "all" to get all of them
    name_of_day = ""
    while name_of_day.lower() not in Day_inputs:
        name_of_day = input("\n Which day's data would you like to analyze? \n Enter one of the following: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday\n")
        if name_of_day.lower() in Day_inputs:
            day = name_of_day.lower()
        else:
            print("Unable to retireve. Please enter one of the following: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #We'll start by loading the data file into a data frame
    df = pd.read_csv(city)

    #Then we'll get the datetime from the Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Then, we'll create new columns from Start Time to extract the month and the day of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #For month filtration, if the user doesn't input "all", we'll index the months' list to get an int that corresponds to each, and then create a new dataframe
    if month != "all":
        month = Month_inputs.index(month)
        df = df.loc[df['month'] == month]
    #If the user doesn't input "all" we will create new dataframe to filter by day of week
    if day != "all":
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Arguments:
    (DataFrame) df - Pandas DataFrame which contains the data of the city with the filter for both the month and day applied
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    from datetime import datetime
    start_time = datetime.now()
    # Here, we display to the user the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: " + Month_inputs[most_common_month].title())

    # Here, we display the most common day of the week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day is: " + most_common_day)

    # Here, we display the most common hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour is: " + str(most_common_hour))
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Arguments:
    (DataFrame) df - Pandas DataFrame with the data of the city filtered by day and month
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    from datetime import datetime
    start_time = datetime.now()

    # This is to display the most common starting station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is:" + most_common_start_station)

    # This is to display the most common ending station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: " + most_common_end_station)

    # This is to show the most common route (starting to ending station) that people take
    most_common_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Arguments:
    (DataFrame) df - Pandas DataFrame with the data of the city filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    from datetime import datetime
    start_time = datetime.now()

    # Here, we display the total travel time of the bikers
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # Here, we display the average time it takes the biker to finish their route
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:" + str(mean_travel_time))
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    from datetime import datetime
    start_time = datetime.now()

    # This displays the user type counts
    types_of_users = df['User Type'].value_counts()
    print("The number of user types is: " + str(types_of_users))

    # This displays counts of gender: Since only Chicago and New York City have gender-related data
    if CITY_DATA == 'chicago.csv' or CITY_DATA == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
    else:
        print("No gender data for this city")
    
    end_time = datetime.now()
    print("Duration: {}".format(end_time - start_time))

    # Here, we display to the user the earliest, latest, and most common birth year of bikers
    from datetime import datetime

    start_time = datetime.now()
    earliest_birth_year = df['Birth Year'].min()
    most_recent_birth_year = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()[0]
    print("Earliest birth year is: {}\n".format(earliest_birth_year))
    print("Most recent birth year is: {}\n".format(most_recent_birth_year))
    print("Most common birth year is: {}\n".format(most_common_birth_year))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print('-'*40)

def displaying_raw_data(df):
    '''If the user requests so, this function displays the raw data'''
    print(df.head())
    next = 0
    while True:
        viewing_raw_data = input("Are you interested in viewing the next five rows from the raw data? Enter: Yes or No")
        if viewing_raw_data.lower() != yes:
            return
        next += 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
