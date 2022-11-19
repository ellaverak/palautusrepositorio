*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ulla  ulla1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kissa123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  gg  kissa123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  ulla  ulla
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ulla  ullaulla
    Output Should Contain  Invalid password

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
