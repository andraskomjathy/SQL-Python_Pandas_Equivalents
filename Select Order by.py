##SELECT * FROM dataset WHERE marital_status = 'married' ORDER BY age

dataset[dataset.marital_status == 'married'].sort_values('age')

##SELECT * FROM dataset WHERE marital_status = 'single' ORDER BY age DESC

dataset[dataset.marital_status == 'single'].sort_values('age', ascending=False)

##SELECT department FROM dataset WHERE country_code = 'DE'
##ORDER BY satisfaction_score DESC

(dataset[dataset.country_code == 'DE'].sort_values('satisfaction_score',ascending=False)).department

##SELECT department, satisfaction_score FROM dataset WHERE country_code = 'DE'
##ORDER BY satisfaction_score

(dataset[dataset.country_code == 'DE'][['department','satisfaction_score']]
 .sort_values('satisfaction_score'))

