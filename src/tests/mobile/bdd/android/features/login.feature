@login
Feature: Login Scenarios
  As a user of the mobile app
  I want to log in with my credentials
  So that I can access the Catalog page

  @negative
  Scenario Outline: Login with invalid credentials
    Given I am on Login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I tap login button
    Then I should see error message "<expectedMsg>"

    Examples:
      | username         | password         | expectedMsg                                                 |
      | invalid_username | 10203040         | Provided credentials do not match any user in this service. |
      | bob@example.com  | invalid_password | Provided credentials do not match any user in this service. |

  @positive
  Scenario Outline: Login with valid credentials
    Given I am on Login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I tap login button
    Then I should see Catalog Page with title "<title>"

    Examples:
      | username        | password | title    |
      | bob@example.com | 10203040 | Products |
