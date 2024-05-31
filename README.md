# Selenium Testing Program

## What's the purpose?
This program provides me with a platform to not only enhance my skills but also showcase my expertise as a QA automation engineer proficient in Python and Selenium. Employing the Gherkin language, I craft test cases following the principles of Behavior Driven Development. Subsequently, I meticulously code each step, meticulously evaluating the website's functionality from a user-centric perspective. The website being used is: https://www.saucedemo.com/. Designed with a straightforward user interface, it emulates the shopping journey, offering a range of distinct features for testing.

## To run the program
In order to run the program, make sure to have the appropriate tools installed. 

To install use:
```
pip install behave
pip install python
```


To verify you can use:
```
python --version
pip --version
pip show behave
```

From there, you can run in the CLI the following commands:
```
python -m behave
python -m behave features/(feature of your choice).feature
python -m behave --tags=@you_can_tag_specific_scenarios
```