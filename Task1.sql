SELECT d.NAME AS DEPT_NAME, AVG(s.AMT) AS AVG_MONTHLY_SALARY -- Select department name and average salary
FROM Departments d
JOIN Employees e ON d.ID = e.DEPT_ID -- Join Departments table with Employees table based on department ID
JOIN Salaries s ON e.ID = s.EMP_ID -- Join resulting table with Salaries table based on employee ID
GROUP BY d.NAME -- Group the results by department name
ORDER BY AVG_MONTHLY_SALARY DESC -- Sort the departments in descending order of average salary
LIMIT 3; -- Retrieve only the top 3 departments
