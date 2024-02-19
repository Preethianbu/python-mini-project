from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"(.*)how are you(.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"(good|well|okay|ok)(.*)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"(what's|want)(.*) ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["top secret ;)","Preethi Anbu created me using Python's NLTK library ",]
    ],
    [
        r"(located|location|city|where are you)(.*) ?",
        ['Chennai, India',]
    ],
    [
        r"(.*)raining(.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"(how|health)(.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"(.*)quit(.*)",
        ["Bye for now. See you soon :) ,It was nice talking to you."]
    ],
    [
        r"(.*)age(.*)",
        ["oh! I don't really have age, I'm just here to have fun and chat with you"]
    ],
    [
        r"are you single",
        ["Haha, well, as a virtual friend, I don't really have a relationship status. 😄 But I'm here to chat and be a good friend!"]
    ],
    [
        r"(.*)sorry(.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"(.*)",
        ['Thats nice to hear but I am unable to answer your question, please ask my friend Google']
    ],
    
]
my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}
#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()
while True:
    response = chat.converse()
    if response == 'quit':
        break

    choice = input("Chat again? (yes/no): ")
    if choice.lower() != 'yes':
        break
