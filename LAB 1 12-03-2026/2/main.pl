car_faults(car1, engine_wont_start).
car_faults(car1, overheating).

car_faults(car2, coolant_low).
car_faults(car2, whitesmoke).

car_faults(car3, engine_wont_start).
car_faults(car3, overheating).
car_faults(car3, coolant_low).

car_faults(car4, engine_wont_start).
car_faults(car4, fuel_gauge_empty).

troubleshooting(Car, dead_battery) :-
    car_faults(Car, engine_wont_start).

troubleshooting(Car, blown_head_gasket) :-
    car_faults(Car, overheating),
    car_faults(Car, coolant_low),
    car_faults(Car, whitesmoke).

troubleshooting(Car, radiator_leak) :-
    car_faults(Car, overheating),
    car_faults(Car, coolant_low).

troubleshooting(Car, no_fuel) :-
    car_faults(Car, engine_wont_start),
    car_faults(Car, fuel_gauge_empty).