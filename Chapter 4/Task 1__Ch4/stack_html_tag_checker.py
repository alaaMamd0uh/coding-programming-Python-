class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # remove top item
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


# function to extract tags manually from the HTML string
def extractTags(htmlContent):
    tags=[]
    insideTag = False
    tag =""
    for char in htmlContent:
        if char == '<':
            insideTag = True
            tag ="<"
        elif char == '>':
            tag += ">"
            tags.append(tag)
            insideTag = False
        elif insideTag:
            tag += char
    return tags


# function to check if tags are balanced using the custom stack
def check_balance(htmlContent):
    stack = Stack()
    tags = extractTags(htmlContent)

    for tag in tags:
        if tag.startswith("</"):  # closing tag
            tag_name = tag[2:-1].strip()
            if stack.is_empty() or stack.peek() != tag_name:
                return "Invalid"
            stack.pop()
        else:
            tag_name = tag[1:-1].strip()
            stack.push(tag_name)

    return "Valid" if stack.is_empty() else "Invalid"


with open("test.html") as file:
    htmlContent = file.read()

print("__________________________________________")
print(htmlContent)  # to check what we read
print("__________________________________________")

print(check_balance(htmlContent))
