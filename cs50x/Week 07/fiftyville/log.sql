-- Keep a log of any SQL queries you execute as you solve the mystery.

select description from crime_scene_reports where year = 2024 and month = 7 and day = 28 and street = "Humphrey Street";

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time,
-- each of their interview transcripts mentions the bakery.

select transcript from interviews where year = 2024 and month = 7 and day = 28;

-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery
-- parking lot and drive away. If you have security footage from the bakery parking lot,
-- you might want to look for cars that left the parking lot in that time frame.

-- I don't know the thief's name, but it was someone I recognized. Earlier this morning,
-- before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw
-- the thief there withdrawing some money.

-- As the thief was leaving the bakery, they called someone who talked to them for less
-- than a minute. In the call, I heard the thief say that they were planning to take the
-- earliest flight out of Fiftyville tomorrow. The thief then asked the person on the
-- other end of the phone to purchase the flight ticket.

-- People who left the bakery within ten minutes of the theft
create temp table suspects1 as
select * from people where license_plate in (
    select license_plate from bakery_security_logs where year = 2024 and month = 7 and day = 28
    and hour = 10 and minute between 15 and 25 and activity = "exit"
);

-- +--------+---------+----------------+-----------------+---------------+
-- |   id   |  name   |  phone_number  | passport_number | license_plate |
-- +--------+---------+----------------+-----------------+---------------+
-- | 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
-- | 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
-- | 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
-- | 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
-- | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+---------+----------------+-----------------+---------------+

-- People who withdrew money from the ATM on Leggett Street
create temp table suspects2 as
select * from suspects1 where id in (
    select person_id from bank_accounts where account_number in (
        select account_number from atm_transactions where year = 2024 and month = 7 and day = 28
        and atm_location = "Leggett Street" and transaction_type = "withdraw"
    )
);

-- +--------+--------+----------------+-----------------+---------------+
-- |   id   |  name  |  phone_number  | passport_number | license_plate |
-- +--------+--------+----------------+-----------------+---------------+
-- | 396669 | Iman   | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 514354 | Diana  | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+--------+----------------+-----------------+---------------+

-- Calls from suspects2 that lasted less than one minute.
create temp table suspect_phone_calls as
select * from phone_calls where year = 2024 and month = 7 and day = 28 and caller in (
    select phone_number from suspects2
) and duration < 60;

-- People who are callers in suspect_phone_calls
create temp table suspects3 as
select * from suspects2 where phone_number in (
    select caller from suspect_phone_calls
);

-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+-------+----------------+-----------------+---------------+

-- The earliest flight out of Fiftville on the 29th
create temp table earliest_flight as
select * from flights where year = 2024 and month = 7 and day = 29 and origin_airport_id = (
    select id from airports where city = "Fiftyville"
) order by hour, minute limit 1;

select city from airports where id = (
    select destination_airport_id from earliest_flight
);

-- Destination: New York City

create temp table thief as
select id, name, phone_number, suspects3.passport_number, license_plate from suspects3 join (
    select passport_number from passengers where flight_id = (
        select id from earliest_flight
    )
) as passports on suspects3.passport_number = passports.passport_number;

-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+-------+----------------+-----------------+---------------+

-- Thief: Bruce

-- Person whom Bruce called
create temp table accomplice as
select * from people where phone_number = (
    select receiver from suspect_phone_calls where caller = (
        select phone_number from thief
    )
);

-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
-- +--------+-------+----------------+-----------------+---------------+

-- Accomplice: Robin
