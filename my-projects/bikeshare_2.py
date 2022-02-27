import time
import pandas as pd
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike_share data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please choose a city name from Chicago, New York City or Washington:\n> ").lower()
        if city not in CITY_DATA:
            print("please enter a valid city name")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('please enter a month name that you want to filter by or enter "all" \
if you do not want to apply month filter:\n> ')
        if month not in months:
            print("please enter a valid month name")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        day = input('please enter a day name that you want to filter by or enter "all" \
if you do not want to apply day filter:\n> ')
        if day not in days:
            print("please enter a valid day name")
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("the most common month is: ", calendar.month_name[common_month])

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("the most common day of week is: ", common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("the most common starting hour is: ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("the most common start station is: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("the most common end station is: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_start_station_and_end_station = (df['Start Station'] + ' -- ' + df['End Station']).mode()[0]
    print("the most frequent start and end station is: ", most_frequent_start_station_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: " + str(total_travel_time) + " seconds or " + str(total_travel_time/60) + " minutes")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("the mean travel time is: " + str(mean_travel_time) + " seconds or " + str(mean_travel_time/60) + " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bike_share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("the count of user type is:\n", user_type_count)

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("the count of gender is:\n", gender_count)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth = df['Birth Year'].min()
        print("the earliest year of birth is: ", int(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print("the most recent year of birth is: ", int(most_recent_year_of_birth))

        common_year_of_birth = df['Birth Year'].mode()[0]
        print("the most common year of birth is: ", int(common_year_of_birth))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n>')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
