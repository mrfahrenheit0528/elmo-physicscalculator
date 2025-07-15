import math
from colorama import Fore
import time

# 1st quarter: Kinematics equations for velocity, displacement, and acceleration
def find_velocity(vi, t, a):
    velocity = vi + (a*t)
    return velocity

def find_displacement(vi, t, a):
    displacement = (vi*t) + ((a/2)*(t**2))
    return displacement

def find_acceleration(vf, vi, t):
    acceleration = (vf - vi)/t
    return acceleration

# 2nd quarter: Forces, friction, tension, weight, momentum, impulse, centripetal force, centripetal acceleration, work, kinetic energy, gravitational potential energy, elastic potential energy, work done on elastic potential energy, power
def find_force(m, a):
    force = m*a
    return force

def find_frictionf(uu, Fn):
    frictionf = uu * Fn
    return frictionf

def find_tensionf(w, m, a):
    tensionf = w + (m*a)
    return tensionf

def find_weight(m):
    weight = m*9.80665
    return weight

def find_momentum(m, v):
    momentum = m*v
    return momentum

def find_impulse(fi, ff, t):
    impulse = (ff-fi)*t
    return impulse

def find_centripetalf(v, m, r):
    centripetalf = (m*(v**2))/r
    return centripetalf

def find_centripetalA(v, r):
    centripetalA = (v**2)/r
    return centripetalA

def find_work(f, d, angle):
    work = f*d*(math.cos(angle))
    return work

def find_kineticE(m, v):
    kineticE = (m(v**2))/2
    return kineticE

def find_gpE(m, h):
    gpE = m*9.80665*h
    return gpE

def find_epE(k, d):
    epE = (k/2)*(d**2)
    return epE

def find_WepE(k, xi, xf):
    WepE = ((k/2)*(xi**2))-((k/2)*(xf**2))
    return WepE

def find_power(W, t):
    power = W/t
    return power

# 3rd quarter: Pressure, buoyant force, gravitational force
def find_pressure(f, area):
    pressure = f/area
    return pressure

def find_buoyantf(density, V):
    buoyantf = density*V*9.80665
    return buoyantf

def find_gravitationalf(m1, m2, d):
    gravitaionalf = (6.674*(10**-11))*((m1*m2)/(d**2))
    return gravitaionalf

# File handling functions

# Reads operations and givens from a file and returns them
def read_from_file(filename):
    while True:
        try:
            open(filename, "r")
        except FileNotFoundError:
            print(f'{Fore.RED}The problem set file doesn\'t exist. please create it first inside your folder before proceeding to this option and try again. \nYou can use the manual physics calculator if you don\'t have problem set file.{Fore.WHITE}')
            time.sleep(4)
            break
        with open(filename, "r") as file:
            operations = []  # List to store operations (e.g., FIND_VELOCITY)
            givens = []  # List to store given values for each operation
            for line in file:
                    if 'Find' in line:
                        strpdline = line.rstrip("\n")
                        operation = strpdline.split(" ")
                        operation.pop(0)
                        operations.append(str(operation[0].upper()))
                    if 'Given' in line:
                        a = {}
                        strpdline = line.rstrip("\n").lstrip("Given: ")
                        given = strpdline.split(",")
                        for i in given:
                            individual_given = i.split("=")
                            a[individual_given[0].lstrip(' ').rstrip(' ').upper()] = individual_given[1].strip(' ')
                        givens.append(a)
        return operations, givens
        break
        
            

# Removes non-numeric characters from a string (useful for extracting numerical values with units)
def remove_unit(string):
    result = ""
    for i in range(len(string)):
        if string[i].isdigit() or string[i] == ".":
            result += string[i]
        else:
            break
    return result

# Appends data to a file
def save_to_file(data, filename):
    with open(filename, "a") as file:
        file.write(data)

# Welcome message for the physics calculator program
print("Welcome to our Physics Calculator.")
print("With this program, you can calculate simple and basic physics calculations.")

