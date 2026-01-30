import math

def trig_calculator():
    print("--- Quick Trig Calculator ---")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tg/tan)")
    print("4. Cotangent (ctg/cot)")
    
    choice = input("\nSelect a function (1-4): ")
    angle_deg = float(input("Enter the angle in degrees: "))
    
    # Convert degrees to radians
    # Equation: radians = degrees * (pi / 180)
    angle_rad = math.radians(angle_deg)

    try:
        if choice == '1':
            result = math.sin(angle_rad)
            print(f"sin({angle_deg}°) = {round(result, 4)}")
            
        elif choice == '2':
            result = math.cos(angle_rad)
            print(f"cos({angle_deg}°) = {round(result, 4)}")
            
        elif choice == '3':
            # Tangent is undefined at 90, 270, etc.
            result = math.tan(angle_rad)
            print(f"tg({angle_deg}°) = {round(result, 4)}")
            
        elif choice == '4':
            # Cotangent is 1/tan. Undefined at 0, 180, etc.
            result = 1 / math.tan(angle_rad)
            print(f"ctg({angle_deg}°) = {round(result, 4)}")
            
        else:
            print("Invalid selection.")
            
    except ZeroDivisionError:
        print(f"Error: The function is undefined for {angle_deg}°.")

if __name__ == "__main__":
    trig_calculator()
