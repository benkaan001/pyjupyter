# ADVANCED QUESTIONS

## Question 1

`Write a query to calculate the running total of sales for each month in the year 2012, including months with no sales.`

(Hint: Refer to invoices table. Use a combination of subqueries and join)

## Expected Output
| InvoiceMonthFinal | TotalSales | RunningTotalSales |
| --- | --- | --- |
| January | 37.62 | 37.62 |
| February | 27.72 | 65.34 |
| March | 37.62 | 102.96 |
| April | 33.66 | 136.62 |
| May | 37.62 | 174.24 |
| June | 37.62 | 211.86 |
| July | 37.62 | 249.48 |
| August | 37.62 | 287.10 |
| September | 37.62 | 324.72 |
| October | 37.62 | 362.34 |
| November | 49.62 | 411.96 |
| December | 38.62 | 450.58 |


## Question 2

`Write a query to retrieve the top 5 customers who have made the most purchases over the past 6 months, but exclude customers who have made a single large purchase.`

(Hint: use the HAVING clause to filter out customers who have only made one purchase)

## Expected Output:

| CustomerId | CustomerFullName   | PurchaseCount | TotalSpend | InvoiceId | FirstPurchaseDate |
| ---       | ---                | ---           | ---        | ---       | ---               |
| 26        | Richard Cunningham | 14            | 23.86      | 299       | 2012-08-05       |
| 55        | Mark Taylor        | 14            | 13.86      | 250       | 2012-01-01       |
| 34        | João Fernandes     | 14            | 13.86      | 257       | 2012-02-01       |
| 13        | Fernanda Ramos     | 14            | 13.86      | 264       | 2012-03-03       |
| 51        | Joakim Johansson   | 14            | 13.86      | 271       | 2012-04-03       |


## Question 3

`Write a query to retrieve the names of all artists who have never had an album with fewer than 10 tracks.`

(Hint: use a subquery with a NOT EXISTS clause)

## Expected Output

| Name                              |
|-----------------------------------|
| AC/DC                             |
| Aerosmith                         |
| Alanis Morissette                 |
| Alice In Chains                   |
| Amy Winehouse                     |
| Antônio Carlos Jobim              |
| Audioslave                        |
| BackBeat                          |
| Battlestar Galactica              |
| Battlestar Galactica (Classic)    |
| Black Label Society               |
| Black Sabbath                     |
| Body Count                        |
| Bruce Dickinson                   |
| Buddy Guy                         |
| Caetano Veloso                    |
| Cássia Eller                      |
| Chico Buarque                     |
| Chico Science & Nação Zumbi       |
| Chris Cornell                     |
| Cidade Negra                      |
| Cláudio Zoli                      |
| Creedence Clearwater Revival      |
| David Coverdale                   |
| Deep Purple                       |
| Def Leppard                       |
| Djavan                            |
| Ed Motta                          |
| Elis Regina                       |
| Eric Clapton                      |
| Faith No More                     |
| Falamansa                         |
| Foo Fighters                      |
| Frank Sinatra                     |
| Funk Como Le Gusta                |
| Gene Krupa                        |
| Gilberto Gil                      |
| Godsmack                          |
| Gonzaguinha                       |
| Green Day                         |
| Guns N' Roses                     |
| Heroes                            |
| House Of Pain                     |
| Incognito                         |
| Iron Maiden                       |
| James Brown                       |
| Jamiroquai                        |
| JET                               |
| Jimi Hendrix                      |
| João Suplicy                      |
| Joe Satriani                      |
| Jorge Ben                         |
| Jota Quest                        |
| Judas Priest                      |
| Kiss                              |
| Led Zeppelin                      |
| Legião Urbana                     |
| Lenny Kravitz                     |
| Lost                              |
| Lulu Santos                       |
| Marcos Valle                      |
| Marillion                         |
| Marisa Monte                      |
| Marvin Gaye                       |
| Men At Work                       |
| Metallica                         |
| Miles Davis                       |
| Milton Nascimento                 |
| Mônica Marianno                   |
| Mötley Crüe                       |
| Motörhead                         |
| Nirvana                           |
| O Rappa                           |
| O Terço                           |
| Olodum                            |
| Os Mutantes                       |
| Os Paralamas Do Sucesso           |
| Ozzy Osbourne                     |
| Page & Plant                      |
| Passengers                        |
| Paul D'Ianno                      |
| Pearl Jam                         |
| Planet Hemp                       |
| Queen                             |
| R.E.M.                            |
| R.E.M. Feat. Kate Pearson         |
| Raimundos                         |
| Raul Seixas                       |
| Red Hot Chili Peppers             |
| Rush                              |
| Santana                           |
| Scorpions                         |
| Skank                             |
| Smashing Pumpkins                 |
| Soundgarden                       |
| Spyro Gyra                        |
| Stevie Ray Vaughan & Double Trouble|
| Stone Temple Pilots               |
| System Of A Down                  |
| Temple of the Dog                 |
| The Black Crowes                  |
| The Clash                         |
| The Cult                          |
| The Doors                         |
| The Office                        |
| The Police                        |
| The Rolling Stones                |
| The Tea Party                     |
| The Who                           |
| Tim Maia                          |
| Titãs                             |
| Toquinho & Vinícius               |
| U2                                |
| UB40                              |
| Van Halen                         |
| Various Artists                   |
| Velvet Revolver                   |
| Vinícius De Moraes                |
|Zeca Pagodinho                    |


## Question 4
`Write a query to retrieve the average revenue per customer for each country in the database, but only include countries with more than 10 customers.`

(Hint: use a combination of subqueries and the HAVING clause)

| Country   |   AvgRevenuePerCustomer |   TotalRevenue |
|:----------|------------------------:|---------------:|
| Germany   |                1.39714  |         156.48 |
| France    |                1.11486  |         195.09 |
| Brazil    |                1.08629  |         190.09 |
| Canada    |                0.678482 |         303.95 |
| USA       |                0.442147 |         523.06 |

## Question 5
`Write a query to retrieve the names of all customers who have made a purchase within 5 minutes of their last purchase.`

(Hint: use the LAG() window function and the TIMESTAMPDIFF() function)

## Expected Output:

|   CustomerId |   TotalPurchase | PurchaseDate   | PreviousPurchaseDate   |
|-------------:|----------------:|:---------------|:-----------------------|
|            3 |           13.86 | 2010-04-21     | 2010-03-11             |
|            7 |           18.86 | 2010-01-18     | 2009-12-08             |
|           12 |           13.86 | 2010-12-25     | 2010-11-14             |
|           16 |           13.86 | 2010-09-23     | 2010-08-13             |
|           20 |           13.86 | 2010-06-22     | 2010-05-12             |
|           24 |           15.86 | 2010-03-21     | 2010-02-08             |
|           33 |           13.86 | 2010-11-24     | 2010-10-14             |
|           37 |           13.86 | 2010-08-23     | 2010-07-13             |
|           41 |           13.86 | 2010-05-22     | 2010-04-11             |
|           45 |           21.86 | 2010-02-18     | 2010-01-08             |
|           54 |           13.86 | 2010-10-24     | 2010-09-13             |
|           58 |           13.86 | 2010-07-23     | 2010-06-12             |


## Question 6
`Write a query to retrieve the total revenue generated by each genre, but exclude any revenue from tracks with a duration of less than 30 seconds.`

(Hint: use a subquery with a NOT IN clause)



## Question 7
`Write a query to retrieve the name of the customer who has made the largest percentage increase in purchases compared to the previous year.`

(Hint: use a self-join and the LAG() window function)



