# Import for integration with BotCity Maestro SDK
import reFramework.globalVariable as globalVariables
import pandas as pd

def main():

    print("Initializing applications...")

    try:
        # If first run, read local configuration file
        df_settingAndConstants = pd.DataFrame()
        config = globalVariables.config
        if not config:
            print("Initializing settings")

            for sheet in globalVariables.configSheetsName:
                df_settingAndConstants = pd.read_excel(globalVariables.configFilePath, sheet)
                for index, setting in df_settingAndConstants.iterrows():
                    config.update({setting['Name']:setting['Value']})

    except:
        print("Exception ocurred while initializing process")

    print("Applications initialized correctly")

if __name__ == '__main__':
    main()