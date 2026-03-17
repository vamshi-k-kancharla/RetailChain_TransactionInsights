
'''
    Sub Task Input values to process Customer Behavioral Analysis
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Most Spending by Customer Category")
    print("2 :=> Customer Categories with specific payment methods")
    print("3 :=> Average number of items bought per transaction per store type")
    print("4 :=> Exit the Customer Behavior Analysis code")

    print('\n')


'''
    Find the most spending by Customer Category
'''

def FindMostSpendingByCustomerCategory(retailTransactionsDataFrame) :

    customerCategoriesAvgSpending = retailTransactionsDataFrame[['Customer_Category', 'Total_Cost']].groupby('Customer_Category').mean()

    maxAvgSpending = 0

    customerCategoriesWithMaxAvgSpending = []

    customerCategoriesWithAvgSpendingObject = customerCategoriesAvgSpending['Total_Cost']

    for Customer_Category, Total_Cost in customerCategoriesWithAvgSpendingObject.items() :

        #print("Customer_Category = " + Customer_Category + ", Avg_Cost = " + str(Total_Cost))

        if maxAvgSpending == 0 :

            maxAvgSpending = Total_Cost
            customerCategoriesWithMaxAvgSpending.append(Customer_Category)

        else :

            if Total_Cost == maxAvgSpending :

                customerCategoriesWithMaxAvgSpending.append(Customer_Category)

            else :

                break

    print("Max Average Spending Per Individual Customer Category is : ", maxAvgSpending)  
    print("Max Avg Spending Customer Categores are : ", customerCategoriesWithMaxAvgSpending)  



'''
    Find the customer categories preferring Payment methods
'''

def FindPaymentMethodsPreferredByCustomerCategory(retailTransactionsDataFrame) :

    customersWithPaymentMethods = retailTransactionsDataFrame[['Customer_Category','Payment_Method']].groupby('Customer_Category').value_counts().groupby('Customer_Category').head(1)

    print("Payment Methods preferred by Customer Categories are : \n")  

    print(customersWithPaymentMethods)


'''
    Find the Average Items Bought per Store Type
'''

def FindAverageItemsBoughtPerStoreType(retailTransactionsDataFrame) :

    print("Average no of items bought per transaction per store type are : \n")  

    print(retailTransactionsDataFrame[['Store_Type','Total_Items']].groupby('Store_Type').mean())


'''
    Process the Basic Insights of Customer behavior Analysis
'''

def ProcessCustomerBehavioralAnalysisInsights(retailTransactionsDataFrame) :

    PrintSubTaskInputParameterDetails()
    task = int(input('enter the given Sub task input : '))

    print('\n')

    match task :

        case 1 :

            FindMostSpendingByCustomerCategory(retailTransactionsDataFrame)

        case 2 :

            FindPaymentMethodsPreferredByCustomerCategory(retailTransactionsDataFrame)

        case 3 :

            FindAverageItemsBoughtPerStoreType(retailTransactionsDataFrame)

        case _ :

            print("Invalid input received...Please try again")












