#Ternary Operators 

"The ternary operator allows you to assing one value if a condition is true or else false"

age = 17 

eligibilityCheck = "Eligible" if (age >= 18) else "Not Eligible"
print(eligibilityCheck)


#instead of elif 

#The ternary operator can be used instead of elif in longer if statement


signal = "srange"

checkSignal = "Go!" if(signal == "Green" or signal == "green") else "Get Ready!" if(signal == "Orange" or signal == "orange") else "Stop!"
print(checkSignal)