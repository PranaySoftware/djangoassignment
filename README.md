# djangoassignment
## Test One:
### Interval Dates
Create a method which returns interval date by the following condition
Give start and end date (both inclusive) in the ‘YYYYMMDD’ format (ex. 20181231 is 31st Dec 2018), output list of dates that satisfy exactly one of the following conditions. The output should be in chronological order. One date per line. Input dates belong between the year 1900 to 2100.
1. The day is the 4th Saturday of the month.
2. The day is Saturday and the date is multiple of 5.
Example:
Input dates
• Start date: 20180728
• End date: 20180927
Output:
• 20180728
• 20180915
• 20180922
Explanation:
20180728 4th Saturday of July (28th July 2018) 20180825 Not in the solution as it satisfies both the conditions. 20180915 The date is multiple of 5 and it is a Saturday. 20180922 4th Saturday of September.
## Test Two:
1. Create Django APP for user registration and login
2. Create a product associated with User.
3. List the products on User login.
Use Django Default user authentication.
Use sql lite