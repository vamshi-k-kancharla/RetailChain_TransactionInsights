
import matplotlib.pyplot as plt

import pandas as pd

'''
    Sub Task Input values to visualize Dashboard & Statistics
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Bar plot of no of transactions per city")
    print("2 :=> Pie chart of distribution of payment methods")
    print("3 :=> Line chart of monthly revenue trends")
    print("4 :=> Exit the code")

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

        case _ :

            print("Invalid input received...Please try again")


