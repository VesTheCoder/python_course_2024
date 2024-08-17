while True:
    try: a = float(input("Input any number: "))
    except ValueError:
        print("Incorrect input. Please input a number.")
    
    try: b = float(input("Input any number: "))
    except ValueError:
        print("Incorrect input. Please input a number.")
   
    try: c = a / b
    except ValueError:
        print("We can't devide by zero.")
        try: b = float(input("Input any number (not 0): "))
        except ValueError:
            print("Incorrect input. Please input a number.")
        else: continue
    else: print(f"NIIIICEEE!!!, {a} / {b} = {c}")