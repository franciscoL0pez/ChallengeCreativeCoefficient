# Creative Coefficient challenge

## Ejer 001
```bash
The design team has submitted designs for the login screens.
The PM needs to create a ticket to implement this screen and
asked for your help in specifying the requirements and assumptions for the following design:
```

Requirements:
- The system allows user to enter email and password
- The system validates the email and password in the database or an authentication service
- The system alert users if the credentials are not valid
- The system include captcha
- The system must be validate if captcha is solved correctly
- The system must have a way to recover passwords (Forgot your password?)
- The "Remember me" option must persist user session data if enabled
- The system encrypt the credentials
  

Assumptions:
- Email must be registered 
- The user knows how to solve captcha
- The email must be exist in the authentication system
- Users will not be able to proceed if required fields are incomplete


## Ejer 4

```bash
Write a query to find the top 3 most profitable drugs sold, and how much profit they made.
Assume that there are no ties in the profits.
Display the result from the highest to the lowest total profit.
```
Query:
- SELECT drug, (total_sales - cogs) AS total_profit FROM pharmacy_sales ORDER BY total_profit DESC LIMIT 3;
I create table and insert some data to test query: https://sandboxsql.com/b36e3629-a7e3-4961-891f-43663a2930fa

