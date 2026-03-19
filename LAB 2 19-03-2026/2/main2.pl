# not working

# % Write a program in Prolog to develop an interactive consultation system that diagnoses common diseases based on symptoms entered
# % by the user.

# symptom(john, fever).
# symptom(john, cough).
# symptom(john, headache).

# symptom(mary, sneezing).
# symptom(mary, runny_nose).
# symptom(mary, fever).

# diagnosis(Patient, flu) :-
#     symptom(Patient, fever),
#     symptom(Patient, cough),
#     symptom(Patient, headache).

# diagnosis(Patient, cold) :-
#     symptom(Patient, sneezing),
#     symptom(Patient, runny_nose).

# diagnosis(Patient, allergy) :-
#     symptom(Patient, sneezing),
#     symptom(Patient, fever).

# start :-
#     write('Enter symptom: '), read(Symptom),
#     diagnose(Symptom).

# diagnose(fever) :-
#     write('You may have Flu'), nl.

# diagnose(cough) :-
#     write('You may have Cold'), nl.

# diagnose(headache) :-
#     write('Take rest and stay hydrated'), nl.

# diagnose(_) :-
#     write('Unknown symptom'), nl.


# % queries
# % ?- start.