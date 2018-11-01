Feature: Exemplo JWT

  Scenario: Gerar um JWT e adicionar aos Headers
    Given I generate a milliseconds date "iat" with "0" minutes
    Given I generate a milliseconds date "exp" with "15" minutes
    Given I use the json and generate a JWT Token
        """
        {
        "jti": "9e74d1f6-7095-4718-8f11-47dc9ec99c63", 
        "iat": ${iat},
        "scope": [
          "read",
          "write"
        ],
"user_id": "5bbf64322fbf95000868adc2",
  "client_id": "5b391f6e02e9c10009af8592",
  "app_id": "5b391ec6f18f4f00082d59b1",
  "business_id": "5bbf64322fbf95000868adc1",
  "service_id": "5b391f6df18f4f00082d59b3",
  "authorities": [
    "ROLE_BUSINESSADMIN",
    "ROLE_CLI-AUTH-IDENTIFIED",
    "ROLE_CLI-1STPARTY",
    "ROLE_USER",
    "ROLE_CLI-3RDPARTY",
    "ROLE_BUSINESSUSER",
    "ROLE_ADMIN",
    "ROLE_AUTH-IDENTIFIED"
  ],
        "exp": ${exp}
      }
        """
    Given I set the Bearer Authorization header
    Then I print the path

	