import mysql.connector

# Database connection details (replace with your own)
host = "localhost"
user = "your_username"
password = "your_password"

try:
  # Connect to MySQL server
  db = mysql.connector.connect(host=host, user=user, password=password)
  cursor = db.cursor()

  # Create database query (uses IF NOT EXISTS to avoid errors)
  sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
  cursor.execute(sql)

  # Commit the change
  db.commit()

  print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
  print("Error creating database:", err)

finally:
  # Close the connection regardless of success or failure
  if db:
    db.close()
    cursor.close()

