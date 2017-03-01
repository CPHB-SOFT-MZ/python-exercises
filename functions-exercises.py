import webget


def print_list(li):
    if len(li) == 1:
        print(li[0])
        return
    print(li[0])
    print_list(li[1:])

l = list(range(0, 10))
# print_list(l)
url = "https://media.giphy.com/media/7ZLBE03JfTAFG/giphy.gif"
# to = "/Users/Mikkel/Desktop"
webget.download(url)