# Infinite loop to repeatedly prompt the user for input
while True:
    # Asking the user if they want to use a problem set from a text file
    choice = input(f'Do you want to use a problem set in a txt file? y/n: \n{Fore.LIGHTGREEN_EX}TIPS!: Your Physics problem set should be written in a "physics_problem.txt" file. The variable you\'re solving for must be indicated by a word "Find", followed by the given variables from the problem set on the next line. \nThe given variables must be indicated by the word "Given", all must be on a single line and seperated by a comma. The given variable must also be seperated from its value with an = sign. Don\'t abbreviate the variables. {Fore.WHITE}').lower()
    # If the user chooses to use a problem set from a file
    if choice =="y":
         # Read operations and givens from the "physics_problem.txt" file
        if (read_from_file("physics_problem.txt")) == None:
            break
        else:
            operations = read_from_file("physics_problem.txt")
         # Loop through each operation in the problem set
        for i in operations:
            count = 0
            numbering = 1
            print(operations)
            # Loop through each operation type (e.g., VELOCITY, DISPLACEMENT, etc.)
            for j in i:
                if j == "VELOCITY":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")# Save numbering to the output file
                     # Extract given values from the givens list
                    if (operations[1][count].get("TIAL VELOCITY")) == None:
                        vi = 0
                    else:
                        vi = float(remove_unit(operations[1][count].get("TIAL VELOCITY")))
                    if (operations[1][count]).get("ACCELERATION") == None:
                        a = 0
                    else:
                        a = float(remove_unit(operations[1][count].get("ACCELERATION")))
                    if (operations[1][count]).get("TIME") == None:
                        t = 0
                    else:
                        t = float(remove_unit(operations[1][count].get("TIME")))
                    velocity = (find_velocity(vi, t, a))
                    save_to_file(f"With the given: vi = {vi}m/s, a = {a}m/s2, and t = {t}s, the velocity is {velocity}m/s.\n", "physics_answer.txt")
                
                elif j == "DISPLACEMENT":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("TIAL VELOCITY")) == None:
                        vi = 0
                    else:
                        vi = float(remove_unit(operations[1][count].get("TIAL VELOCITY")))
                    if (operations[1][count]).get("ACCELERATION") == None:
                        a = 0
                    else:
                        a = float(remove_unit(operations[1][count].get("ACCELERATION")))
                    if (operations[1][count]).get("TIME") == None:
                        t = 0
                    else:
                        t = float(remove_unit(operations[1][count].get("TIME")))
                    displacement = (find_displacement(vi, t, a))
                    save_to_file(f"With the given: vi = {vi}m/s, a = {a}m/s2, and t = {t}s, the displacement is {displacement}m.\n", "physics_answer.txt")
                
                elif j == "ACCELERATION":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("TIAL VELOCITY")) == None:
                        vi = 0
                    else:
                        vi = float(remove_unit(operations[1][count].get("TIAL VELOCITY")))
                    if (operations[1][count]).get("FINAL VELOCITY") == None:
                        vf = 0
                    else:
                        vf = float(remove_unit(operations[1][count].get("FINAL VELOCITY")))
                    if (operations[1][count]).get("TIME") == None:
                        t = 0
                    else:
                        t = float(remove_unit(operations[1][count].get("TIME")))
                    acceleration = (find_acceleration(vf, vi, t))
                    save_to_file(f"With the given: vi = {vi}m/s, vf = {vf}m/s, and t = {t}s, the acceleration is {acceleration}m.\n", "physics_answer.txt")
                
                elif j == "FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("MASS")) == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("ACCELERATION") == None:
                        a = 0
                    else:
                        a = float(remove_unit(operations[1][count].get("ACCELERATION")))
                    force = (find_force(m, a))
                    save_to_file(f"With the given: m = {m}kg and a = {a}m/s2, the force is {force}N.\n", "physics_answer.txt")
                
                elif j == "FRICTION FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("U")) == None:
                        uu = 0
                    else:
                        uu = float(remove_unit(operations[1][count].get("U")))
                    if (operations[1][count]).get("NORMAL FORCE") == None:
                        Fn = 0
                    else:
                        Fn = float(remove_unit(operations[1][count].get("NORMAL FORCE")))
                    frictionf = (find_frictionf(uu, Fn))
                    save_to_file(f"With the given: u = {uu} and Fn = {Fn}N, the friction force is {frictionf}N.\n", "physics_answer.txt")
                
                elif j == "TENSION FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("WEIGHT")) == None:
                        w = 0
                    else:
                        w = float(remove_unit(operations[1][count].get("WEIGHT")))
                    if (operations[1][count]).get("MASS") == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("ACCELERATION") == None:
                        a = 0
                    else:
                        a = float(remove_unit(operations[1][count].get("ACCELERATION")))
                    tensionf = (find_tensionf(w, m, a))
                    save_to_file(f"With the given: w = {w}N, m = {m}kg, and a = {a}m/s2, the tension force is {tensionf}N.\n", "physics_answer.txt")
                
                elif j == "WEIGHT":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count]).get("MASS") == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    weight = (find_weight(m))
                    save_to_file(f"With the given mass, which is = {m}kg, the weight is {w}N.\n", "physics_answer.txt")
                
                elif j == "MOMENTUM":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count]).get("MASS") == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("VELOCITY") == None:
                        v = 0
                    else:
                        v = float(remove_unit(operations[1][count].get("VELOCITY")))
                    momentum = (find_momentum(m, v))
                    save_to_file(f"With the given: m = {m}kg and v = {v}m/s, the momentum is is {momentum}kgm/s.\n", "physics_answer.txt")
                
                elif j == "IMPULSE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("TIAL FORCE")) == None:
                        fi = 0
                    else:
                        fi = float(remove_unit(operations[1][count].get("TIAL FORCE")))
                    if (operations[1][count]).get("FINAL FORCE") == None:
                        ff = 0
                    else:
                        ff = float(remove_unit(operations[1][count].get("FINAL FORCE")))
                    if (operations[1][count]).get("TIME") == None:
                        t = 0
                    else:
                        t = float(remove_unit(operations[1][count].get("TIME")))
                    impulse = (find_impulse(fi, ff, t))
                    save_to_file(f"With the given: fi = {fi}N, ff = {ff}N, and t = {t}s, the impulse is {impulse}Ns.\n", "physics_answer.txt")
                
                elif j == "CENTRIPETAL FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("VELOCITY")) == None:
                        v = 0
                    else:
                        v = float(remove_unit(operations[1][count].get("VELOCITY")))
                    if (operations[1][count]).get("MASS") == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("RADIUS") == None:
                        r = 0
                    else:
                        r = float(remove_unit(operations[1][count].get("RADIUS")))
                    centripetalf = (find_centripetalf(v, m, r))
                    save_to_file(f"With the given: v = {v}m/s, m = {m}kg, and r = {r}m, the centripetal force is {centripetalf}N.\n", "physics_answer.txt")
                
                elif j == "CENTRIPETAL ACCELERATION":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("VELOCITY")) == None:
                        v = 0
                    else:
                        v = float(remove_unit(operations[1][count].get("VELOCITY")))
                    if (operations[1][count]).get("RADIUS") == None:
                        r = 0
                    else:
                        r = float(remove_unit(operations[1][count].get("RADIUS")))
                    centripetalA = (find_centripetalA(v, r))
                    save_to_file(f"With the given: v = {v}m/s and r = {r}m, the centripetal acceleration is {centripetalA}m/s2.\n", "physics_answer.txt")
                
                elif j == "WORK":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("FORCE")) == None:
                        f = 0
                    else:
                        f = float(remove_unit(operations[1][count].get("FORCE")))
                    if (operations[1][count]).get("DISPLACEMENT") == None:
                        d = 0
                    else:
                        d = float(remove_unit(operations[1][count].get("DISPLACEMENT")))
                    if (operations[1][count]).get("ANGLE") == None:
                        angle = 0
                    else:
                        angle = float(remove_unit(operations[1][count].get("ANGLE")))
                    work = (find_work(f, d, angle))
                    save_to_file(f"With the given: f = {f}N, d = {d}m, and angle = {angle}°, the work done is {work}Nm.\n", "physics_answer.txt")
                
                elif j == "KINETIC ENERGY":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("MASS")) == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("VELOCITY") == None:
                        v = 0
                    else:
                        v = float(remove_unit(operations[1][count].get("VELOCITY")))
                    kineticE = (find_kineticE(m, v))
                    save_to_file(f"With the given: m = {m}kg and v = {v}m/s, the kinetic energy is {kineticE}J.\n", "physics_answer.txt")
                
                elif j == "GRAVITATIONAL POTENTIAL ENERGY":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count]).get("MASS") == None:
                        m = 0
                    else:
                        m = float(remove_unit(operations[1][count].get("MASS")))
                    if (operations[1][count]).get("HEIGHT") == None:
                        h = 0
                    else:
                        h = float(remove_unit(operations[1][count].get("HEIGHT")))
                    gpE = (find_gpE(m, h))
                    save_to_file(f"With the given: m = {m}kg and h = {h}m, the gravitational potential energy is {gpE}J/kg.\n", "physics_answer.txt")
                
                elif j == "ELASTIC POTENTIAL ENERGY":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("SPRING CONSTANT")) == None:
                        k = 0
                    else:
                        k = float(remove_unit(operations[1][count].get("SPRING CONSTANT")))
                    if (operations[1][count]).get("DISPLACEMENT") == None:
                        d = 0
                    else:
                        d = float(remove_unit(operations[1][count].get("DISPLACEMENT")))
                    epE = (find_epE(k, d))
                    save_to_file(f"With the given: k = {k}N/m and d = {d}m, the elastic potential energy is {epE}J.\n", "physics_answer.txt")
                
                elif j == "POWER":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("WORK")) == None:
                        W = 0
                    else:
                        W = float(remove_unit(operations[1][count].get("WORK")))
                    if (operations[1][count]).get("TIME") == None:
                        t = 0
                    else:
                        t = float(remove_unit(operations[1][count].get("TIME")))
                    power = (find_power(W, t))
                    save_to_file(f"With the given: W = {W}Nm and t = {t}s, the power is {power}Nm/s.\n", "physics_answer.txt")
                
                elif j == "PRESSURE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("FORCE")) == None:
                        f = 0
                    else:
                        f = float(remove_unit(operations[1][count].get("FORCE")))
                    if (operations[1][count]).get("AREA") == None:
                        area = 0
                    else:
                        area = float(remove_unit(operations[1][count].get("AREA")))
                    pressure = (find_pressure(f, area))
                    save_to_file(f"With the given: f = {f}N and area = {area}m2, the pressure is {pressure}Pa.\n", "physics_answer.txt")
                
                elif j == "BUOYANT FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("DENSITY")) == None:
                        density = 0
                    else:
                        density = float(remove_unit(operations[1][count].get("DENSITY")))
                    if (operations[1][count]).get("VOLUME") == None:
                        V = 0
                    else:
                        v = float(remove_unit(operations[1][count].get("VOLUME")))
                    buoyantf = (find_buoyantf(density, V))
                    save_to_file(f"With the given: density = {density}kg/l and volume = {v}m3, the buoyant force is {buoyantf}N.\n", "physics_answer.txt")
                
                elif j == "GRAVITATIONAL FORCE":
                    save_to_file(f"{numbering}) ", "physics_answer.txt")
                    if (operations[1][count].get("M1")) == None:
                        m1 = 0
                    else:
                        m1 = float(remove_unit(operations[1][count].get("M1")))
                    if (operations[1][count]).get("M2") == None:
                        m2 = 0
                    else:
                        m2 = float(remove_unit(operations[1][count].get("M2")))
                    if (operations[1][count]).get("DISTANCE") == None:
                        d = 0
                    else:
                        d = float(remove_unit(operations[1][count].get("DISTANCE")))
                    gravitationalf = (find_gravitationalf(m1, m2, d))
                    save_to_file(f"With the given: mass 1 = {m1}kg, mass 2 = {m2}kg, and distance = {d}m, the gravitational force is {gravitationalf}N.\n", "physics_answer.txt")
                count += 1
                numbering += 1 # Increment the numbering for the next result
        print('Done! Check your folder for physics_answer.txt')
