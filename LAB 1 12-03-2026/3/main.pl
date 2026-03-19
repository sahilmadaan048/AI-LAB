student(student1, 8.5, 250000, sc).
student(student2, 7.2, 200000, general).
student(student3, 9.1, 500000, obc).
student(student4, 8.0, 350000, st).

merit_eligible(Name) :-
    student(Name, CGPA, _, _),
    CGPA >= 8.0.

income_eligible(Name) :-
    student(Name, _, Income, _),
    Income =< 300000.

reserved_category(Name) :-
    student(Name, _, _, Cat),
    member(Cat, [sc, st, obc]).