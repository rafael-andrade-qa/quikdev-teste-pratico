# Technical Evaluation - Screen 1

## Question 1: Test Scenario and Screen Evaluation

**Screen Description:**
- Form with fields for "Product Name," "Price," and "Expiration Date."
- "Add" button.
- Table to display added products.

**Test Scenario:**

| Test Scenario          | Action                                                      | Expected Result                                   | Observed Behavior                      |
|------------------------|-------------------------------------------------------------|---------------------------------------------------|----------------------------------------|
| Empty Name             | Leave "Product Name" field empty and attempt to add         | Product should not be added. No error message expected. | No validation for empty fields.        |
| Empty Price            | Leave "Price" field empty and attempt to add                | Product should not be added. No error message expected. | No validation for empty fields.        |
| Empty Expiration Date  | Leave "Expiration Date" field empty and attempt to add      | Product should not be added. No error message expected. | No validation for empty fields.        |
| Negative Price         | Enter a negative value in the "Price" field and attempt to add | Product should not be added. No validation for negative price. | Negative price is accepted.           |
| Expiration after 31/12/2021 | Enter an expiration date after 31/12/2021                    | Product should be added. No validation for expiration date. | Expiration date after 31/12/2021 is accepted. |

**Observed Behavior:**
- No validation for empty fields.
- Negative price is accepted.
- Expiration date after 31/12/2021 is accepted.

## Question 2: Test Automation

To automate the testing process for the described functionality, we will use Python and Selenium along with Behave (Cucumber for Python), Gherkin, and the Behavior-Driven Development (BDD) approach.

### Tools and Techniques

**UI Test Automation Tools:**

- **Selenium:** To simulate user actions such as clicking buttons, filling out forms, and navigating between pages.
- **Behave:** A BDD framework for Python that uses Gherkin to write human-readable test specifications.
- **Gherkin:** A simple language for describing test scenarios in a readable syntax.

**Automation Techniques:**

- **Functional Testing:** Ensure that the application functionality works as expected.
- **Field Validation:** Verify that validations for input fields (name, price, expiration date) are functioning correctly.
- **Regression Testing:** Ensure that new changes or bug fixes do not introduce new issues.

