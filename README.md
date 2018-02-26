# Python Bootcamp
Resources for Python Bootcamp

Tasks for each day and the concepts to be covered is provided

## Day 1

### Send an email to yourself
* import statement, function
* print
* integer
* string

```python
from bootcamp import send_email

print("Sending Email...")
send_email("asesomemail@wtfisthis.com", "Hello there!")
```

### Send an email to yourself but with a variable

* variables

```python
from bootcamp import send_email

print("Sending Email...")
to = "asesomemail@wtfisthis.com"
message = "Hello there!"
send_email(to, message)
```

### Send an email to 10 people

* lists
* for loops

```python
person_list = ["asesomemail@wtfisthis.com", "asesomemail@wtfisthis.com", "asesomemail@wtfisthis.com"]
for person in person_list:
    print("Sending email...")
    send_email(person, message)
```

### Send an email to the 4th person in the list. Also do the previous task using list indexing
* list indexing
* len
* range

```python
person = person_list[2]
```

### Send different messages to 10 different people
* dictionaries

### Home work:
* input
Play around with input and have fun!

## Day 2
### Send emails to people in a text file
* read_file
* splitlines
* slicing

```
email@email.com Here there!\n
anotheremail@email.com Sdfkrhehf!\n
```

### Send emails depending on a condition

* if
* else

```
email@email.com, Here there!, yes\n
anotheremail@email.com, skudfhsdufhsk, no\n
```

### Calculate GPA
* operators

### Refactor code to make it more compact
* functions

```python
def calculate_gpa(scores):
    gpa = do_some_magic_here(scores)
    return gpa
```

### Home work: Send emails based on GPA scores from excel sheet

# Day 3:
### Scrap weather
* requests
* regex

Random weather generator [here](http://bootcampmanipal.appspot.com/weather)

### Check weather every 5 mins and send email if too cold
* while



