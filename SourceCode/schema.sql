DROP TABLE IF EXISTS Host;
DROP TABLE IF EXISTS Vacancies;
DROP TABLE IF EXISTS Applicants;
DROP TABLE IF EXISTS Applications;


CREATE TABLE Host (
  hostID int NOT NULL UNIQUE,
  email varchar(255) NOT NULL,
  lastName varchar(255) NOT NULL,
  firstName varchar(255) NOT NULL,
  hPassword varchar(255) NOT NULL,
  phoneNumber int,
  rating int DEFAULT 5,
  CHECK (
    rating <= 10
    AND rating >= 0
        ),
  PRIMARY KEY (hostID)
);

CREATE TABLE Vacancies (
        vacancyID int NOT NULL UNIQUE,
        hostID int NOT NULL UNIQUE,
        location varchar(255) NOT NULL,
        description varchar(255),
        rate varchar(255) NOT NULL,
        startDate date NOT NULL,
        endDate date NOT NULL,
        available bit DEFAULT 1,
        curfew time,
        extraInfo varchar(255),
        images varchar(255),
        PRIMARY KEY (vacancyID),
        FOREIGN KEY (HostID) REFERENCES Host(HostID)
);

CREATE TABLE Applicants (
        applicantID int NOT NULL UNIQUE,
        email varchar(255) NOT NULL,
        lastName varchar(255) NOT NULL,
        firstName varchar(255) NOT NULL,
phoneNumber int,
aPassword varchar(255) NOT NULL,
dietaryRequirements varchar(255),
rating int DEFAULT 5,
dob date NOT NULL,
university NOT NULL,
nationality NOT NULL,
        CHECK (
    rating <= 10
    AND rating >= 0
        ),
        PRIMARY KEY (applicantID)
);

CREATE TABLE Applications (
        vacancyID int UNIQUE NOT NULL,
        ApplicantID int NOT NULL,
        description varchar(255),
        PRIMARY KEY (applicantID, vacancyID),
FOREIGN KEY (vacancyID) REFERENCES Vacancies(VacancyID),
FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
);

