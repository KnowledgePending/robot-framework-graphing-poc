*** Settings ***
Library  graph.py
*** Keywords ***
Create a System Usage Graph
    ${SYSTEM_USAGE_GRAPH} =  Generate System Usage Chart
    Log  ${SYSTEM_USAGE_GRAPH}  html=True

*** Test Cases ***
Graphing System usage over time
    [Documentation]  This embeds a pygal graph within the robotframework log
    Create a System Usage Graph
