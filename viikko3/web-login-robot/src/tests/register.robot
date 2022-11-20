*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  roosa
    Set Password  roosa123
    Set Password confirmation  roosa123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  oi
    Set Password  oioioi123
    Set Password confirmation  oioioi123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  daavid
    Set Password  daavid2
    Set Password confirmation  daavid2
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kerttu
    Set Password  kerttu123
    Set Password confirmation  kerttu1234
    Submit Credentials
    Register Should Fail With Message  Password confirmation failed

Login After Successful Registration
    Successful Registration
    Go to Login Page
    Set Username  petri
    Set Password  petri123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Failed Registration
    Go to Login page
    Set Username  hannu
    Set Password  hannu
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Successful Registration
    Set Username  petri
    Set Password  petri123
    Set Password confirmation  petri123
    Submit Credentials
    Register Should Succeed

Failed Registration
    Set Username  hannu
    Set Password  hannu
    Set Password confirmation  hannu
    Submit Credentials
    Register Should Fail With Message  Invalid password

