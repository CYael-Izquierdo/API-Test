Feature: Create new project

  @Working @delete.new.project
  Scenario: Create new project without modules

    When I create a new project without modules
    Then I should see a successful creation code and I should be able to find the created project