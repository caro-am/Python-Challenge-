import csv

#starting values 
months = 0
total  = 0
GreatestIncrease = ['','0']
GreatestDecrease = ['','0']
ProfitLosses = []

#to open and read csv files 
with open('Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i, row in enumerate(reader):
# != not eaual to         
        if i != 0:
            value = int(row[0].split(',')[1])
            months += 1
            total += value 
# checks and updates greates value            
            if int(GreatestIncrease[1]) < value:
                GreatestIncrease[0] = row[0].split(',')[0]
                GreatestIncrease[1] = str(value)
# checks and updates smallest value            
            elif int(GreatestDecrease[1]) > value:
                 GreatestDecrease[0] = row[0].split(',')[0]
                 GreatestDecrease[1] = str(value)
#checks so se if its a negative 
            if value < 0:
                ProfitLosses.append(value) 
                
#prints the results 
print('Financial Analysis\n----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sum(ProfitLosses)/len(ProfitLosses), 2)}')
print(f'Greatest Increase: {GreatestIncrease[0]} (${GreatestIncrease[1]})')
print(f'Greatest Decrease: {GreatestDecrease[0]} (${GreatestDecrease[1]})')

#write to txt file 
#create new line with /n
Analysis = open("analysis/FinancialReport.txt", "w+")
Analysis.write('Financial Analysis\n----------------------------\n')
Analysis.write(f'Total Months: {months}\n')
Analysis.write(f'Total: ${total}\n')
Analysis.write(f'Average Change: ${round(sum(ProfitLosses)/len(ProfitLosses), 2)}\n')
Analysis.write(f'Greatest Increase: {GreatestIncrease[0]} (${GreatestIncrease[1]})\n')
Analysis.write(f'Greatest Decrease: {GreatestDecrease[0]} (${GreatestDecrease[1]})')
Analysis.close()

print("Exported Results as text file.")
