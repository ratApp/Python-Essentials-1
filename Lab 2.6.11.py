# Lab 2.6.11

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
start_time = hour * 60 + mins   # Start time converted to minutes

end_time = start_time + dura    # Total end time in minutes
end_time_hr = end_time // 60    # Output hours of the end time
end_time_min = end_time % 60    # Output minutes of the end time
print(end_time_hr, end_time_min, sep=":")     #Prints end time in HH:MM format
