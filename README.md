# Booking API tests

To execute test:
```
/bin/bash run.sh
```

## General project description:
```
* For autorization proccess, username and password params are required in command (currently hardcoded in run.sh file).
* Scenarios for APIs that doesn't requires token, executes without authorisation.
* Authorization process triggeres only once on init stage.
* Test, that found bug in the service, has been put on skip.
* Test parametrizing was used where it make a sense. 
* Tests are executes in parallel mode to reduce execution time.
```

## Implemented scenarios:
```
1. Service ping.
2. Create booking (all fields)
3. Create booking (mandatory fields only)
4. Create booking without any of mandatory filed (error expected).
5. Get bookings by firstname, lastname (full match expected).
6. Get bookings by date (greater than or equal to match expected).
7. Full update booking (token in request).
8. Full update booking (no token in request, error expected).
9. Partial update booking (token in request).
10. Partial update booking (no token in request, error expected).
11. Delete booking (token in request).
12. Delete booking (no token in request, error expected).
13. Delete booking by invalid id (token in request, error expected).
*** 
    Get booking by invalid id was not implemented separetly, because scenario already covered as part of 'Delete booking'.
```
## Bugs & Issues:
```
1. Filter for bookings by check-in date doesn't works properly for new bookings. It works only for condition 'greater then', but not for 'equals to'.
Bug reproduces only for new records. For old records bug is not reproduces.
2. Some status codes in responses logically not matches to event.
For example, for 'Create booking without any of mandatory filed' expected error code should be 400 (Bad request) and not 500.
  
```


