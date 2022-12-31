##SELECT * FROM Dataset WHERE job = 'management'

dataset[dataset.job == "management"]

##SELECT age FROM Dataset WHERE job = 'management'

dataset[dataset.job == "management"].age

##SELECT * FROM Dataset WHERE marital_status = 'married' AND education = 'university degree'

dataset[(dataset.marital_status == 'married') & (dataset.education == 'university degree')]

##SELECT age, job FROM Dataset WHERE marital_status = 'married' AND education = 'university degree'

dataset[(dataset.marital_status == 'married') & (dataset.education == 'university degree')
        ][['age','job']]

