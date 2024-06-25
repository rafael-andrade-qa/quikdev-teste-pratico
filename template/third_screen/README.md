# Technical Evaluation - Screen 3

## Question 1: Test Scenario and Screen Evaluation

**Screen Description:**
- Same as Screen 2, but with additional validations for price and expiration date.

**Test Scenario:**

| Test Scenario              | Action                                                      | Expected Result                                   | Observed Behavior                            |
|----------------------------|-------------------------------------------------------------|---------------------------------------------------|----------------------------------------------|
| Empty Name                 | Leave "Product Name" field empty and attempt to add         | Message "Invalid name". Product not added.        | All validations are working correctly.        |
| Empty Price                | Leave "Price" field empty and attempt to add                | Message "Invalid price". Product not added.       | All validations are working correctly.        |
| Empty Expiration Date      | Leave "Expiration Date" field empty and attempt to add      | Message "Invalid expiration date". Product not added. | All validations are working correctly.        |
| Negative Price             | Enter a negative value in the "Price" field and attempt to add | Message "Invalid price". Product not added.       | All validations are working correctly.        |
| Expiration after 31/12/2021 | Enter an expiration date after 31/12/2021                    | Message "Invalid expiration date". Product not added. | Expiration date after 31/12/2021 is accepted. |

**Observed Behavior:**
- Basic validations for mandatory fields are working.
- All validations for price and expiration date are functioning correctly.
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
