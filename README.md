# Lyft Backend Virtual Experience Program

## Introduction

This repository contains the codebase for the Lyft Backend Virtual Experience Program. A Backend Engineer at Lyft collaborates with a cross-functional team consisting of software engineering, product, data science, analytics, and operations to work on Lyft backend projects.

## Technology Used

- Python
- Unit Testing Framework (e.g., `unittest`)
- Test-driven Development (TDD)

## Completed Tasks
Use the tasks list to read the commits in this repository.

### Task 1: System Architecture Refactoring

- **Description:** Designed a clean system architecture to ensure extensibility and easy modification of service criteria.
- **Changes Made:**
  - Introduced a modular architecture to accommodate future changes efficiently.
  - Implemented a class hierarchy for engines and batteries with appropriate attributes and methods.
  - See `UML_diagram.pdf`in this repository for the revised architecture.

### Task 2: Unit Testing

- **Description:** Ensured system correctness through rigorous unit testing.
- **Changes Made:**
  - Created comprehensive unit tests for each engine and battery class.
  - Validated edge cases and expected behavior to guarantee system robustness.

### Task 3: Spindler Battery Upgrade

- **Description:** Modified the Spindler battery service criteria.
- **Changes Made:**
  - Adjusted the code to require service after three years instead of two for Spindler batteries.

### Task 4: Tire Servicing Criteria

- **Description:** Added functionality to account for tire servicing criteria based on wear sensors.
- **Changes Made:**
  - Implemented logic to evaluate tire wear arrays for both Carrigan and Octoprime tires.
  - Integrated tire servicing criteria into the car factory class.

## Instructions for Running the Code

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Navigate to the project directory.
4. Run the desired Python scripts to execute the functionalities.

## Additional Notes

- The system is designed to handle valid inputs. In a real-world scenario, extensive input validation would be implemented.

## Service Criteria and Car Information

### Service Criteria

- **Capulet Engine**
  - Service Interval: Once every 30,000 miles

- **Willoughby Engine**
  - Service Interval: Once every 60,000 miles

- **Sternman Engine**
  - Service Interval: Only when the warning indicator is on

- **Spindler Battery**
  - Service Interval: Once every 2 years

- **Nubbin Battery**
  - Service Interval: Once every 4 years

### Car Models and Engine-Battery Combinations

| Car       | Engine           | Battery           |
|-----------|------------------|------------------|
| Calliope  | Capulet Engine   | Spindler Battery |
| Glissade  | Willoughby Engine| Spindler Battery |
| Palindrome| Sternman Engine  | Spindler Battery |
| Rorschach | Willoughby Engine| Nubbin Battery   |
| Thovex    | Capulet Engine   | Nubbin Battery   |

### Additional Information

- There are five distinct car models within Lyft’s fleet, each equipped with a specific combination of engine and battery type.

- It is important to note that the service criteria for these engines and batteries may undergo changes over time. Additionally, new car models are anticipated to be integrated into the fleet, making adaptability a crucial factor in the program's development.
