"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"


def txt_reader(fileName):
    # assigns f to the passed file
    f = open(fileName, 'r')
    # reads the file content and assigns it to content variable
    content = f.read()
    # prints content
    print(content)
    # closes the file
    f.close()
    # lets user know file is closed
    print(f'File Closed: {f.closed}')


# calls txt_reader file
txt_reader('foo.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


def txt_writer(fileName, *args):
    # assigns f to the passed file
    f = open(fileName, 'w')
    # prints statement indicating function is writing to file
    print(f'Writing To File: {fileName}')
    # writes each value in args to file
    for item in args:
        f.write(f'\n {item}')
    # closes the file
    f.close()
    # lets user know file is closed
    print(f'File Closed: {f.closed}')


txt_writer('bar.txt', 'this is line one',
           'this is line two', 'this is line three')
