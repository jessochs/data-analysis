import pandas as pd

df = pd.read_csv("student_spending.csv")

def main():
    
    mean_income()
    mean_rent()
    student_major()
    student_spending_diagram()
    
def mean_income():
    print()
    average = df['monthly_income'].mean()
    # use the mean() function to easily get the average of the dataset
    # and filtering by only using monthly income
    print(f'The average monthly income for the students is ${average}')

def mean_rent():
    print()
    rent = df['housing'].mean()
    # use the mean() function to easily get the average of the dataset
    # and filtering by only using 'housing'
    print(f'The average rent is ${rent}')

def student_major():
    major = df['major'].value_counts()
    # saving it as a variable so it will be easier to print
    # used value counts to count how many times each value is mentioned
    print('')
    print('Students per major')
    print(major)

def student_spending_diagram():
    print()
    print('Dataset information:')
    print(df.describe())
    # I wanted to create this function to see general
    # numbers for this set

if __name__ == "__main__":
    main()