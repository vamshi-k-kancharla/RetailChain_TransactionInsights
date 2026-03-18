
import matplotlib.pyplot as plt

'''
    Sub Task Input values to analyze promotion and discount impact
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Season with Highest Total revenue")
    print("2 :=> Seasonal Preferences for Store Types Or Product Categories")
    print("3 :=> Plot of Average spending Per Season")
    print("4 :=> Exit the code")

    print('\n')


'''
    Season with Highest Total revenue
'''

def FindSeasonWithHighestTotalRevenue(retailTransactionsDataFrame) :

    print(retailTransactionsDataFrame[['Season', 'Total_Cost']].groupby('Season').sum().sort_values(by='Total_Cost', ascending=False).head(1))


'''
    Seasonal Preferences for Store Types Or Product Categories
'''

def FindSeasonalPreferencesForStoreTypesOrProductCategories(retailTransactionsDataFrame) :

    retailStoreType = retailTransactionsDataFrame[['Season', 'Store_Type']].groupby('Store_Type').value_counts().sort_values(ascending=False).groupby('Store_Type').head(1)

    print(retailStoreType)
    print("\n")

    retailProductCategory = retailTransactionsDataFrame[['Season', 'Product']].groupby('Product').value_counts().sort_values(ascending=False).groupby('Product').head(1)

    retailProductCategoryDF = retailProductCategory.to_frame()

    maxCount = retailProductCategoryDF[retailProductCategoryDF['count'] > 1].max()

    print(retailProductCategoryDF[retailProductCategoryDF['count'] == maxCount['count']])


'''
    Plot of Average spending Per Season
'''

def DrawAPlotOfAvgSpendingPerSeason(retailTransactionsDataFrame) :

    avgSeasonCost = retailTransactionsDataFrame[['Season','Total_Cost']].groupby('Season').mean()

    avgSeasonCost['Total_Cost'].plot(kind='bar')

    plt.show()


'''
    Process the Seasonality Trends on Sales
'''

def ProcessSeasonalityTrends(retailTransactionsDataFrame) :

    PrintSubTaskInputParameterDetails()
    task = int(input('enter the given Sub task input : '))

    print('\n')

    match task :

        case 1 :

            FindSeasonWithHighestTotalRevenue(retailTransactionsDataFrame)

        case 2 :

            FindSeasonalPreferencesForStoreTypesOrProductCategories(retailTransactionsDataFrame)

        case 3 :

            DrawAPlotOfAvgSpendingPerSeason(retailTransactionsDataFrame)

        case _ :

            print("Invalid input received...Please try again")


