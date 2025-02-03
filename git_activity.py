import argparse
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

def main():
    #Parsing CLI  arguments 
    args = parse_arguments()

    print(f"GitHub Username: {args.username}")

if __name__ == "__main__":
    main() 

