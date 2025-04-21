print("Welcome to the armstrong Number Checker🎉🎉")
print("Enter any number and I will print if it is an Armstrong number🤔🤔🤔🤔\n")
num=int(input("🔢🔢🔢Enter a number: "))
power=len(str(num))
armstrong_sum=sum(int(digit)**power for digit in str(num))
if num==armstrong_sum:
    print(f"Yes, {num} It is a Armstrong number🎉🎉🎉🎉🎉🎉")
else:
    print(f"No,{num} is not a armstrong number❌❌❌❌❌")