# Github Commands and Conventions

### 1. Initiate project and push on GitHub

#### Open a folder in VS Code and write the below command

Clone your project to local pc:

```bash
git clone project_url

```

### Select all of the changes to deploy
Deploy all changed files:

```bash
git add .
# OR
git add --all
```
Deploy specific files:
```bash
git add path/to/file1 path/to/file2 path/to/file3
```
```bash
git commit -m 'first commit'
git push
```

### 2. Before deploying any work follow this
Deploy locally changed files in your branch if it’s necessary so that while syncing with base branches can not overwork your own necessary work.

```bash
git fetch
git merge base_branch
# Resolve conflicts if any
# Deploy your work accordingly
git add .
git commit -m 'commit message'
git push

```

### 3. Some important git commands
Display the state of the working directory and the staging area:

```bash
git status
```

Display committed snapshots:

```bash
git log

```
Navigate between already created branches:

```bash
git checkout branch_name
```
Create a new branch:

```bash
git checkout -b new_branch_name
```
To check all the branch list:

```bash
git branch
```
Show the difference between current branch to base Branch:

```bash
git diff
```
Retrieves the latest changes from the remote repository but doesn't integrate them into your local branch:

```bash
git fetch
```
Combines the changes fetched from the remote repository into your current branch:

```bash
git merge "origin/branch-name"
```

When you're working on a project and other team members have pushed changes to the remote repository:

```bash
git pull
```

### 4. Github Branch create Conventions
If there is no branch except main branch, then create a subbranch under the main branch from GitHub so that all the development-based work will be pushed to main branch, when there is no error in the work and all the work will be push to main branch by the team lead or admin.

### Try to follow the convention for branching:

#### To create branch for developing features branch name will be:

```bash
feature/branch-name
```

If there is any bug which needs to be fixed, the branch name will be:
```bash
fix/branch-name
```
If you want to create a branch to write a document, the branch name will be:

```bash
doc/branch-name
```

If you want to create a branch for setup configuration related things, the branch name will be:
```bash
config/branch-name
```
### 5. Github Branch rules
     - Name should be separated by dash
     - Multiple PR can not be created from one branch
     - Always sync your branch with your base branch
### 6. PR Rules
After pushing the work in GitHub, you need to create PR to review your work Without getting one approval from your team members, you cannot merge your PR with your base branch Send a PR request to team members to review PR. 

- After merging PR, delete the branch Please assign yourself in assignee option. 

- Don’t provide too long. PR for review (Max 15 file changes)
- PR Title Conventions

- If the PR is in need to review urgent, try to give PR title:

```bash
[URGENT] PR Title
```

- If the PR is not in need to review urgently try to give PR 

```bash
[NORMAL] PR Title
```

- If the PR is not complete but you need some suggestion to your work PR title:

```bash
[WIP] PR Title
```

## PR Description Template
```bash
The PR contains:

List of content the PR contains with bullet point
Deployment: Deployment date / NA
Test case: How many test cases passed/coverage/NA
```
