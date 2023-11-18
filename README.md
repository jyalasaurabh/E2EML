# Introduction 
This is a demo project for learning and deploying machine learning. 

# Basic Commands 

```powershell
> conda create -p venv python==3.12 -y # creates a enivornment with python version 3.12
> pip install -r requirements.txt # install dependenices and create packages  (deprecated https://github.com/pypa/pip/issues/12330    please use 3.8 python version for this)
# in case above command not working
> python setup.py install # to install setup

> conda activate venv/
# in case above command not working
> conda init # initialize conda

> python app.py # to run web application

> git remote set-url origin https://github.com/jyalasaurabh/E2EML.git #change to github
> git remote set-url origin https://dev.azure.com/StudioOrg/TestProject/_git/E2E_ML #change to devops
```

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)