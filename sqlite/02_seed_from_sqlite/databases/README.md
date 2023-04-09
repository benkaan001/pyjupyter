
Relationships:

- An `Artist` can have `many Albums`. This is represented by the ArtistId column in the Album table, which is a foreign key referencing the Artist table's ArtistId column.

- An `Album` can have `many Tracks`. This is represented by the AlbumId column in the Track table, which is a foreign key referencing the Album table's AlbumId column.

- A `Track` belongs to `one Album` and `one Artist`. This is represented by the composite primary key (PK) in the Track table, which consists of the ArtistId and AlbumId columns. The ArtistId column is also a foreign key referencing the Artist table's ArtistId column.

- A `Track` can have `one MediaType` and `one Genre`. This is represented by the MediaTypeId and GenreId columns in the Track table, both of which are foreign keys referencing the MediaType and Genre tables' primary keys, respectively.

- A `Playlist` can have `many Tracks`, and `a Track` can belong to `many Playlists`. This is represented by the PlaylistId column in the PlaylistTrack table, which is a foreign key referencing the Playlist table's PlaylistId column. The TrackId column in the PlaylistTrack table is also a foreign key referencing the Track table's TrackId column.

- The Employee table has a one-to-many relationship with the Invoice table, as `each employee` can be associated with `multiple invoices` (via the SupportRepId foreign key in the Invoice table).

- The Invoice table has a one-to-many relationship with the InvoiceLine table, as `each invoice` can contain `multiple invoice line items`. Therefore, the Employee table `indirectly` has a one-to-many relationship with the InvoiceLine table, as `an employee` can be associated with `multiple invoices`, and each invoice can contain multiple invoice line items.

```
+------------------+       +------------------+       +----------------------+
|      Artist      |       |      Album       |       |       Track          |
+------------------+       +------------------+       +----------------------+
| ArtistId (PK)    |       | AlbumId (PK)     |       | TrackId (PK)         |
| Name TEXT        |       | Title TEXT       |       | Name TEXT            |
+------------------+       | ArtistId INTEGER |       | AlbumId INTEGER (FK) |
                           | GenreId INTEGER  |       | MediaTypeId INT (FK) |
                           +-------------------+      | GenreId INTEGER (FK) |
                                                      | Composer TEXT        |
                                                      | Milliseconds INTEGER |
                                                      | Bytes INTEGER        |
                                                      | UnitPrice NUMERIC    |
                                                      +----------------------+

+-------------------+      +--------------+        +------------------+
|     MediaType     |      |     Genre    |        |     Playlist     |
+-------------------+      +--------------+        +------------------+
| MediaTypeId (PK)  |      | GenreId (PK) |        | PlaylistId (PK)  |
| Name TEXT         |      | Name TEXT    |        | Name TEXT        |
+-------------------+      +--------------+        +------------------+

+------------------------+    +---------------------+
|  PlaylistTrack         |    |       Customer      |
+------------------------+    +---------------------+
| PlaylistId (PK, FK)    |    | CustomerId (PK) INT |
| TrackId (PK, FK)       |    | FirstName TEXT      |
| PlaylistTrackId (PK)   |    | LastName TEXT       |
+------------------------+    | Company TEXT        |
                              | Address TEXT        |
                              | City TEXT           |
                              | State TEXT          |
                              | Country TEXT        |
                              | PostalCode TEXT     |
                              | Phone TEXT          |
                              | Fax TEXT            |
                              | Email TEXT          |
                              | SupportRepId INT (FK) |
                              +---------------------+

+----------------------+      +------------------------+
|      Employee        |      |        Invoice         |
+----------------------+      +------------------------+
| EmployeeId (PK)      |      | InvoiceId (PK) INTEGER |
| LastName TEXT        |      | CustomerId INTEGER     |
| FirstName TEXT       |      | InvoiceDate TEXT       |
| Title TEXT           |      | BillingAddress TEXT    |
| ReportsTo INT (FK)   |      | BillingCity TEXT       |
| BirthDate TEXT       |      | BillingState TEXT      |
| HireDate TEXT        |      | BillingCountry TEXT    |
| Address TEXT         |      | BillingPostalCode TEXT |
| City TEXT            |      | Total NUMERIC          |
| State TEXT           |      +------------------------+
| Country TEXT         |
| PostalCode TEXT      |
| Phone TEXT           |
| Fax TEXT             |
| Email TEXT           |
+----------------------+

+---------------------+
|      InvoiceLine    |
+---------------------+
| InvoiceLineId (PK)  |
| InvoiceId INT  (FK) |
| TrackId INT (FK)    |
| UnitPrice NUMERIC   |
| Quantity INTEGER    |
+---------------------+

```