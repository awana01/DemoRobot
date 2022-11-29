*** Settings ***
Library    SeleniumLibrary
Library    ../Keywords/InitBrowser.py

*** Variables ***
${URL}     https://www.google.com/


*** Test Cases ***
Test01 Google Sample Test
    Launch URL
    Enter search data


*** Keywords ***
Launch URL
  ${chrome_options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
  Call Method    ${chrome_options}    add_argument    --no-sandbox
  Call Method    ${chrome_options}    add_argument    --disable-extensions
  Call Method    ${chrome_options}    add_argument    --headless
  Call Method    ${chrome_options}    add_argument    --disable-gpu
#   Create Webdriver    Chrome    chrome_options=${chrome_options}
#   Go To    ${URL}
Enter search data
  @{chrome_options}  Create List    
  open chrome browser      https://www.google.com/
  ...              chrome
  ...              --disable-infobar  --window-size=900,600   --disable-blink-features=AutomationControlled  --disable-extensions
  Click Element    name:q
  Input Text       name:q     Github Actions\n
  Sleep     3s
  ${size_dict}     Get Window Size
  Log To Console   ${size_dict} 
  Set Window Size  width=902    height=800