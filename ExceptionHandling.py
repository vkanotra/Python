a = 5
b = 0

try:
    print("connection resource open")
    print(a/b)                              # If run time error, then further stmts are'nt executed, so we use try block
    print("connection resource closed")     # This statement will still not run, so we use it in finally block

except ZeroDivisionError as e:
    print("Hi,", e)

except ValueError as e:
    print("Hi,", e)

except Exception as e:
    print("Hi,", e)

finally:                               # will run if error or if no error
    print("connection resource closed in finally block")

print("hello")
print("rest of the code")