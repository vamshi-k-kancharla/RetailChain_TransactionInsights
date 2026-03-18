
'''
    Sub Task Input values to analyze promotion and discount impact
'''

def PrintSubTaskInputParameterDetails() :

    print("1 :=> Impact of discount on Average Cost")
    print("2 :=> Average no of items purchased per Promotion Type")
    print("3 :=> Most effective Promotion type for maximum Total Cost")
    print("4 :=> Exit the code")

    print('\n')


'''
    Impact of discount on Average Cost
'''

def FindImpactOfDiscountOnAverageCost(retailTransactionsDataFrame) :

    print(retailTransactionsDataFrame[['Discount_Applied', 'Total_Cost']].groupby('Discount_Applied').mean())


'''
    Average no of items purchased per Promotion Type
'''

def FindAvgNoOfItemsBoughtPerPromotion(retailTransactionsDataFrame) :

    print(retailTransactionsDataFrame[['Promotion', 'Total_Items']].groupby('Promotion').mean())


'''
    Most effective Promotion type for maximum Total Cost
'''

def FindMostEffectivePromotionForMaxTotalCost(retailTransactionsDataFrame) :

    print(retailTransactionsDataFrame[['Promotion', 'Total_Cost']].groupby('Promotion').sum().sort_values(by='Total_Cost', ascending=False).head(1))


'''
    Process the Impact of Promotion and Discount on Sales
'''

def ProcessImpactOfPromotionAndDiscount(retailTransactionsDataFrame) :

    PrintSubTaskInputParameterDetails()
    task = int(input('enter the given Sub task input : '))

    print('\n')

    match task :

        case 1 :

            FindImpactOfDiscountOnAverageCost(retailTransactionsDataFrame)

        case 2 :

            FindAvgNoOfItemsBoughtPerPromotion(retailTransactionsDataFrame)

        case 3 :

            FindMostEffectivePromotionForMaxTotalCost(retailTransactionsDataFrame)

        case _ :

            print("Invalid input received...Please try again")












