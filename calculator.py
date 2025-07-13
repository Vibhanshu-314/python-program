# my aim is understand the concept of the loops in funny way and make code fun -friendly for viewers



a, b = map(int, input("Enter the positive values / बड़े भाई ढंग की वैल्यू डालो प्लीज़: ").split())
n = input('''

    1. Add करना है आ जाओ
    2. Minus यानी Subtract करना है आ जाओ
    3. Product करना है आ जाओ
    4. Divide करना है आ जाओ
    5. कुछ नहीं करना है — बाहर जाना है यानी Exit 🙃

Enter your choice (1-5): ''')

# Addition function
def add():
    return a + b

# Subtraction function
def sub():
    return a - b

# Multiplication function
def product():
    return a * b

# Division function
def divide():
    if b != 0:
        return a / b
    else:
        return "Zero se divide nahi hota bhai!"

# Ab user ke input ke hisaab se function call kar rahe hain
if n == "1":
    print("Result:", add())

elif n == "2":
    print("Result:", sub())

elif n == "3":
    print("Result:", product())

elif n == "4":
    print("Result:", divide())

elif n == "5":
    print("धन्य हो भाई! खत्म तो किया आपने 😂")

else:
    print("कहा था भाई की ढंग का नंबर डाल!!!")



