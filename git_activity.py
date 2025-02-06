import argparse
import json 
import urllib
import urllib.error
import urllib.request 


def parse_arguments():
    """
    Sets up the argument parser and defines the CLI arguments. 
    Return: parsed argument 
    """
    #set up argument parser 
    parser = argparse.ArgumentParser(description="A CLI tool to fetch recent activity of a github user and display it on the terminal")
    parser.add_argument("username", type= str, help= "Provide the github username")
    
    #parse argument 
    return parser.parse_args()

def fetch_github_activity(username):
    """Fetches the recent activity of a Github user from the github api 
    
    Parameters:
        username -> github username as a string 
    Return: a list of recent activities or error message
    """

    #initialize the github url 
    url = f"https://api.github.com/users/{username}/events"

    try:
        #Open the Url and fetch data 
        with urllib.request.urlopen(url) as response:

            #read and decode JSON data
            data = json.loads(response.read().decode("utf-8"))

            #check if data is empty for new user or no recent activities 
            if not data:
                return f"No recent activity found for user: {username}"
            
            return data #Returns raw JSON data for further processing 

    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Error: User '{username}' not found"
        elif e.code == 403:
            return "Error: API rate limit exceeded. Try again later"
        else: 
            return f"HTTP Error {e.code}: {e.reason}"
        
    except urllib.error.URLError:
        return f"Error: Unable to connect to the Github API. Check your internet connection."
        
def main():
    #Parsing CLI  arguments 
    args = parse_arguments()
    activity = fetch_github_activity(args.username)

    #print the fetched activity
    print(activity)



if __name__ == "__main__":
    main() 

