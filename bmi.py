def calculate_bmi():
    print("--- BMI Calculator ---")
    try:
        weight = float(input("Weight (kg) darj karein: "))
        height = float(input("Height (meters) darj karein: "))
        
        bmi = weight / ((height / 100) ** 2)
        print(f"Aapka BMI hai: {bmi:.2f}")

        if bmi < 18.5:
            print("Status: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Status: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Status: Overweight")
        else:
            print("Status: Obese")
    except ValueError:
        print("Kripya sahi number enter karein.")

calculate_bmi()