# Gherkin file created at 4/03/16

Feature: Create a bridge - add-br

  Scenario: Create a bridge and its port and interface

    Given a name for the bridge
    When a bridge is created
    Then the bridge is created and its port and interface