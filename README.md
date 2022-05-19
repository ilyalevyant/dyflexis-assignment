# Picnic Recruitment Task #

This assignment was created specifically for our SDET recruitment process.
You were given a link to GitHub, which when you visited that link, created a private fork
of this repository. Only you and the developers at Picnic can see the code you push to this
repository. If you did not receive a link, please contact us. Please read the following
instructions carefully and try to ensure that you fulfill all requirements listed.

## Task ##

We would like you to implement a test automation solution for GitHub Gists API:

* [Creating a Gist][gists-create]
* [Reading a Gist][gists-read]
* [Updating a Gist][gists-update]
* [Deleting a Gist][gists-delete]
* [Listing Gists for a user][gists-user]

While you do this, please follow the technical requirements listed below.

**A note before you start**

Familiarize yourself with official GitHub documentation as a single source of functional
requirements for API behavior. We expect you to test both **authorized and unauthorized**
scenarios where applicable.

## Technical Requirements ##

1. Programming language (choose one):
    * Python
    * Java
2. Test approach (choose one):
    * BDD (Gherkin-based) testing frameworks
    * Traditional xUnit test code style
3. Framework requirements:
    * Marshalling / unmarshalling of requests and responses (object representation)
    * Cleanup of the test data
4. Project instructions should specify:
    * Overview of the language/framework used
    * How to set up dependencies and environment for the project
    * How to execute the tests from command line

## How to hand in your assignment ##

1. Make a local clone of this repository on your machine. Once you've cloned the repository, create
   your own branch and commit any changes there. Do not make any changes to the `main` branch.
2. Push your changes as frequently as you like to `origin/your-branch-name`,
   and create a pull request to merge your changes back into the `main`
   branch. Don't merge your pull request. Once you're finished with the
   assignment, we will do a code review of your pull request.
3. When you're finished, [create and add][github-labels] the label `done` to
   your pull request and let your contact person know. Please do **NOT** publish your solution 
   on a publicly available location (such as a public GitHub repository, your personal website,
   _et cetera_).

This process closely mimics our actual development and review cycle. We hope you enjoy it!

## Resources ##

* Gists API Documentation: [GitHub Gists][github-gists]
* For [authorization][github-oauth2] you can [generate][github-tokens] Personal OAuth token with `gists` scope

## Grading Criteria ##

You will be assessed on the following criteria:

* Project structure and approach
* Code readability and style
* Ease of tests setup and execution
* Self-documentation of the tests
* Logical reasoning behind test scenarios

_Thanks in advance for your time and interest in Picnic!_

[github-labels]: https://help.github.com/articles/about-labels
[github-gists]: https://developer.github.com/v3/gists/
[github-tokens]: https://github.blog/2013-05-16-personal-api-tokens/
[github-oauth2]: https://developer.github.com/v3/#oauth2-token-sent-in-a-header
[gists-user]: https://developer.github.com/v3/gists/#list-gists-for-a-user
[gists-read]: https://developer.github.com/v3/gists/#get-a-gist
[gists-create]: https://developer.github.com/v3/gists/#create-a-gist
[gists-update]: https://developer.github.com/v3/gists/#update-a-gist
[gists-delete]: https://developer.github.com/v3/gists/#delete-a-gist
