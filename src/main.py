from textnode import TextNode, TextType
print("hello world")

def main():
    textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textNode)


main()
