
% Write Prolog program to perform the following operations on lists. Use recursion wherever applicable: length of list, sum of elements,
% membership check, check if list is sorted, append & concatenate.

% Length of list
list_length([], 0).
list_length([_|T], N) :-
    list_length(T, N1),
    N is N1 + 1.

% Sum of elements
list_sum([], 0).
list_sum([H|T], Sum) :-
    list_sum(T, S1),
    Sum is H + S1.

% Membership
my_member(X, [X|_]).
my_member(X, [_|T]) :-
    my_member(X, T).

% Check sorted list
sorted([]).
sorted([_]).
sorted([A, B|T]) :-
    A =< B,
    sorted([B|T]).

% Append
my_append([], L, L).
my_append([H|T], L, [H|R]) :-
    my_append(T, L, R).


% queries

% ?- list_length([1,2,3], N).
% ?- list_sum([1,2,3], S).
% ?- my_member(2, [1,2,3]).
% ?- sorted([1,2,3]).
% ?- my_append([1,2], [3,4], X).