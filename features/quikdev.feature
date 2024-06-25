@web
Feature: System screens testing

  Scenario Outline: Empty fields on screens
    Given I am on '<screen>'
    When I fill in the fields '<product_name>', '<price>' and '<expiry_date>'
    And I try to add
    Then the product should not be added
    And the error message should be displayed in the fields '<product_name>', '<price>' and '<expiry_date>'

    Examples:
      | screen        | product_name | price | expiry_date |
      | first_screen  |              |       |             |
      | second_screen |              |       |             |
      | third_screen  |              |       |             |

  Scenario Outline: Negative price on screens
    Given I am on '<screen>'
    When I fill in the fields '<product_name>', '<price>' and '<expiry_date>'
    And I try to add
    Then the product should not be added
    And the error message should be displayed in the fields '<product_name>', '<price>' and '<expiry_date>'

    Examples:
      | screen         | product_name | price    | expiry_date    |
      | first_screen   | iPhone       | -100     | 29/12/2021     |
      | second_screen  | Samsung      | -50.75   | 30/12/2021     |
      | third_screen   | Pixel        | -200.99  | 31/12/2021     |

  Scenario Outline: Expiry date after 31/12/2021 on screens
    Given I am on '<screen>'
    When I fill in the fields '<product_name>', '<price>' and '<expiry_date>'
    And I try to add
    Then the product should not be added
    And the error message should be displayed in the fields '<product_name>', '<price>' and '<expiry_date>'

    Examples:
      | screen        | product_name | price | expiry_date |
      | first_screen  | iPhone       | 1000  | 01/01/2022  |
      | second_screen | Samsung      | 750   | 01/01/2022  |
      | third_screen  | Pixel        | 500   | 01/01/2022  |
