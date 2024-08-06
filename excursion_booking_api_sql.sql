CREATE DATABASE excursions;
USE excursions;

-- Create main table used to store bookings made via api
CREATE TABLE `excursion_bookings` (
tour_guide VARCHAR(50) DEFAULT NULL,
location VARCHAR(50) DEFAULT NULL,
`9-12` INTEGER DEFAULT NULL,
`9-12_bookingid` VARCHAR(50) DEFAULT NULL,
`13-18` INTEGER DEFAULT NULL,
`13-18_bookingid` VARCHAR(50) DEFAULT NULL,
`19-23` INTEGER DEFAULT NULL,
`19-23_bookingid` VARCHAR(50) DEFAULT NULL,
booking_date DATE NOT NULL
);


-- Loop through dates and populate table
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `filldates`(date_start DATE, date_end DATE, tour_guide VARCHAR(50))
BEGIN
  WHILE date_start <= date_end DO
    INSERT INTO excursion_bookings (tour_guide, booking_date) VALUES (tour_guide, date_start);
    SET date_start = date_add(date_start, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;

-- Remove column that wasn't utilised
ALTER TABLE excursion_bookings
DROP COLUMN location;

-- View all bookings
SELECT * FROM excursion_bookings
ORDER BY booking_date;

-- Add tour guide and date availability
CALL `excursions`.`filldates`('2024-07-01', '2024-07-07', 'Amy');