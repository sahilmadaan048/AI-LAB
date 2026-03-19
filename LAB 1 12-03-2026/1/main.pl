symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(mary, sneezing).
symptom(mary, runny_nose).
symptom(mary, fever).

diagnosis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, headache).

diagnosis(Patient, cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

diagnosis(Patient, allergy) :-
    symptom(Patient, sneezing),
    symptom(Patient, fever).