# End of the infinite loop

# If the user chooses not to use a problem set from a file
    elif choice == "n":
        print(f"{Fore.GREEN}Okay, please select then what physics variable you\'re solving for.")
        print(f"{Fore.YELLOW}1) Velocity")
        print(f"{Fore.YELLOW}2) Displacement")
        print(f"{Fore.YELLOW}3) Acceleration")
        print(f"{Fore.YELLOW}4) Force")
        print(f"{Fore.YELLOW}5) Friction Force")
        print(f"{Fore.YELLOW}6) Tension Force")
        print(f"{Fore.YELLOW}7) Weight")
        print(f"{Fore.YELLOW}8) Momentum")
        print(f"{Fore.YELLOW}9) Impulse")
        print(f"{Fore.YELLOW}10) Centripetal Force")
        print(f"{Fore.YELLOW}11) Centripetal Acceleration")
        print(f"{Fore.YELLOW}12) Work")
        print(f"{Fore.YELLOW}13) Kinetic Energy")
        print(f"{Fore.YELLOW}14) Gravitational Potential Energy")
        print(f"{Fore.YELLOW}15) Elastic Potential Energy")
        print(f"{Fore.YELLOW}16) Work done by Elastic Potential Energy")
        print(f"{Fore.YELLOW}17) Power")
        print(f"{Fore.YELLOW}18) Pressure")
        print(f"{Fore.YELLOW}19) Buoyant Force")
        print(f"{Fore.YELLOW}20) Gravitational Force")
        print(f"{Fore.YELLOW}0) I don't need this, I'm Einstein{Fore.WHITE}")
