# Import Statements
import emp

def main():
    """
    Create five of the ProductionWorker items and five of the ShiftSupervisor items from class
    emp and then print them.
    """
    # Create five items for ProductionWorker.
    employee1 = emp.ProductionWorker('Frank McMullen', '1001', '1', 25.00)
    employee2 = emp.ProductionWorker('Harriet Walter', '1002', '2', 22.50)
    employee3 = emp.ProductionWorker('Tom Walton', '1015', '3', 19.50)
    employee4 = emp.ProductionWorker('Mark Camacho', '1027', '1', 18.50)
    employee5 = emp.ProductionWorker('Pauline Golden', '1029', '3', 20.50)

    #Create five items for ShiftSupervisor.
    supervisor1 = emp.ShiftSupervisor('Ellen Duffy', '2010', 40000, 800.00)
    supervisor2 = emp.ShiftSupervisor('Rick Gonzalez', '2020', 39000, 750.00)
    supervisor3 = emp.ShiftSupervisor('Calvin Stafford', '2022', 42000, 500.00)
    supervisor4 = emp.ShiftSupervisor('Lindsey Newman', '2027', 46000, 900.00)
    supervisor5 = emp.ShiftSupervisor('Marta Salazar', '2031', 48000, 1000.00)

    # Print the five items for ProductionWorker
    print("Production worker information:")
    print("==============================\n")
    print(employee1)
    print()
    print(employee2)
    print()
    print(employee3)
    print()
    print(employee4)
    print()
    print(employee5)

    # Print the five items for ShiftSupervisor
    print("\nShift Supervisor information:")
    print("===============================\n")
    print(supervisor1)
    print()
    print(supervisor2)
    print()
    print(supervisor3)
    print()
    print(supervisor4)
    print()
    print(supervisor5)

# Call the main function.
if __name__ == '__main__':
    main()
