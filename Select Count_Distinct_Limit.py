##SELECT DISTINCT month FROM Dataset

dataset.month.unique()

##SELECT COUNT(campaign) FROM Dataset

dataset.campaign.size

##SELECT COUNT(DISTINCT age) FROM Dataset

dataset.age.nunique()

##SELECT * FROM Dataset LIMIT 10

dataset.head(10)

##SELECT DISTINCT age FROM Dataset LIMIT 10

dataset.age.head(10).unique()

##SELECT COUNT(DISTINCT age) FROM Dataset LIMIT 10

dataset.age.head(10).nunique()

