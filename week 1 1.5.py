"""
Header Documentation
-------------------------------------------------------------------------------
Name:    [Your Name]
Date:    August 4, 2026
Purpose: Week 1 Term Project - Demonstrating Inheritance, Composition, 
         and basic Console UI User Interactions for an Employee System.
-------------------------------------------------------------------------------
"""

from abc import ABC, abstractmethod
from typing import List


# =============================================================================
# 1. COMPOSITION CLASSES
# =============================================================================

class ContactInfo:
    """
    Demonstrates COMPOSITION.
    This class holds communication metadata and will be composed INSIDE
    the Employee base class.
    """
    def __init__(self, email: str, phone: str, office_location: str):
        self.email = email
        self.phone = phone
        self.office_location = office_location

    def get_contact_summary(self) -> str:
        return f"{self.email} | Ph: {self.phone} | Office: {self.office_location}"


class Department:
    """
    Demonstrates COMPOSITION.
    Represents an organizational unit embedded within an Employee record.
    """
    def __init__(self, dept_name: str, cost_center: str):
        self.dept_name = dept_name
        self.cost_center = cost_center

    def __str__(self) -> str:
        return f"{self.dept_name} (CC-{self.cost_center})"


# =============================================================================
# 2. INHERITANCE: BASE CLASS
# =============================================================================

class Employee(ABC):
    """
    Demonstrates INHERITANCE (Base / Parent Abstract Class).
    Incorporates COMPOSITION by containing instance objects of ContactInfo 
    and Department.
    """
    def __init__(self, emp_id: str, name: str, dept_name: str, cost_center: str, email: str, phone: str, office: str):
        self.emp_id = emp_id
        self.name = name
        
        # DEMONSTRATING COMPOSITION: Department & ContactInfo objects composed in Employee
        self.department = Department(dept_name, cost_center)
        self.contact_info = ContactInfo(email, phone, office)

    @abstractmethod
    def calculate_pay(self) -> float:
        """Abstract method to be overridden by derived classes."""
        pass

    @abstractmethod
    def get_pay_details(self) -> str:
        """Returns string representation of pay structure."""
        pass

    def display_row(self) -> str:
        """Formats employee details for tabular display."""
        return (f"{self.emp_id:<6} | {self.name:<18} | {self.department.dept_name:<12} | "
                f"{self.get_pay_details():<22} | {self.contact_info.email}")


# =============================================================================
# 3. INHERITANCE: DERIVED / CHILD CLASSES
# =============================================================================

class SalariedEmployee(Employee):
    """
    Demonstrates INHERITANCE (Derived / Child Class #1).
    Inherits from base class Employee and overrides pay calculation logic.
    """
    def __init__(self, emp_id: str, name: str, dept_name: str, cost_center: str, 
                 email: str, phone: str, office: str, annual_salary: float):
        super().__init__(emp_id, name, dept_name, cost_center, email, phone, office)
        self.annual_salary = annual_salary

    def calculate_pay(self) -> float:
        # Bi-weekly pay calculation
        return round(self.annual_salary / 26, 2)

    def get_pay_details(self) -> str:
        return f"${self.annual_salary:,.2f}/yr (Salaried)"


class HourlyEmployee(Employee):
    """
    Demonstrates INHERITANCE (Derived / Child Class #2).
    Inherits from base class Employee and adds hourly-specific attributes.
    """
    def __init__(self, emp_id: str, name: str, dept_name: str, cost_center: str, 
                 email: str, phone: str, office: str, hourly_rate: float, hours_worked: float):
        super().__init__(emp_id, name, dept_name, cost_center, email, phone, office)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self) -> float:
        # Standard pay + overtime calculation (> 40 hrs)
        if self.hours_worked <= 40:
            return round(self.hourly_rate * self.hours_worked, 2)
        else:
            overtime_hours = self.hours_worked - 40
            return round((40 * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5), 2)

    def get_pay_details(self) -> str:
        return f"${self.hourly_rate:.2f}/hr ({self.hours_worked} hrs)"


# =============================================================================
# 4. USER INTERACTION & MANAGEMENT SYSTEM
# =============================================================================

class EmployeeManagementSystem:
    """Manages system state, sample instantiation, and UI interaction loop."""
    
    def __init__(self):
        self.employees: List[Employee] = []
        self._seed_sample_data()

    def _seed_sample_data(self):
        """Instantiates classes with realistic sample information."""
        emp1 = SalariedEmployee(
            emp_id="E101",
            name="Sarah Connor",
            dept_name="Engineering",
            cost_center="101",
            email="s.connor@corp.com",
            phone="555-0192",
            office="Bldg A - 302",
            annual_salary=95000.00
        )
        emp2 = HourlyEmployee(
            emp_id="E102",
            name="Marcus Wright",
            dept_name="Operations",
            cost_center="204",
            email="m.wright@corp.com",
            phone="555-0144",
            office="Bldg B - 105",
            hourly_rate=35.50,
            hours_worked=45.0
        )
        emp3 = SalariedEmployee(
            emp_id="E103",
            name="Ellen Ripley",
            dept_name="Security",
            cost_center="901",
            email="e.ripley@corp.com",
            phone="555-0881",
            office="Bldg C - 101",
            annual_salary=110000.00
        )
        self.employees.extend([emp1, emp2, emp3])

    def display_header(self):
        print("=" * 85)
        print("  COURSE PROJECT WEEK 1: INHERITANCE & COMPOSITION DEMO")
        print("  Assignment: User Interactions & OOP Class Architecture")
        print("  Student Name: [Your Name]")
        print("=" * 85)
        print("\nWELCOME to the Employee Management System!")
        print("Use the menu options below to view records and interact with the system.\n")

    def display_menu(self):
        print("-" * 35 + " MAIN MENU " + "-" * 35)
        print("1. Display Brief Employee List")
        print("2. Display Detailed Roster (Tabular View with Composition & Inheritance Data)")
        print("3. Add New Employee (Simulated Action)")
        print("4. Delete Employee (Simulated Action)")
        print("5. Exit System")
        print("-" * 81)

    def display_brief_list(self):
        print("\n--- BRIEF EMPLOYEE LIST ---")
        for emp in self.employees:
            print(f" • [{emp.emp_id}] {emp.name} - Dept: {emp.department.dept_name}")
        print()

    def display_detailed_roster(self):
        print("\n--- DETAILED EMPLOYEE ROSTER ---")
        print(f"{'ID':<6} | {'Name':<18} | {'Department':<12} | {'Pay Details':<22} | Contact Email")
        print("-" * 85)
        for emp in self.employees:
            print(emp.display_row())
        print("-" * 85)
        print()

    def run(self):
        self.display_header()
        while True:
            self.display_menu()
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                self.display_brief_list()
            elif choice == "2":
                self.display_detailed_roster()
            elif choice == "3":
                print("\n[INFO] 'Add Employee' feature queued for Week 2 implementation.\n")
            elif choice == "4":
                print("\n[INFO] 'Delete Employee' feature queued for Week 2 implementation.\n")
            elif choice == "5" or choice.lower() == "exit":
                print("\nThank you for evaluating Phase 1. Exiting application...\n")
                break
            else:
                print("\n[ERROR] Invalid choice. Please enter a number between 1 and 5.\n")


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    app = EmployeeManagementSystem()
    app.run()