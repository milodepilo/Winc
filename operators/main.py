# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#language comparison
spain_language = "spanish"
switzerland_language = "German"
print(spain_language == switzerland_language)

#religion comparison
spain_religion = "roman catholic"
switzerland_religion = "roman catholic"
print(spain_religion == switzerland_religion)

#capital name length comparison
captial_spain = "Madrid"
captial_switzerland = "Bern"
print(len(captial_spain) == len(captial_switzerland))

#GDP comparison
GDP_spain = 1714860000000
GDP_swizterland = 590.17 * (10**12)
print(GDP_swizterland > GDP_spain)

#population growth less than 1%
pgr_spain = 0.13
pgr_switzerland = 0.65
print(pgr_spain < 1 and pgr_switzerland < 1)

#at least one has populaton > 10 mil
population_count_spain = 47163418
population_count_switzerland = 8508698
print(population_count_spain > 10000000000 or population_count_switzerland > 10000000000)

population_count_spain = 47163418
population_count_switzerland = 8508698
print(population_count_spain > 10000000000 and not population_count_switzerland > 10000000000)
