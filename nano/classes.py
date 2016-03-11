import urllib
def read_text():
    quotes = open("profanity.txt")
    content_files = quotes.read()
    print(content_files)
    quotes.close()
    check_profanity(content_files)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=shot")
    output = connection.read()
    print(output)
    connection.close()
read_text()
