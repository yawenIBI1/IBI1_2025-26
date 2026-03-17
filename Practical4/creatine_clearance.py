# Pseudocode comments :
# 1. Define and store variables: age (years), weight (kg), gender (male/female), cr (µmol/l)
# 2. Validate input ranges using conditional checks:
#    - age < 100
#    - 20 < weight < 80
#    - 0 < cr < 100
#    - gender either 'male' or 'female'
# 3. If validation fails, report exactly which input variable needs correction
# 4. If validation passes, calculate CrCl using the given formula:
#    CrCl = ((140 - age) * weight) / (72 * cr) * (0.85 if female)
# 5. Output the final calculated CrCl rate

def calculate_creatinine_clearance(age, weight, gender, cr):
    """
    Validates inputs and calculates Creatinine Clearance (CrCl) using the provided formula.
    """
    # Step 1: Input validation checks
    if age >= 100:
        return "Error: Age needs correction (must be less than 100 years)."
    if weight <= 20 or weight >= 80:
        return "Error: Weight needs correction (must be between 20 kg and 80 kg)."
    if cr <= 0 or cr >= 100:
        return "Error: Creatinine concentration needs correction (must be between 0 and 100 µmol/l)."
    if gender not in ["male", "female"]:
        return "Error: Gender needs correction (must be 'male' or 'female')."
    
    # Step 2: Calculate CrCl 
    if gender == "male":  # distinguish gender
        crcl = (140 - age) * weight / (72 * cr)
    else:  # female
        crcl = (140 - age) * weight * 0.85 / (72 * cr)
    
    # Return the result with correct units
    return crcl

# Store the values of the person's data in variables 
if __name__ == "__main__":
    # Example data - you can change these values to test
    patient_age = 50
    patient_weight = 70
    patient_gender = "male"
    patient_cr = 80  # Unit: µmol/l 

    # Calculate and get result (either error message or number)
    result = calculate_creatinine_clearance(patient_age, patient_weight, patient_gender, patient_cr)

    # Check if result is an error message (string) or a number
    if isinstance(result, str):
        # Print error if it if a string
        print(result)
    else:
        # Print the final calculated rate with 2 decimal places
        # Using str() as hinted in the question to convert number to string
        print("Estimated Creatinine Clearance Rate: " + str(round(result, 2)) + " mL/min")