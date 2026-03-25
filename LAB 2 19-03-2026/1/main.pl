% Write a program in Prolog that defines a knowledge base representing extended family tree with atleast two generations

% Facts
parent(john, mary).
parent(john, david).
parent(mary, alice).
parent(mary, bob).
parent(david, tom).

male(john).
male(david).
male(bob).
male(tom).

female(mary).
female(alice).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).


% queries
% ?- ancestor(john, alice).
% ?- grandparent(john, bob).
% ?- grandparent(john, mary).