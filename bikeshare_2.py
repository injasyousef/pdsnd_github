import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        print("Invalid input. Please enter a valid city.")

    while True:
        month = input("Enter month (january to june or 'all'): ").lower()
        if month in months:
            break
        print("Invalid input. Please enter a valid month.")

    while True:
        day = input("Enter day of the week or 'all': ").lower()
        if day in days:
            break
        print("Invalid input. Please enter a valid day.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('Most Common Month:', df['month'].mode()[0].title())
    print('Most Common Day of Week:', df['day_of_week'].mode()[0].title())
    print('Most Common Start Hour:', df['hour'].mode()[0])



def station_stats(df):
    print('\nThe Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most commonly used start station
    print('Most Commonly Used Start Station:', df['Start Station'].mode()[0])

    # most commonly used end station
    print('Most Commonly Used End Station:', df['End Station'].mode()[0])

    # most frequent combination of start and end station
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']
    print('Most Common Trip:', df['Trip Combination'].mode()[0])



def trip_duration_stats(df):
    print('\nTrip Duration...\n')
    start_time = time.time()

    # total travel time
    print('Total Travel Time (seconds):', df['Trip Duration'].sum())

    # average travel time
    print('Average Travel Time (seconds):', df['Trip Duration'].mean())



def user_stats(df):
    print('\nUser Stats...\n')
    start_time = time.time()

    # counts of user types
    print('\nUser Types:\n', df['User Type'].value_counts())

    # counts of gender (only for cities with Gender column)
    if 'Gender' in df.columns:
        print('\nGender Distribution:\n', df['Gender'].value_counts())
    else:
        print('\nGender data not available for this city.')

    # birth year stats (only for cities with Birth Year column)
    if 'Birth Year' in df.columns:
        print('\nEarliest Year of Birth:', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:', int(df['Birth Year'].max()))
        print('Most Common Year of Birth:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth year data not available for this city.')


def display_raw_data(df):
    i = 0
    while True:
        raw = input('\nWould you like to see the raw data?  yes, no: ').lower()
        if raw != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("\nNo more data to display.")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
