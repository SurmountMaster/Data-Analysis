import pandas as pd


def to_percent(value):
    return (value * 100).round(1)


def calculate_demographic_data(print_data=True):
    # Read data from file
    df_source = pd.read_csv(
        r"C:\Users\chido\Downloads\github\Excel\freecodecamp-data-analysis-with-python-main\freecodecamp-data-analysis-with-python-main\demographic-data-analyzer\adult.data.csv"
        )

    # How many of each race are represented in this dataset?
    race_counts_series = df_source['race'].value_counts()

    # What is the average age of men?
    avg_age_males = round(df_source[df_source['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    pct_bachelors = to_percent((df_source['education'] == 'Bachelors').sum() / len(df_source))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    edu_advanced_mask = df_source['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    edu_nonadvanced_mask = ~edu_advanced_mask

    pct_adv_over50k = to_percent(
        ((edu_advanced_mask) & (df_source['salary'] == '>50K')).sum() / edu_advanced_mask.sum()
    )
    pct_nonadv_over50k = to_percent(
        ((edu_nonadvanced_mask) & (df_source['salary'] == '>50K')).sum() / edu_nonadvanced_mask.sum()
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hours_week = df_source['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    cnt_min_workers = (df_source['hours-per-week'] == min_hours_week).sum()
    pct_rich_minhours = to_percent(
        ((df_source['hours-per-week'] == min_hours_week) & (df_source['salary'] == '>50K')).sum()
        / cnt_min_workers
    )

    # What country has the highest percentage of people that earn >50K?
    country_rich_ratio = (
        df_source[df_source['salary'] == '>50K']['native-country'].value_counts()
        / df_source['native-country'].value_counts()
    )

    top_rich_country = country_rich_ratio.idxmax()
    top_rich_country_pct = to_percent(country_rich_ratio[top_rich_country])

    # Identify the most popular occupation for those who earn >50K in India.
    top_occupation_india = df_source[
        (df_source['native-country'] == 'India') & (df_source['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_counts_series)
        print("Average age of men:", avg_age_males)
        print(f"Percentage with Bachelors degrees: {pct_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {pct_adv_over50k}%")
        print(f"Percentage without higher education that earn >50K: {pct_nonadv_over50k}%")
        print(f"Min work time: {min_hours_week} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {pct_rich_minhours}%")
        print("Country with highest percentage of rich:", top_rich_country)
        print(f"Highest percentage of rich people in country: {top_rich_country_pct}%")
        print("Top occupations in India:", top_occupation_india)

    return {
        'race_count': race_counts_series,
        'average_age_men': avg_age_males,
        'percentage_bachelors': pct_bachelors,
        'higher_education_rich': pct_adv_over50k,
        'lower_education_rich': pct_nonadv_over50k,
        'min_work_hours': min_hours_week,
        'rich_percentage': pct_rich_minhours,
        'highest_earning_country': top_rich_country,
        'highest_earning_country_percentage': top_rich_country_pct,
        'top_IN_occupation': top_occupation_india
    }
