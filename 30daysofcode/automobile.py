loan_amt, insurance, gas, oil, tires, maintainance, = (int(input('Enter monthly loan amount: >>')),
                                                      int(input('Enter monthly insurance amount: >>')),
                                                      int(input('Enter monthly gas amount: >>')),
                                                      int(input('Enter monthly oil amount: >>')),
                                                      int(input('Enter monthly tires amount: >>')),
                                                      int(input('Enter monthly tires amount: >>')))
total_amt = loan_amt+insurance+gas+oil+tires+maintainance
print(f"The total monthly expense is ${total_amt}")
print(f"The total annual expense is ${total_amt*12}")

'''
Implementation in a function
def auto(loan_amt, insurance, gas, oil, tires, maintainance):
    total_amt = loan_amt+insurance+gas+oil+tires+maintainance
    return f"The total monthly expense is ${total_amt}", f"The total annual expense is ${total_amt*12}"
'''