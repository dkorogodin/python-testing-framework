@product
Feature: Product Scenarios
  As a user of the mobile app
  I want to view product information
  So that I can verify product details

  @positive
  Scenario Outline: Validate product info on Products page
    Given I am logged in as "bob@example.com" with password "10203040"
    Then I should see product with title "<title>" and price "<price>"

    Examples:
      | title               | price  |
      | Sauce Labs Backpack | $29.99 |

  @positive
  Scenario Outline: Validate product info on Product Details page
    Given I am logged in as "bob@example.com" with password "10203040"
    When I tap product title "<title>"
    Then I should be on Product Details page with title "<title>"
    And I should see product details with title "<title>", price "<price>" and description "<description>"

    Examples:
      | title               | price  | description                                                                                                                            |
      | Sauce Labs Onesie | $7.99 | Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel. |
