import csv

months = 0
total  = 0
GreatestIncrease = ['','0']
GreatestDecrease = ['','0']
ProfitLosses = []

with open('Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i, row in enumerate(reader):
        if i != 0:
            value = int(row[0].split(',')[1])
            months += 1
            total += value
            if int(GreatestIncrease[1]) < value:
                GreatestIncrease[0] = row[0].split(',')[0]
                GreatestIncrease[1] = str(value)
            elif int(GreatestDecrease[1]) > value:
                 GreatestDecrease[0] = row[0].split(',')[0]
                 GreatestDecrease[1] = str(value)
            if value < 0:
                ProfitLosses.append(value)

print('Financial Analysis\n----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sum(ProfitLosses)/len(ProfitLosses), 2)}')
print(f'Greatest Increase: {GreatestIncrease[0]} (${GreatestIncrease[1]})')
print(f'Greatest Decrease: {GreatestDecrease[0]} (${GreatestDecrease[1]})')

Analysis = open("analysis/FinancialReport.txt", "w+")
Analysis.write('Financial Analysis\n----------------------------\n')
Analysis.write(f'Total Months: {months}\n')
Analysis.write(f'Total: ${total}\n')
Analysis.write(f'Average Change: ${round(sum(ProfitLosses)/len(ProfitLosses), 2)}\n')
Analysis.write(f'Greatest Increase: {GreatestIncrease[0]} (${GreatestIncrease[1]})\n')
Analysis.write(f'Greatest Decrease: {GreatestDecrease[0]} (${GreatestDecrease[1]})')
Analysis.close()

print("Exported Results as text file.")
