# all commands of git and github

* git is version control system( traks changes in codes)
* github is a website we host repositorires online

# git configuring
=> git config --global user.name "name"             //adds name in our local environment
=> git config --global user.email "email"            //adds email in our local environment
=> git config --list                                            // for verfication of git configs

# basic commands
1. clone : clones a repo into our local system
=> git clone <-link->
2. status : to check the status of git
=> git status
3.add: this adds untracked files 
=> git add <-file name->                          // for one file
=> git add .                                             // for adding add untracked files at once
4.commit : commits the changes in the files
=> git commit -m "some message"
5.push : pushes to online repo
=> git push origin main
6. pull : to get the newly added files from the github repo to our local environment
=> git pull                                  

# INIT COMMAND : with below commands we can create a new repo in local system and can push it to github
=> git init                                                       // for creating a new repo in local system
=> git remote add origin <-link->                    // adds the github repo
=> git remote -v                                               // for verification of remote
=> git push origin main                                 // pushes the code to remote git hub repo

# BRANCHES IN GITHUB : 
=> git branch
=> git branch -M main                                          // to remame a branch
=> git checkout <-branch name->                          // to move to one branch to another
=> git checkout -b 'feature'                             // adds a new branch named feature
=> git branch -d 'test'                                    // deletes the test branch
=> git push --set-upstream origin feature        // adds the feature branch to github repo

# MERGING CODE :
=> git diff <-branch name->            // to check the changes
=> git merge <-branch  name->
by create a PR(pull request) in the github
=> git pull origin main                                 // to get new changed files from the github to our local system
=> git merge feature          // merges the main branch with feature branch

# FIXING MISTAKES
1. if added
=> git reset <-file name->      // resets only one file
=> git reset .                          // resets all newly added files
2. if commited
=> git reset HEAD~1                                  // restores to latest commit
=> git log                                              // for seeing all the commit's hash values
=> git reset <-commit hash->                // restores upto that commit hash
=> git reset --hard <-commit hash->        // completely resets the code up to that commit