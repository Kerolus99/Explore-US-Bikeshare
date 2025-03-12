import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("enter a city from those cities that you want to analyze (chicago, new york city, washington).\n").lower()
    while city not in CITY_DATA.keys():
        print("Enter a valid city from those (chicago, new york city, washington),Please.")
        city = input("Enter a city from those cities that you want to analyze (chicago, new york city, washington).\n").lower()
        


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "febraury", "march", "april", "may", "june", "all"]
    while True:
        month = input("choose a month from those months (january, febraury, march, april, may, june) or all\n").lower()
        if month in months:
            break
        else:
            print("Enter a valid month ")
            


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sunday", "monday", "tuesday", "wednesday", "thrusday", "friday", "saturday", "all"]
    while True:
        day = input("Enter day in a week or enter (all) if you want all the week\n").lower()
        if day in days:
            break
        else:
            print("Enter a valid day ")
    


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
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["start hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        months = ["january", "febraury", "march", "april", "may", "june"]
        month = months.index(month) +1
        df = df[df["month"] == month]
        
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month is: {}".format(df["month"].mode()[0]))


    # TO DO: display the most common day of week
    print("Most common day is: {}".format(df["day_of_week"].mode()[0]))

    # TO DO: display the most common start hour
    print("Most common hour is: {}".format(df["start hour"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station is: {}".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most commonly used end station is: {}".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df["combination_of_start_and_end"] = df["Start Station"]+","+df["End Station"]
    print("Most frequent combination of start station and end station trip is: {}".format(df["combination_of_start_and_end"].mode()[0]))
          
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The Total travel time is: {}".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(df["Trip Duration"].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts().to_frame())


    # TO DO: Display counts of gender
    if city != "washington":
        print(df["Gender"].value_counts().to_frame())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest Year of birth is: {}".format(int(df["Birth Year"].min())))
        print("Most common Year of birth is: {}".format(int(df["Birth Year"].mode()[0])))
        print("Most resent Year of birth is: {}".format(int(df["Birth Year"].max())))
    else:
        print("there is no birth of year data in washington")

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    #ask the user if he wants to see 5 rows of raw data
    print("Do you want to see the raw data?\n")
    
    x = 0
    users_input = input("do you want to show you a 5 rows of raw data?, type yes or no\n").lower()
    users_choice = ["yes", "no"]
    if users_input not in users_choice:
        print("Invalid typing, please type yes or no")
        users_input = input("do you want to show you a 5 rows of raw data?, type yes or no\n").lower()
    elif users_input == "no":
        print("okay")
    elif users_input == "yes":
        while x+5 < df.shape[0]:
            print(df.iloc[x:x+5])
            x += 5
            users_input = input("do you want to show you a more of 5 rows of raw data?, type (yes) or (no)\n").lower()
            if users_input == "no":
                print("okay")
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Bye bye")
            break


if __name__ == "__main__":
	main()
