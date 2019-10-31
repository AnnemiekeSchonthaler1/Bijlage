-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-10-23 11:13:31.795

-- tables
-- Table: Dataset_tabel
CREATE TABLE Dataset_tabel (
    dataset_int int NOT NULL,
    HMM text NOT NULL,
    CONSTRAINT Dataset_tabel_pk PRIMARY KEY (dataset_int)
);

-- Table: Eiwit
CREATE TABLE Eiwit (
    eiwit_naam varchar(50) NOT NULL,
    eiwitfamilie_familie_naam varchar(10) NOT NULL,
    consensuspatroon varchar(50) NOT NULL,
    CONSTRAINT Eiwit_pk PRIMARY KEY (eiwit_naam)
);

-- Table: Eiwit_functie
CREATE TABLE Eiwit_functie (
    functie varchar(10) NOT NULL,
    CONSTRAINT Eiwit_functie_pk PRIMARY KEY (functie)
);

-- Table: Eiwitsequentie
CREATE TABLE Eiwitsequentie (
    accessiecode varchar(6) NOT NULL,
    seq varchar(400) NOT NULL,
    Eiwit_eiwit_naam varchar(50) NOT NULL,
    CONSTRAINT Eiwitsequentie_pk PRIMARY KEY (accessiecode)
);

-- Table: Geconserveerde_stukken
CREATE TABLE Geconserveerde_stukken (
    motif varchar(300) NOT NULL,
    Eiwit_eiwit_naam varchar(50) NOT NULL,
    CONSTRAINT Geconserveerde_stukken_pk PRIMARY KEY (motif)
);

-- Table: Tussentabel_eiwit_dataset
CREATE TABLE Tussentabel_eiwit_dataset (
    Eiwit_eiwit_naam varchar(50) NOT NULL,
    ID int NOT NULL,
    Dataset_tabel_dataset_int int NOT NULL,
    CONSTRAINT Tussentabel_eiwit_dataset_pk PRIMARY KEY (ID)
);

-- Table: Tussentabel_eiwit_eiwit_functie
CREATE TABLE Tussentabel_eiwit_eiwit_functie (
    Eiwit_eiwit_naam varchar(50) NOT NULL,
    Eiwit_functie_functie varchar(10) NOT NULL,
    ID int NOT NULL,
    CONSTRAINT Tussentabel_eiwit_eiwit_functie_pk PRIMARY KEY (ID)
);

-- Table: eiwitfamilie
CREATE TABLE eiwitfamilie (
    domein varchar(10) NOT NULL,
    familie_naam varchar(10) NOT NULL,
    CONSTRAINT eiwitfamilie_pk PRIMARY KEY (familie_naam)
);

-- foreign keys
-- Reference: Eiwit_eiwitfamilie (table: Eiwit)
ALTER TABLE Eiwit ADD CONSTRAINT Eiwit_eiwitfamilie FOREIGN KEY Eiwit_eiwitfamilie (eiwitfamilie_familie_naam)
    REFERENCES eiwitfamilie (familie_naam);

-- Reference: Eiwitsequentie_geen_mutatie_Eiwit (table: Eiwitsequentie)
ALTER TABLE Eiwitsequentie ADD CONSTRAINT Eiwitsequentie_geen_mutatie_Eiwit FOREIGN KEY Eiwitsequentie_geen_mutatie_Eiwit (Eiwit_eiwit_naam)
    REFERENCES Eiwit (eiwit_naam);

-- Reference: Geconserveerde_stukken_Eiwit (table: Geconserveerde_stukken)
ALTER TABLE Geconserveerde_stukken ADD CONSTRAINT Geconserveerde_stukken_Eiwit FOREIGN KEY Geconserveerde_stukken_Eiwit (Eiwit_eiwit_naam)
    REFERENCES Eiwit (eiwit_naam);

-- Reference: Table_13_Eiwit (table: Tussentabel_eiwit_eiwit_functie)
ALTER TABLE Tussentabel_eiwit_eiwit_functie ADD CONSTRAINT Table_13_Eiwit FOREIGN KEY Table_13_Eiwit (Eiwit_eiwit_naam)
    REFERENCES Eiwit (eiwit_naam);

-- Reference: Table_13_Eiwit_functie (table: Tussentabel_eiwit_eiwit_functie)
ALTER TABLE Tussentabel_eiwit_eiwit_functie ADD CONSTRAINT Table_13_Eiwit_functie FOREIGN KEY Table_13_Eiwit_functie (Eiwit_functie_functie)
    REFERENCES Eiwit_functie (functie);

-- Reference: Table_18_Eiwit (table: Tussentabel_eiwit_dataset)
ALTER TABLE Tussentabel_eiwit_dataset ADD CONSTRAINT Table_18_Eiwit FOREIGN KEY Table_18_Eiwit (Eiwit_eiwit_naam)
    REFERENCES Eiwit (eiwit_naam);

-- Reference: Tussentabel_eiwit_dataset_Dataset_tabel (table: Tussentabel_eiwit_dataset)
ALTER TABLE Tussentabel_eiwit_dataset ADD CONSTRAINT Tussentabel_eiwit_dataset_Dataset_tabel FOREIGN KEY Tussentabel_eiwit_dataset_Dataset_tabel (Dataset_tabel_dataset_int)
    REFERENCES Dataset_tabel (dataset_int);

-- End of file.
