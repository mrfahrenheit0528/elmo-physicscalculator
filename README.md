# Physics Calculator

A command-line **physics calculator written in Python** that solves common introductory physics equations through either manual user input or a text-based problem set.

This project was developed during my **first year** as an introductory programming project combining basic physics concepts with Python.

---

## Project Explanation

ELMO Physics Calculator was created to simplify repetitive calculations for common physics problems.

The program allows users to select a physics quantity, enter the required values, and automatically calculate the result.

It also includes a simple file-processing mode where multiple problems can be written in a text file and processed automatically.

---

## Key Features

- Menu-driven command-line interface
- 20 supported physics calculations
- Manual input mode
- Text-file problem processing
- Automatic result output to a text file
- Basic input validation
- Colored terminal messages using Colorama
- Functions separated according to individual physics formulas

---

## Supported Calculations

### Kinematics

- Velocity
- Displacement
- Acceleration

### Forces, Motion & Energy

- Force
- Friction Force
- Tension Force
- Weight
- Momentum
- Impulse
- Centripetal Force
- Centripetal Acceleration
- Work
- Kinetic Energy
- Gravitational Potential Energy
- Elastic Potential Energy
- Work Done by Elastic Potential Energy
- Power

### Fluids & Gravitation

- Pressure
- Buoyant Force
- Gravitational Force

---

## Methodology

The program was built by translating common introductory physics equations into individual Python functions.

Two methods of interaction were implemented:

1. **Manual Mode** — the user selects a quantity, enters the required values, and receives the calculated result directly in the terminal.
2. **Problem Set Mode** — the program reads formatted problems from `physics_problem.txt`, extracts the requested calculation and given values, performs the calculations, and saves the results to `physics_answer.txt`.

---

## Results

The completed application can perform multiple introductory physics calculations from a single command-line program.

The project helped demonstrate the use of:

- Python functions
- Conditional statements
- Loops
- Exception handling
- File reading and writing
- String parsing
- Mathematical formulas
- User input validation

---

## Tech Stack

**Language:** Python  
**Libraries:** `math`, `time`, Colorama  
**Interface:** Command Line / Terminal  
**Input:** Keyboard or `.txt` problem set  
**Output:** Terminal or `.txt` answer file

---

## Usage

### 1. Clone the Repository

```bash id="97w0g0"
git clone https://github.com/mrfahrenheit0528/elmo-physicscalculator.git
cd elmo-physicscalculator
```

### 2. Install Colorama

```bash id="tbdkgt"
pip install colorama
```

### 3. Run the Program

```bash id="zw4x15"
python main.py
```

---

## Manual Calculator

When prompted:

```text id="71vfq6"
Do you want to use a problem set in a txt file? y/n:
```

Enter:

```text id="xza28a"
n
```

The program displays the available calculations.

Example:

```text id="ud5t45"
1) Velocity
2) Displacement
3) Acceleration
4) Force
...
20) Gravitational Force
```

Select the calculation and enter the requested values.

---

## Problem Set Mode

The calculator can also process problems from:

```text id="h1dp5u"
physics_problem.txt
```

A problem follows a simple format using `Find` and `Given`.

Example:

```text id="wcwz0m"
Find Velocity
Given: Initial Velocity=10m/s, Acceleration=2m/s2, Time=5s
```

Run the program and choose:

```text id="29jeqf"
y
```

The calculated results are written to:

```text id="gvqdz3"
physics_answer.txt
```

---

## Developer

**Guiller Angelo Hermoso**

Developed during my first year as an introductory Python programming project.