# End of the if-elif-else block

# Infinite loop to repeatedly prompt the user for input until a valid choice is made
        while True:
            try:
                # Attempt to convert the user input to an integer
                choice = int(input("Enter the corresponding number of your choice: "))
            except:
                if ValueError:
                    print("Please enter a NUMBER that corresponds to your choice")
                # Check if the entered choice is outside the valid range (0 to 20)
                elif choice <0 or choice >20: 
                 # Handle the case where the user enters a non-numeric value
                    print("Please enter a NUMBER that corresponds to your choice")
                continue  # Continue the loop to prompt the user again

# Check the user's choice and perform corresponding calculations or exit                
            if choice == 0:
                print("okay then, goodbye!")
                break

            elif choice == 1:
                print(f"{Fore.RED}Find Velocity{Fore.WHITE}")
                while True:
                    try:
                        vi = int(input("Enter the initial velocity: "))
                        t = int(input("Enter the time: "))
                        a = int(input("Enter the acceleration: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated velocity is {find_velocity(vi, t, a)} m/s')
                    break
            
            elif choice == 2:
                print(f"{Fore.RED}Find Displacement{Fore.WHITE}")
                while True:
                    try:
                        vi = int(input("Enter the initial velocity: "))
                        t = int(input("Enter the time: "))
                        a = int(input("Enter the acceleration: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated displacement is {find_displacement(vi, t, a)} m')
                    break

            elif choice == 3:
                print(f"{Fore.RED}Find Acceleration{Fore.WHITE}")
                while True:
                    try:
                        vi = int(input("Enter the initial velocity: "))
                        vf = int(input("Enter the final velocity: "))
                        t = int(input("Enter the time: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated acceleration is {find_acceleration(vf, vi, t)} m/s2')
                    break

            elif choice == 4:
                print(f"{Fore.RED}Find Force{Fore.WHITE}")
                while True:
                    try:
                        m = int(input("Enter the mass: "))
                        a = int(input("Enter the acceleration: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated force is {find_force(m, a)} N')
                    break

            elif choice == 5:
                print(f"{Fore.RED}Find Friction Force{Fore.WHITE}")
                while True:
                    try:
                        uu = int(input("Enter the  friction coefficient: "))
                        Fn = int(input("Enter the normal force: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated friction force is {find_frictionf(uu, Fn)} N')
                    break

            elif choice == 6:
                print(f"{Fore.RED}Find Tension Force{Fore.WHITE}")
                while True:
                    try:
                        w = int(input("Enter the weight: "))
                        m = int(input("Enter the mass: "))
                        a = int(input("Enter the acceleration: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated tension force is {find_tensionf(w, m, a)} N')
                    break
            
            elif choice == 7:
                print(f"{Fore.RED}Find Weight{Fore.WHITE}")
                while True:
                    try:
                        m = int(input("Enter the mass: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated weight is {find_weight(m)} N')
                    break
            
            elif choice == 8:
                print(f"{Fore.RED}Find Momentum{Fore.WHITE}")
                while True:
                    try:
                        m = int(input("Enter the  mass: "))
                        v = int(input("Enter the velocity: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated momentum is {find_momentum(m, v)} kgm/s')
                    break

            elif choice == 9:
                print(f"{Fore.RED}Find Impulse{Fore.WHITE}")
                while True:
                    try:
                        fi = int(input("Enter the initial velocity: "))
                        ff = int(input("Enter the final velocity: "))
                        t = int(input("Enter the time: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated impulse is {find_impulse(fi, ff, t)} Ns')
                    break
            
            elif choice == 10:
                print(f"{Fore.RED}Find Centripetal Force{Fore.WHITE}")
                v = int(input("Enter the velocity: "))
                m = int(input("Enter the mass: "))
                r = int(input("Enter the radius: "))
                print(f'The calculated centripetal force is {find_centripetalf(v, m, r)} N')
            
            elif choice == 11:
                print(f"{Fore.RED}Find Centripetal Acceleration{Fore.WHITE}")
                while True:
                    try:
                        v = int(input("Enter the velocity: "))
                        r = int(input("Enter the radius: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated centripetal acceleration is {find_centripetalA(v, r)} m/s2')
                    break

            elif choice == 12:
                print(f"{Fore.RED}Find Work{Fore.WHITE}")
                while True:
                    try:
                        f = int(input("Enter the force: "))
                        d = int(input("Enter the displacement: "))
                        angle = int(input("Enter the angle: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated work is {find_work(f, d, angle)} Nm')
                    break
            
            elif choice == 13:
                print(f"{Fore.RED}Find Kinetic Energy{Fore.WHITE}")
                while True:
                    try:
                        m = int(input("Enter the mass: "))
                        v = int(input("Enter the velocity: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated kinetic energy is {find_kineticE(m, v)} J')
                    break
            
            elif choice == 14:
                print(f"{Fore.RED}Find Gravitational Potential Energy{Fore.WHITE}")
                while True:
                    try:
                        m = int(input("Enter the mass: "))
                        h = int(input("Enter the height of the object: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated gravitational potential energy is {find_gpE(m, h)} J/kg')
                    break

            elif choice == 15:
                print(f"{Fore.RED}Find Elastic Potential Energy{Fore.WHITE}")
                while True:
                    try:
                        k = int(input("Enter the spring constant: "))
                        d = int(input("Enter the displacement: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated elastic potential energy is {find_epE(k, d)} J')
                    break
            
            elif choice == 16:
                print(f"{Fore.RED}Find Work done by Elastic Potential Energy{Fore.WHITE}")
                k = int(input("Enter the spring constant: "))
                xi = int(input("Enter the initial position: "))
                xf = int(input("Enter the final position: "))
                print(f'The calculated work done by EPE is {find_WepE(k, xi, xf)} J')
            
            elif choice == 17:
                print(f"{Fore.RED}Find Power{Fore.WHITE}")
                while True:
                    try:
                        W = int(input("Enter the Work: "))
                        t = int(input("Enter the time: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated power is {find_power(W, t)} Nm/s')
                    break
            
            elif choice == 18:
                print(f"{Fore.RED}Find Pressure{Fore.WHITE}")
                while True:
                    try:
                        f = int(input("Enter the force: "))
                        area = int(input("Enter the area: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated pressure is {find_pressure(f, area)} Pa')
                    break
            
            elif choice == 19:
                print(f"{Fore.RED}Find Buoyant Force{Fore.WHITE}")
                while True:
                    try:
                        density = int(input("Enter the density: "))
                        V = int(input("Enter the volume: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated buoyant force is {find_buoyantf(density, V)} N')
                    break
            
            elif choice == 20:
                print(f"{Fore.RED}Find Gravitational Force{Fore.WHITE}")
                while True:
                    try:
                        m1 = int(input("Enter the mass of the first object: "))
                        m2 = int(input("Enter the mass of the second object: "))
                        d = int(input("Enter the distance between them: "))
                    except ValueError:
                        print(f"{Fore.LIGHTRED_EX}Input error, try all over again.{Fore.WHITE}")
                        continue
                    print(f'The calculated gravitational force is {find_gravitationalf(m1, m2, d):} N')
                    break
            
            break

# Loop for handling incorrect inputs and prompting the user to try again
    else:
        print('Wrong input. Please enter "y" if yes & "n" if no.')
    
# Prompt the user to continue with another calculation or exit
    continue_calculation = input("Do you want to continue performing calculations? (y/n): ").lower()
    if continue_calculation != "y":
        print("Thank you, Goodbye!")
        break
