# python_behave_template
Selenium webdriver , python , behave

#### INSTALLATION

1. Install a virtual environment
    ```sh
    $ virtualenv -p python3.5 env
    ```

2. Install all packages in the `requirements.text` file.
    ```sh
    $ env/bin/pip install -r requirements.text


# Website
This repository is part of all tutorials on [ Selenium Framework ](http://www.seleniumframework.com)
 

# Usage  
1. If you do not know how to use git, click "Download zip" option at right corner  
2. For Git users, git clone  
3. Install Python 2.7 or higher. Follow this [ Install Python ](http://www.seleniumframework.com/python-basic/what-is-python/)  
4. Install behave. Follow this [ Install behave ] (http://www.seleniumframework.com/python-basic/what-is-behave/) 
5. Complete installing Selenium webdriver components **Pending notes**
6. Open a shell/command prompt and from the root folder run "behave features --no-capture"  
7. Run behave with "-v" gives verbose log. For example running headless using phantomjs with -v creates ghostdriver.log  


# Hiptest publish
1. gem install hiptest-publisher
1. hiptest-publisher -c hiptest-publisher.config --only=features
