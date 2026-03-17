
'''
    Sub Task Input values to process transaction insights
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Total transactions")
    print("2 :=> Total Number of Unique Customers")
    print("3 :=> Top 5 products sold across all transactions")
    print("4 :=> Cities with highest number of transactions")
    print("5 :=> Exit the basic insights code")

    print('\n')


'''
    Find the total transactions of retail chain so far
'''

def FindTotalTransactions(retailTransactionsDataFrame) :

    print("Total Number of transactions are : " + str(len(retailTransactionsDataFrame)))


'''
    Find the unique customers in the transaction database
'''

def FindUniqueCustomers(retailTransactionsDataFrame) :

    print("Total Number unique customers are : " + str(len(retailTransactionsDataFrame['Customer_Name'].unique())))


'''
    Find the top 5 most products sold
'''

def FindTop5ProductsSold(retailTransactionsDataFrame) :

    topProducts = retailTransactionsDataFrame['Product'].value_counts().sort_values(ascending= False)

    print("Top most 5 products sold in the retail chain are : \n")

    print(topProducts[:5])


'''
    Find Cities with Highest No Of Transactions
'''

def FindCitiesWithHighestTransactions(retailTransactionsDataFrame) :

    mostTransactionsCityWise = retailTransactionsDataFrame['City'].value_counts().sort_values(ascending=False)

    maxTransactionsCityWise = 0

    citiesWithHighestTransactions = []

    for City, Count in mostTransactionsCityWise.items() :

        #print("City = " + City + ", Count = " + str(Count))

        if maxTransactionsCityWise == 0 :

            maxTransactionsCityWise = Count
            citiesWithHighestTransactions.append(City)

        else :

            if Count == maxTransactionsCityWise :

                citiesWithHighestTransactions.append(City)

            else :

                break

    print("Max Transactions Per Individual City is : ", maxTransactionsCityWise)  
    print("Max Transactional Cities are : ", citiesWithHighestTransactions)  


'''
    Process the Basic Insights of retail transactions
'''

def ProcessBasicRetailTransactionInsights(retailTransactionsDataFrame) :

    PrintSubTaskInputParameterDetails()
    task = int(input('enter the given Sub task input : '))

    print('\n')

    match task :

        case 1 :

            FindTotalTransactions(retailTransactionsDataFrame)

        case 2 :

            FindUniqueCustomers(retailTransactionsDataFrame)

        case 3 :

            FindTop5ProductsSold(retailTransactionsDataFrame)

        case 4 :

            FindCitiesWithHighestTransactions(retailTransactionsDataFrame)

        case _ :

            print("Invalid input received...Please try again")












