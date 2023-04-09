-- drop tables if they already exist
-- using CASCADE to overwrite the FK constraint on reload
DROP TABLE IF EXISTS artists CASCADE;
DROP TABLE IF EXISTS albums CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS media_types CASCADE;
DROP TABLE IF EXISTS tracks CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS invoices CASCADE;
DROP TABLE IF EXISTS invoice_items CASCADE;
DROP TABLE IF EXISTS playlists CASCADE;
DROP TABLE IF EXISTS playlist_track CASCADE;



-- Create table artists
CREATE TABLE artists (
  ArtistId INTEGER PRIMARY KEY,
  Name TEXT
);

-- Create table albums
CREATE TABLE albums (
  AlbumId INTEGER PRIMARY KEY,
  Title TEXT,
  ArtistId INTEGER,
  FOREIGN KEY (ArtistId) REFERENCES artists (ArtistId)
);

-- Create table genres
CREATE TABLE genres (
  GenreId INTEGER PRIMARY KEY,
  Name TEXT
);

-- Create table media_types
CREATE TABLE media_types (
  MediaTypeId INTEGER PRIMARY KEY,
  Name TEXT
);

-- Create table tracks
CREATE TABLE tracks (
  TrackId INTEGER PRIMARY KEY,
  Name TEXT,
  AlbumId INTEGER,
  MediaTypeId INTEGER,
  GenreId INTEGER,
  Composer TEXT,
  Milliseconds INTEGER,
  Bytes INTEGER,
  UnitPrice REAL,
  FOREIGN KEY (AlbumId) REFERENCES albums (AlbumId),
  FOREIGN KEY (MediaTypeId) REFERENCES media_types (MediaTypeId),
  FOREIGN KEY (GenreId) REFERENCES genres (GenreId)
);


-- Create table Employees
CREATE TABLE employees (
  EmployeeId INTEGER PRIMARY KEY,
  LastName TEXT,
  FirstName TEXT,
  Title TEXT,
  ReportsTo INTEGER,
  BirthDate TEXT,
  HireDate TEXT,
  Address TEXT,
  City TEXT,
  State TEXT,
  Country TEXT,
  PostalCode TEXT,
  Phone TEXT,
  Fax TEXT,
  Email TEXT,
  CONSTRAINT fk_reports_to FOREIGN KEY (ReportsTo) REFERENCES employees (EmployeeId)
);

-- Create table customers
CREATE TABLE customers (
  CustomerId INTEGER PRIMARY KEY,
  FirstName TEXT,
  LastName TEXT,
  Company TEXT,
  Address TEXT,
  City TEXT,
  State TEXT,
  Country TEXT,
  PostalCode TEXT,
  Phone TEXT,
  Fax TEXT,
  Email TEXT,
  SupportRepId INTEGER,
  FOREIGN KEY (SupportRepId) REFERENCES employees (EmployeeId)
);

-- Create table invoices
CREATE TABLE invoices (
  InvoiceId INTEGER PRIMARY KEY,
  CustomerId INTEGER,
  InvoiceDate TEXT,
  BillingAddress TEXT,
  BillingCity TEXT,
  BillingState TEXT,
  BillingCountry TEXT,
  BillingPostalCode TEXT,
  Total REAL,
  FOREIGN KEY (CustomerId) REFERENCES customers (CustomerId)
);

-- Create table invoice_items
CREATE TABLE invoice_items (
  InvoiceLineId INTEGER PRIMARY KEY,
  InvoiceId INTEGER,
  TrackId INTEGER,
  UnitPrice REAL,
  Quantity INTEGER,
  FOREIGN KEY (InvoiceId) REFERENCES invoices (InvoiceId),
  FOREIGN KEY (TrackId) REFERENCES tracks (TrackId)
);

-- Create table playlists
CREATE TABLE playlists (
  PlaylistId INTEGER PRIMARY KEY,
  Name TEXT
);

-- Create table playlist_track
CREATE TABLE playlist_track (
  PlaylistId INTEGER,
  TrackId INTEGER,
  CONSTRAINT pk_PlaylistTrack PRIMARY KEY (PlaylistId, TrackId),
  FOREIGN KEY (PlaylistId) REFERENCES playlists (PlaylistId),
  FOREIGN KEY (TrackId) REFERENCES tracks (TrackId)
);

