# Local Development Setup

## Setup GitHub CodeSpaces to do local development
- Without the hassle of local setup, you can get a devlopment environment interacting with your repository.
- Read more about CodeSpaces [here](https://github.com/codespaces)
- 1 min tutorial to get setup see this [video](https://youtu.be/_W9B7qc9lVc)
- Note - As of Jan 2023 I read there is 15GB and 120 Core Hours of Free Use per month on personal account. Please review [here](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts)
- If you have a day job and can only spend daily 30 mins on weekdays and 4 to 5 hours per weekend, the hours cover more than enough for self learning pace.(It will be less than 50 hours per month of use, hence the conclusion.)

## GitHub Basics

Learn more about Git Basics [here](https://github.com/education/github-starter-course)

Configure Git:
- Set the name: `git config --global user.name "Your Name"`
- Set the email: `git config --global user.email "youremail@example.com"`

The following commands are your daily bread and butter, if you are using CLI

1. `git status -s` To check the latest status of your local repository compared to the destination
2. `git add TBD_FILE_NAME` adds a specific file to the staging area, replace TBD_FILE_NAME with the name of the file.
3. `git commit -m "my changes"` Always be in a habit to provide good commit messages, any body can write code, always write more to serve the reader later on. You save time for others being thoughtful about your code commit comments.
4. `git add -all` Adds all the files to the staging area, that have uncommitted changes.
5. `git commit -am "commit message"` combines the add to staging area and commit with the commit message.
6. `git push origin master` or `git push origin main` push the committed changes to the main or master branch. 


## Add GitHub CoPilot Extension

<img width="884" alt="image" src="https://github.com/AMNEngineering/amn-internship-python/assets/29447019/182bacec-ac24-4d73-a77a-ec29dbf39a36">

## Postman
1. Go to [Download Postman](https://www.postman.com/downloads/) and get the latest postman tool.
2. Create an account in postman, I created one using my gmail account. This helps create your own workspace and fork interesting Postman Collection to work in your workspace.
3. [Public REST APIs](https://www.postman.com/cs-demo/workspace/public-rest-apis/collection/8854915-454a2dc7-dcbe-41cf-9bfa-da544fcd93a2) Is a colleciton of random publicly available REST APIs, which you can play with in your postman tool and study the underlying HTTP request/response.
4. The best tool for debugging APIs in general, is to call it using API Exploration tool like Postman and play with query parameters and study the HTTP Response in real-time to debug pressing issues. 
5. Most likely, the REST APIs you would be using is secured by an API Token, understand the authorization mechanism for the REST API you will be working for before tinkering around with the API in Postman.

## ChatGPT
1. Create an account in ChatGPT if you have not go to [here](https://platform.openai.com/signup?launch)
2. Take this course to learn [effective prompt engineering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/), before embarking on partnering with ChatGPT.
3. The course teaches you how to give clear and specific instructions to ChatGPT to get your help better and faster.
- Principle 1: Write clear and specific instructions
- Principle 2: Give the model time to “think”
4. You own the output of your own work, even if you got assistance from ChatGPT. So its essential to verify the output of ChatGPT, to ensure the outcome you originally desired is actually present. Don't blame ChatGPT for the mistake, own your own accountability in conciously using ChatGPT to assist you to be more productive. So use the tool like ChatGPT to aid your productivity, but own the accountability of the outcome it creates. (Extreme Ownership!)
5. Lastly, if you are curious and tenacious, ChatGPT is a unending source of information, that never gets tired, so keep your curiosity and hunger of experimentation high!

Lets get started!!

