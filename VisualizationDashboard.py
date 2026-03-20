
import matplotlib.pyplot as plt

import pandas as pd

'''
    Sub Task Input values to visualize Dashboard & Statistics
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Bar plot of no of transactions per city")
    print("2 :=> Pie chart of distribution of payment methods")
    print("3 :=> Line chart of monthly revenue trends")
    print("4 :=> Stacked bar of revenue by Season and Customer Category")
    print("5 :=> Exit the code")

    print('\n')


'''
    Bar plot of no of transactions per city
'''

def PlotNoOfTransactionsPerCity(retailTransactionsDataFrame) :

    retailTransactionsDataFrame[['City']].value_counts().plot(kind='bar')

    plt.show()


'''
    Pie chart of distribution of payment methods
'''

def PlotDistributionOfPaymentMethods(retailTransactionsDataFrame) :

    retailTransactionsDataFrame[['Payment_Method']].value_counts().plot(kind='pie', autopct='%1.2f%%')

    plt.show()



'''
    Line chart of monthly revenue trends
'''

def PlotMonthlyRevenueTrends(retailTransactionsDataFrame) :

    retailTransactionsDataFrame['Date'] = pd.to_datetime(retailTransactionsDataFrame['Date'])

    retailTransactionsDataFrame['Year_Month'] = retailTransactionsDataFrame['Date'].dt.strftime('%Y-%m')

    retailXnNewDataFrame = retailTransactionsDataFrame.sort_values(by='Year_Month')

    monthlyRevenueTrendDF = retailXnNewDataFrame[['Year_Month', 'Total_Cost']].groupby('Year_Month').sum()

    monthlyRevenueTrendDF.plot(kind='line')

    plt.show()


'''
    Stacked Bar of Total Revenue by Season & Customer Category
'''

def PlotStackedBarRevenueBySeasonAndCustomerCategory(retailTransactionsDataFrame) :

    # learnt the stack bar from the source => https://www.geeksforgeeks.org/python/create-a-stacked-bar-plot-in-matplotlib/

    # Extract Retail Transaction Total Cost for the Seasons & Customer Category

    retailXnNewDF = retailTransactionsDataFrame[['Season', 'Customer_Category', 'Total_Cost']].groupby(['Season', 'Customer_Category']).sum()

    retailXnStackBarDF = { 'Season' : [] }

    customerCategories = []

    # extract indexes of Season & Customer Category

    for i, j in retailXnNewDF.index :

        if i not in retailXnStackBarDF['Season'] :
            retailXnStackBarDF['Season'].append(i)

        if j not in customerCategories :

            customerCategories.append(j)

    #print(retailXnStackBarDF)
    #print(customerCategories)


    # Populate the Customer Category object values with Zeroes

    for category in customerCategories :

        retailXnStackBarDF[category] = []

        for i in range(len(retailXnStackBarDF['Season'])) :

            retailXnStackBarDF[category].append(0)

    #print(retailXnStackBarDF)


    # Now populate the DF object with actual values

    for i, j in retailXnNewDF.index :

        currentIndex = retailXnStackBarDF['Season'].index(i)

        retailXnStackBarDF[j][currentIndex] = retailXnNewDF.loc[i,j]['Total_Cost']

    retailXnStackBarDF

    retailXnStackBarActualDF = pd.DataFrame(retailXnStackBarDF).set_index('Season')

    retailXnStackBarActualDF.plot(kind='bar', stacked=True)

    plt.show()


'''
    Draw the plots & graphs for visualisation dashboard
'''

def PlotTheTrendsAndCharts(retailTransactionsDataFrame) :

    PrintSubTaskInputParameterDetails()
    task = int(input('enter the given Sub task input : '))

    print('\n')

    match task :

        case 1 :

            PlotNoOfTransactionsPerCity(retailTransactionsDataFrame)

        case 2 :

            PlotDistributionOfPaymentMethods(retailTransactionsDataFrame)

        case 3 :

            PlotMonthlyRevenueTrends(retailTransactionsDataFrame)

        case 4 :

            PlotStackedBarRevenueBySeasonAndCustomerCategory(retailTransactionsDataFrame)

        case _ :

            print("Invalid input received...Please try again")


