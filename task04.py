from task02 import calc_dragon_heads

def main():
    age = int (input("Input dragon age:"))

    head = calc_dragon_heads(age)

    msg = f"Dragon with {age}hears has {head} heads."
    print(msg)

if __name__=="__main__":
    main()