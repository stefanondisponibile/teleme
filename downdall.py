import argparse
from teleme import messages
from pprint import pprint

def main():
    parser = argparse.ArgumentParser("Download your telegram messages.")
    parser.add_argument("-n", "--name", help="Target conversation name.", default="B-ubusetette 🍒", type=str)
    parser.add_argument("-l", "--limit", help="Limit the number of messages retrieved.", default=None, type=int)
    parser.add_argument("-u", "--user", help="Target user name.", default=None, type=str)
    parser.add_argument("-d", "--dump", help="Dump data.", default=True, type=bool)
    args = parser.parse_args()
    results = messages.get_messages(**vars(args))
    pprint(results)
    print("💫")

if __name__ == "__main__":
    main()
