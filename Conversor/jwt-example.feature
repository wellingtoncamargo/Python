Feature: Exemplo JWT

  Scenario: Gerar um JWT e adicionar aos Headers
    Given I generate a milliseconds date "iat" with "99999999" minutes
    Given I generate a milliseconds date "exp" with "9999999" minutes
    Given I use the json and generate a JWT Token
        """
        {
        "jti": "9e74d1f6-7095-4718-8f11-47dc9ec99c63", 
        "iat": ${iat},
        "scope": [
          "read",
          "write"
        ],
  "user_id": "5b4e3a9b9a73770009bedf11",
  "client_id": "5b391f6e02e9c10009af8592",
  "client_id_default": "5b39132402e9c10009af8572",
  "app_id": "5b391ec6f18f4f00082d59b1",
  "business_id": "123",
  "service_id": "5b391f6df18f4f00082d59b3",
  "customer_id": 6721,
  "jti": "7eb82d3f-1fdd-479f-863d-3187fd73865d",
  "iat": 1535640157,
  "authorities": [
    "ROLE_BUSINESSADMIN",
    "ROLE_CLI-AUTH-IDENTIFIED",
    "ROLE_BUSINESS",
    "ROLE_CLI-1STPARTY",
    "ROLE_USER",
    "ROLE_AUTH-BASIC",
    "ROLE_CLI-3RDPARTY",
    "ROLE_PERSON",
    "ROLE_BUSINESSOWNER",
    "ROLE_BUSINESSUSER",
    "ROLE_AUTH-IDENTIFIED"
  ],
        "exp": ${exp}
      }
        """
    Given I set the Bearer Authorization header
    Then I print the path

	