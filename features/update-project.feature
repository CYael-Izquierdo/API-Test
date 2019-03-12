Feature: Update project

  @Working @delete.new.project
  Scenario: Modify project name by id
    Given a "Update Test" Project with "update-test" identifier
    When I modify the name to "Project updated"
    Then I should see a successful update code and the new name in the project
