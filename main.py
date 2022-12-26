from api import APIHandler
from credentials import auth

def main():

    api = APIHandler(auth)
    api.validate_token()
    print(api.access_token)

if __name__ == "__main__":
    # Initial commit
    main()
