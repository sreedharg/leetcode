/* Write your T-SQL query statement below */
select a.name as Employee
from Employee a join Employee b on a.managerid = b.id
and a.salary > b.salary