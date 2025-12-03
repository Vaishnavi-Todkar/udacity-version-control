import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # CITY
    while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Try again.")

    # MONTH
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter month from January to June or 'all': ").lower()
        if month in months:
            break
        print("Invalid input. Try again.")

    # DAY
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter day of week or 'all': ").lower()
        if day in days:
            break
        print("Invalid input. Try again.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data and filters by month and day if applicable.
    """
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
    """Displays popular times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')

    print("Most common month:", df['month'].mode()[0])
    print("Most common day of week:", df['day_of_week'].mode()[0])
    print("Most common start hour:", df['hour'].mode()[0])

    print('-' * 40)


def station_stats(df):
    """Displays popular stations and trips."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    print("Most common start station:", df['Start Station'].mode()[0])
    print("Most common end station:", df['End Station'].mode()[0])

    df['trip'] = df['Start Station'] + " -> " + df['End Station']
    print("Most common trip:", df['trip'].mode()[0])

    print('-' * 40)


def trip_duration_stats(df):
    """Displays total and average trip duration."""
    print('\nCalculating Trip Duration...\n')

    print("Total travel time:", df['Trip Duration'].sum())
    print("Mean travel time:", df['Trip Duration'].mean())

    print('-' * 40)


def user_stats(df, city):
    """Displays user info statistics."""
    print('\nCalculating User Stats...\n')

    print("Counts of user types:\n", df['User Type'].value_counts())

    if city != 'washington':
        print("\nCounts of gender:\n", df['Gender'].value_counts())

        print("\nEarliest birth year:", int(df['Birth Year'].min()))
        print("Most recent birth year:", int(df['Birth Year'].max()))
        print("Most common birth year:", int(df['Birth Year'].mode()[0]))
    else:
        print("\nGender data not available for Washington.")
        print("Birth year data not available for Washington.")

    print('-' * 40)


def display_raw_data(df):
    """Displays raw data upon request."""
    i = 0
    while True:
        raw = input("Show 5 lines of raw data? (yes/no): ").lower()
        if raw != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
