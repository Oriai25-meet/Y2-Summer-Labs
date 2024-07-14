import random
good_days_count = 0
temperatures = []
good_days = []
for i in range(7):
	temperatures.append(random.randint(26,40))
days_of_the_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for i in range(len(days_of_the_week)):
	if temperatures[i] % 2 == 0:
		good_days.append(days_of_the_week[i])
		good_days_count+=1
for i in range(len(days_of_the_week)):
	print(days_of_the_week[i],":", temperatures[i])
print("shelly had",good_days_count, "good days")
print("the good days:",good_days)
highest_temp = max(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
print("highest temp:",highest_temp, "on", highest_temp_day)

lowest_temp = min(temperatures)
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]
print("lowest temp:",lowest_temp,"on",lowest_temp_day)

above_avg = []
avg = sum(temperatures)/len(temperatures)
for i in temperatures:
	if i>avg:
		above_avg.append(i)
print("the average temp was:",avg)
print("list of above avg:", above_avg)

sorted_temp = sorted(temperatures)
print("sorted list:",sorted_temp)
