# Created by C L at 11/04/2020
Feature: burnup
  A burnup is a diagram predicting future by looking at past performances

  Scenario Outline: Get average of 3 lowest numbers for worst case forecast
    Given i have a "<list>"  of numbers
    Then the lowest average is "<result>"

    Examples:
      | list     | result |
      | 3,5,10,6 | 4.67   |
      | 3,4      | 3.5    |

  Scenario Outline: If i have a long history of sprint, we should only take the 6 most recent one
    Given i have a "<list>"  of numbers
    And i have more than 6 numbers
    Then the lowest average is "<low_result>"
    And the highest average is "<high_result>"
    And the average is "<result>"

    Examples:
      | list                  | low_result | high_result | result |
      | 3,34,21,7, 42,9,13,21 | 9.67       | 28          | 18.83  |

  Scenario Outline: Get average of 3 highest numbers for best case forecast
    Given i have a "<list>"  of numbers
    Then the highest average is "<result>"

    Examples:
      | list     | result |
      | 3,5,10,6 | 7      |
      | 3,4      | 3.5    |

  Scenario: Calculate best forecast for the next 6 iterations using the 3 best iterations
    Given i have a list of past sprint velocity
    Then i can give a best case forecast for the next 6 iterations based on the best 3 iterations over the last 6 iterations

  Scenario: Calculate worst forecast for the next 6 iterations using the 3 worst iterations
    Given i have a list of past sprint velocity
    Then i can give a worst case forecast for the next 6 iterations based on the worst 3 iterations over the last 6 iterations

  Scenario: Calculate average forecast for the next 6 iterations
    Given i have a list of past sprint velocity
    Then i can give an average case forecast for the next 6 iterations based on at most the last 6 iterations

  Scenario: Calculate real progress
    Given i have a list of past sprint velocity
    Then i must get the real progress by incrementing each week with the sum of previous weeks

  Scenario: Calculate best forecast for the next 6 iterations using standard deviation
    Given i have a list of past sprint velocity
    Then i can give a best case forecast for the next 6 iterations based on the standard deviation on the last 6 iterations

  Scenario: Calculate worst forecast for the next 6 iterations using the 3 worst iterations
    Given i have a list of past sprint velocity
    Then i can give a worst case forecast for the next 6 iterations based on the the standard deviation on  the last 6 iterations

