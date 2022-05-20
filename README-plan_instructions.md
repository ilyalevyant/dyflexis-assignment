## Test Plan ##

This is the short overview for created test, separated by given APIs:

Creating a gist:
- create gist with all fields
- create gist only mandatory fields
- try to create gist without token
- try to create gist without mandatory fields

Updating a gist: 
- update all possible fields in gist
- try to update gist without token
- try to update gist by wrong id
 
Delete a gist:
- delete gist by id
- try to delete gist without token
- delete gist by invalid id

Get gists:
- get gists by user
- try to get gists by invalid user
- get gists by user with 'page' parameter
- get gists by user with 'per page' parameter
- try to get gists by user with invalid date (future date) parameter

**All APIs who do not require authorization was tested without token.**


## How to start ##

Run command in the terminal: `bash run.sh`

This command will automatically execute the next commands:
1. Install all dependencies
2. Run most of tests in parallel (to reduce runtime)
3. Run one specific test separately, because it depends on DB data (data should not be changed during test run). 

If this project is opened in PyCharm, it can be run manually by right-click on `test_gists.py` -> Run 'pytest in...'
## Short design overview ##

This design-pattern we are calling Service Object model.
The main goal of it to separate test logic, test data and service requests.
Each test builds like this:
1. Generate necessary data with `data factory` class: for request, for expected response, for actual response.
2. Do some action with service: for each action we have method in `test helper` class. Method takes some data for test and requesting service with this data. All additional info (like endpoint url) it takes from `config` file. This user-logic method is calling service request method from class `gists_service_api`. It has method for each supported method in our back-end service. And each method calls according method in `services_api` class to make request itself. This is the most lower level in our framework where we can modify our request according to needs(add default headers, use framework `requests` to send request, etc.). 
3. Validate result: 
    - validate status code is equals to expected.
    - validate response body or error message.

Most popular actions, like `create gist` is placed in a separated methods (fixtures). After test run fixture is deleting specific gist.
