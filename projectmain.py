from time import time

def typingErrors(prompt, iwords, words):
    errors = 0
    for i in range(min(len(iwords), len(words))):
        if i in (0, len(iwords)-1):
            if iwords[i] != words[i]:
                errors += 1
        else:
            if iwords[i] != words[i] or (iwords[i+1] != words[i+1] and iwords[i-1] != words[i-1]):
                errors += 1
    return errors

def typingSpeed(iprompt, stime, etime):
    iwords = iprompt.split()
    twords = len(iwords)
    elapsed_time = etime - stime
    speed = twords / elapsed_time * 60  # words per minute
    return speed

def timeElapsed(stime, etime):
    return round(etime - stime, 2)

if __name__ == '__main__':
    while True:
        prompt = "Self-confidence is a tricky subject for many people. For some, it's impossible to feel good about themselves without outside validation. When you're in a situation where the people in your life aren't helping you to feel better about yourself, this can become a problem in your day to day life. Most insecurity stems from feelings of not being attractive or feelings of loneliness. If your insecurity doesn't necessarily stem from a lack of interaction, but more a lack of feeling attractive, there are other options that will help you online. Sometimes the best way to put your insecurities to rest can simply be to get an honest opinion. There are multiple support groups online where you can share a picture of yourself with other members and they will give honest feedback on your appearance. In most cases, they will point out good qualities that you may have missed in yourself. But you can trust them to be honest and many members give very valuable style and posture advice to increase your attractiveness. These practical tips and unbiased opinions from supportive strangers will immediately help you feel better about yourself, and if the tips are implemented it will also improve your self-esteem in the long-run."
        print("Type this: '", prompt, "'")

        input("Press ENTER when you are ready!")

        stime = time()
        iprompt = input()
        etime = time()

        time_taken = timeElapsed(stime, etime)
        speed = typingSpeed(iprompt, stime, etime)
        errors = typingErrors(prompt.split(), iprompt.split(), prompt.split())

        print("Total Time elapsed:", time_taken, "s")
        print("Your Average Typing Speed was:", speed, "words/minute")
        print("With a total of:", errors, "errors")

        choice = input("Start again? (yes/no): ").lower()
        if choice != 'yes':
            break
