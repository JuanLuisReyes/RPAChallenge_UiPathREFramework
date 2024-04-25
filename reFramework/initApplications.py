from reFramework.getMaestro import *
import reFramework.globalVariable as globalVariables
import time

def main():
    
    print("Opening applications...")

    try:
        # Initializing browser configuration
        print("Opening 'RPA Challenge' website")
        rpaChallenge_URL = globalVariables.config.get("RPAChallenge_URL")
        bot.browse(rpaChallenge_URL)

        time.sleep(5)

    except Exception as Error:
        print(Error)

    print("Applications initialized!")

if __name__ == '__main__':
    main()