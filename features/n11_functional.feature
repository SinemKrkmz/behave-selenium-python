Feature: N11_Functional



  Scenario: TestCases
    Given got web site "https://www.n11.com"
    When get page title
    Then title is shown "n11.com - Alışverişin Uğurlu Adresi"
    And I click link Giriş Yap
    And I enter  email
    And I enter valid password
    And I click button Üye Girişi
    And I enter search text "Samsung"
    And I click button Search
    Then "Samsung" search is shown
    And I click page button "2"
    Then Second page is shown "Samsung - n11.com - 2"
    And Add "3" product to favorites
    And I click link favorites
    And I click favorites product
    Then shown favorites product
    And delete favorites product
    And I click delete tamam button
    Then product deleted "İzlediğiniz bir ürün bulunmamaktadır."
