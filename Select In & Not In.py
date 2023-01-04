##SELECT * FROM Dataset WHERE job in ('services', 'technician')

Dataset[Dataset.job.isin(['services','technician'])]

##SELECT education FROM Dataset WHERE job in ('services', 'technician')

Dataset[Dataset.job.isin(['services','technician'])].education

##SELECT * FROM Dataset WHERE marital_status not in ('married', 'single')

Dataset[~Dataset.marital_status.isin(['married','single'])]

##SELECT job FROM Dataset WHERE marital_status not in ('married', 'single')

Dataset[~Dataset.marital_status.isin(['married','single'])].job
