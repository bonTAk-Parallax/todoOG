ToDo App 

Built a todo app using Django for basic learning purposes. The app has an user registration, authentication/authorization and guest user system. Along with basic CRUD functionality for both the tasks todo and users at hand. Learned GIT and GitHub along the way as well. The project will have multiple other functionalities and apps in the future like user groups, group specific tasks and real time chat among user. This is all in the future though, now I be documenting every minute detail/s and steps required for it's creation. Wish me luck. (OS used: Linux Mint)


Django setup:

    • Create a folder and open it in Vs-code
      Go to the terminal 
      
    • Create a virtual environment:
      python3 venv -m .venv
      
    • Activate the virtual environment:
      source .venv/bin/activate


Why? To isolate the project from other Django projects/dependencies to avoid clash between the packages. Some project might require different packages, old version of Django and it's global installation might affect other ones that prefer the latest version. That is just one basic reason I mentioned, to have an in-depth knowledge regarding it, refer to https://dev.to/sarahhudaib/why-virtualenv-is-important-for-django-development-58fp .


    • Django installation inside the venv:
      python3 pip -m install Django
      
    • PIP update:
      python3 pip -m install -U pip
      
    • Setting up the project:
      python3 django-admin todo_list
      
    • Adding an app inside the project:
      python3 django-admin base

Note: An project may have various apps for multiple use cases. Lets take Facebook as an example, this project might have apps like real_time chat app, short/reels app, etc.



Using GIT, the easy way:

Pre-requisite: Have a GitHub account and GIT installed.

    • Go to source control in vs-code and initialize the repository.
    • Make a .gitignore file and put venv/ or other unwanted code that don’t need to be pushed to git.
    • Preferably, paste all the raw files from python.gitignore repository in GitHub since just .gitignore does not cover all the files.
    • Now all the git functions can be used from source control using GUI.

To use GIT from CLI:

    • Check the current status of files     :  	git status
    • Add the files to be tracked:          :       git add –all
    • Commit the changes                    :  	git commit -m “__msg__”
    • Push the changes to repository        :  	Make a repository in GitHub, copy the 'git remote add origin.....' cmd and paste it in CLI of vs-code
                                                    Link your GitHub account to VS-code 
                                                    Run cmd:  git push origin main
    • Add, commit and push/publish again as you make new changes along the way.

Note: Might need to identify yourself, just use 
( git config --global user.email "you@example.com" ) and 
( git config --global user.name "Your Name" )
