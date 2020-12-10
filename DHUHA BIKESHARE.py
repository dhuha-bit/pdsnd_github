import numpy as np
import pandas as pd
import time

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

    # Function 1 # get_filters () #
"""
    #Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
def get_filters():
    CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
    MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

    print('Hello! Lets explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # City part#
    
    while True: 
        city =input("\n Please specify a city to analyze? (chicago, new york city, washington)\n").lower()          
        if city not in CITY_DATA:
          print("Apologies, please select one of the mentioned cities Chicago, New York City or Washington.\n")
          continue
        else: 
          break
    # City name was not entered correctly, we can not preform analysis
    # Month part #
    while True: 
        month =input("\n Please specify a month to analyze? (january, february, march, april, may, june)\n").lower()         
        if month not in MONTH_DATA:
          print("Apologies, please select one of the mentioned months.\n")
          continue
        else: 
          break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Day part#
    while True: 
        day =input("\n Please specify a day to analyze? (monday, tuesday,wednesday, friday, saturday, sunday).\n").lower()        
        if day not in DAY_DATA:
          print("Apologies, please select one of the mentioned days.\n")
          continue
        else: 
          break
    
  
    print('-' * 40)
    return city, month,day
    



    #Function 2
def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #Loads data for the specified city and filters by month and day if applicable.
    #Args:
        #(str) city - name of the city to analyze
        # (str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day filter

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # filter by day of week to create the new dataframe
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


    # Function 3
def popular_hour(df):
    pass


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common hour of day
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    common_hour = df['hour'].mode()[0]

    print('Most common  Hour:', popular_hour)

    # Most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]

    # Most common month
    df['month'] = df['Start Time'].dt.day
    common_month = df['month'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


    # Function 4

def station_stats(df):
    # print ('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # display most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] +" "+ df['End Station']
    most_common_start_end_station = df['trip'].mode()[0]
    print("The most common used station of start station and end station trip is : " + most_common_start_end_station)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


    # Function 5
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time  is:", (total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time  is:", (mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


    # Function 6
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
        
    start_time = time.time()

        # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

        # Display counts of gender
    if city != 'washington':
      gender = df['Gender'].value_counts()
      print("The user gender count  is: \n" + str(gender))

        # Display earliest, most recent, and most common year of birth
      birth_year = df['Birth Year']
        # earlist birth
      earliest_birth: object = df['Birth Year'].min()
      print("The most earlist birth year is:", earliest_birth)

        # most recent birth
      most_recent: object = birth_year.max()
      print("The most recent birth year is:", most_recent)
        # most common year of birth
      most_common_year: object = df['Birth Year'].mode()[0]
      print('The most common year is:', most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


    # Function 7
    
def bikeshare_data(df):
    index=0
    while True:
        user_answer=input("do you want to see raw data? if yes enter Y, if no enter N")
        if user_answer not in ['N','Y']:
            print("Please select Y or N")
            continue
        elif user_answer=="Y":
            print(df[index:index+5])
            index+=5
        else:
            break 
        
        
def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        bikeshare_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you')

            break

if __name__ == "__main__":
    main()


