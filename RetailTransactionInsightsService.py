
'''
    
    Author : Vamshi Krishna Kancharla
    Have You used AI Tools to generate code : No 
    Have You used documentation for Syntax & to learn Concepts : Yes, Searched through google.
    
'''

import pandas as pd

from BasicInsights import ProcessBasicRetailTransactionInsights
from CustomerBehaviorAnalysis import ProcessCustomerBehavioralAnalysisInsights
from PromotionAndDiscountImpact import ProcessImpactOfPromotionAndDiscount
from SeasonalityTrends import ProcessSeasonalityTrends
from VisualizationDashboard import PlotTheTrendsAndCharts


'''
    Task Input values to process transaction insights
'''

def PrintTaskInputParameterDetails() :

    print("1 :=> Basic Exploration")
    print("2 :=> Customer Behaviour Analysis")
    print("3 :=> Promotion & Discount Impact")
    print("4 :=> Seasonality Trends")
    print("5 :=> Visualisation Dashboard")
    print("6 :=> Exit the Retail Transactions Insights code")

    print('\n')



'''
    Process the retail transaction Insights from given input
'''

def ProcessRetailTransactionInsights(retailTransactionsDataFrame) :

    '''
       Execute the code forever until the exit input is received from user

    '''

    try :

        while True :

            print('\n')
            print('\n')
            print('=' * 40)

            PrintTaskInputParameterDetails()
            task = int(input('enter the given task input : '))

            print('\n')

            match task :

                case 1 :

                    ProcessBasicRetailTransactionInsights(retailTransactionsDataFrame)

                case 2 :

                    ProcessCustomerBehavioralAnalysisInsights(retailTransactionsDataFrame)

                case 3 :

                    ProcessImpactOfPromotionAndDiscount(retailTransactionsDataFrame)

                case 4 :

                    ProcessSeasonalityTrends(retailTransactionsDataFrame)

                case 5 :

                    PlotTheTrendsAndCharts(retailTransactionsDataFrame)

                case 6 :

                    break

                case _ :

                    print("Invalid input entered...Please try again")

    except Exception as e :

        print("Exception occured while executing the code => ", e)

'''
    Read the CSV File
    Print the DataFrame

'''


print("Reading CSV File of Retail Chain Transactions")

retailTransactionsDataFrame = pd.read_csv("Retail_Transactions_Dataset.csv")
#print(retailTransactionsDataFrame)

ProcessRetailTransactionInsights(retailTransactionsDataFrame)


