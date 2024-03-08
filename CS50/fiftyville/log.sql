-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports 
WHERE year = 2021 AND month = 7 AND day = 28 
AND street = 'Humphrey Street';

SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 ;

SELECT name from bakery_security_logs JOIN people
ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND month = 7 AND day = 28
AND hour = 10 AND minute > 15;

SELECT name FROM 
people JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.atm_location = 'Leggett Street' AND
year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw';

SELECT name FROM phone_calls JOIN people
ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND month = 7 AND day = 28
AND duration < 60;

SELECT * FROM airports WHERE city = "Fiftyville";

SELECT * FROM flights WHERE origin_airport_id = 8 AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour;

SELECT name FROM bakery_security_logs JOIN people
ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021 AND month = 7 AND day = 28
AND hour = 10 AND minute > 15 AND minute < 30
INTERSECT
SELECT name FROM
people JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.atm_location = 'Leggett Street' AND
year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw'
INTERSECT
SELECT name FROM phone_calls JOIN people
ON people.phone_number = phone_calls.caller
WHERE year = 2021 AND month = 7 AND day = 28
AND duration < 60
INTERSECT
SELECT name FROM people JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
JOIN airports ON airports.id = origin_airport_id
WHERE year = 2021 AND month = 7 AND day = 29

SELECT * FROM people WHERE name = 'Bruce'

SELECT receiver FROM phone_calls WHERE caller = '(367) 555-5533' 
AND day = 28 AND month = 7 AND duration < 60;

SELECT name FROM people where phone_number = '(375) 555-8161';

SELECT * FROM airports WHERE id = 4;
