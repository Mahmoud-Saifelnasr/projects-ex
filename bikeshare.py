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
    while True:
        city=input('write your city of choice form the following options(chicago, new york city, washington):').lower()
        capital=('chicago','new york city','washington')
        if city not in capital:
            print ('not a valid input')
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=('All','January','February','March','April','May','June')
        month=input('write your month of choice or write All:').lower()
        if month.islower():
            month=month.title()
        if month not in months:
            print ('invalid input,try again')
            continue
        else:
            break
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekdays=['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        day=input('write your day of choice or write All:').lower()
        if day.islower():
            day=day.title()
        if day not in weekdays:
            print ('invalid input,try again')
            continue
        else:
            break

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'All':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('the most common month:',common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('the most common day:',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()
                 
    print('most commonly used start station is', common_start)
    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()      
    print('most commonly used end station is', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    Combination=df.groupby(['Start Station'])['End Station'].value_counts()
    Combination=Combination.keys()[0]
    print('the most frequent combination of start station and end station trip',Combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    print ('total travel time is:',round(total/60/60)," hours")
    # TO DO: display mean travel time
    average=df['Trip Duration'].mean()
    print ('average travel time is:',round(average/60)," Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Type=df['User Type'].value_counts()
    print ('counts of user types:\n',Type.to_string())

    # TO DO: Display counts of gender
    if set(['Gender','Birth Year']).issubset(df.columns):
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types.to_string())
    else:
        print ('gender data not available')
        
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if set(['Gender','Birth Year']).issubset(df.columns):
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        common_year=df['Birth Year'].value_counts()
        common=common_year.keys()[0]
        print('the oldest bikeriders are born in {},\n the youngest bikeriders are born in {},\n and most common bikes riders age are {}'.format(earliest,recent,common))
    else:
        print('no birth year data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_data=input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ").lower()
            if view_data not in ('yes','no'):
                print ('not a valid answer,please answer by writing yes or no')
            else:
                break
        start_loc = 0
        while (view_data=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            while True:
                view_display = input("Do you wish to continue? Enter yes or no?").lower()
                if view_display not in ('yes','no'):
                    print('not a valid answer')
                else:
                    break
            if view_display !='yes':
                break
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
