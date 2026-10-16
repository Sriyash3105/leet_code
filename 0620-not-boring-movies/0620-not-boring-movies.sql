# Write your MySQL query statement below
SELECT * FROM Cinema
    WHERE (MOD(Cinema.id,2) = 1) AND Cinema.description NOT LIKE 'boring'
    ORDER BY Cinema.rating DESC;