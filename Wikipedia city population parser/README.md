Inspired from https://github.com/prajwal72/City-Details <br >
This repo allowing to get a full info from Wikipedia article for 1 city_name <br >
I wanted to get just 1 parameter (population) from multiple city names

### How to use this parser
* Open [Wikipedia (wiki) population parser.ipynb]()
* Have a list of city_names in English in a valid wiki format <br >
* To check which names are valid, insert name after wiki/ <br >
example:
https://en.wikipedia.org/wiki/Limassol
* Change city names in city_names variable
* Run it and look at progress bar. It takes about 2 second per city
* Get result_df_sorted. It contains city_name and a bunch of population columns

Unfortunately, resulted dataset will contain data about population and area, they use the same names <br >
This is how to clean such data quickly [example](https://docs.google.com/spreadsheets/d/1-8ECzjb8rjlTTc9BUJQxNiSKWHopB2tw0X9NdC_fdl8/edit?usp=sharing)

To do. Delete &nbsp values without deleting the whole thing, add ability to get area/population