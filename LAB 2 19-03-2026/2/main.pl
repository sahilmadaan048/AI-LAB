% ask user for symptoms
start :-
    write('Do you have fever? (yes/no): '), read(F1),
    write('Do you have cough? (yes/no): '), read(F2),
    write('Do you have headache? (yes/no): '), read(F3),
    write('Do you have sneezing? (yes/no): '), read(F4),
    write('Do you have runny_nose? (yes/no): '), read(F5),
    diagnose(F1, F2, F3, F4, F5).

% rules
diagnose(yes, yes, yes, _, _) :-
    write('You may have Flu'), nl.

diagnose(_, _, _, yes, yes) :-
    write('You may have Cold'), nl.

diagnose(yes, _, _, yes, _) :-
    write('You may have Allergy'), nl.

diagnose(_, _, _, _, _) :-
    write('Unable to diagnose properly'), nl.


% ?- consult('main.pl').
% ?- start.


% Do you have fever? (yes/no): yes.
% Do you have cough? (yes/no): yes.
% Do you have headache? (yes/no): yes.
% Do you have sneezing? (yes/no): no.
% Do you have runny_nose? (yes/no): no.

%You may have Flu