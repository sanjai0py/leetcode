-- # Write your MySQL query statement below
select stu.student_id, stu.student_name, sub.subject_name, COUNT(exm.student_id) AS attended_exams
from students stu
cross join subjects sub
left join examinations exm
    on stu.student_id = exm.student_id
        and sub.subject_name = exm.subject_name
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, sub.subject_name; 

