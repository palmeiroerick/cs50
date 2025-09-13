-- drop index search_enrollments_by_course_id;
-- drop index search_enrollments_by_student_id;
-- drop index search_courses_by_semester;
-- drop index search_satisfies_by_course_id;

-- vacuum;

create index search_enrollments_by_course_id on "enrollments" (course_id);
create index search_enrollments_by_student_id on "enrollments" (student_id);
create index search_courses_by_semester on "courses" (semester);
create index search_satisfies_by_course_id on "satisfies" (course_id);
