import duckdb

conn = duckdb.connect(database='review2.duckdb')

print("Creating table...")
conn.execute('create schema if not exists company_schema')
conn.execute("""
               create or replace table company_schema.employee (
             id integer,
             name varchar,
             age integer,
             department varchar,
             salary float)   
             """)

print("table created successfully")
print("inserting data...")

conn.execute("""insert into company_schema.employee (id, name, age, department, salary) values
                (1, 'apple', 30, 'HR', 60000),  
                (2, 'abc', 25, 'Engineering', 75000),  
                (3, 'xyz', 28, 'Marketing', 50000),
                (4, 'pqr', 35, 'Engineering', 80000),
                (5, 'efg', 29, 'HR', 62000)
             """)

print("data inserted successfully")
result = conn.execute("select * from company_schema.employee").fetchall()
print(result)        
print("data fetched successfully")
