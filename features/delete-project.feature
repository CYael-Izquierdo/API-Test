Feature: Delete project

  @Working
  Scenario: Delete project by id

    Given a new project created
    When I delete this project
    Then I should see a successful delete code and I shouldn't be able to find the project