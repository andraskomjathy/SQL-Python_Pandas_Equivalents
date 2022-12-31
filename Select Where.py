##SELECT * FROM Dataset WHERE Job = 'management'

dataset[dataset.job == "management"]

##SELECT Age FROM Dataset WHERE Job = 'management'

dataset[dataset.job == "management"].age

##SELECT * FROM Dataset WHERE Marital_status = 'married' AND Education = 'university degree'

dataset[(dataset.Marital_status == 'married') & (dataset.Education == 'university degree')]

##SELECT Age, Job FROM Dataset WHERE Marital_status = 'married' AND Education = 'university degree'

dataset[(dataset.Marital_status == 'married') & (dataset.Education == 'university degree')
        ][['Age','Job']]

