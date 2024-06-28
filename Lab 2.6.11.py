# Lab 2.6.11

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
start_time = hour * 60 + mins   # start time in minutes

end_time = start_time + dura
end_time_hr = end_time // 60
end_time_min = end_time % 60
print(end_time_hr, end_time_min, sep=":")
