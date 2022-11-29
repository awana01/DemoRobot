*** Settings ***
Suite Setup           
     
  

*** Test Cases ***
Test with templete iteration1 
   [Template]   Run test for ${iteration}
    1
    2
    3
Test multi keywords
  [setup]  Try some keywords
  Hello world
*** Keywords ***
Run test for ${iteration}
  ${result}        Evaluate          type(${iteration})
  Log To Console   ${result}
  Log To Console   iter:${iteration} 

Try some keywords
    Run Keywords
    Log To Console    \nHello py0
    Log To Console    Hello py1
    Log To Console    Hello py2

Hello world
    Log To Console    Hello World