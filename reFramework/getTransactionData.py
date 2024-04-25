from reFramework.getMaestro import *
import reFramework.globalVariable as globalVariables
import pandas as pd

def main():
    
    print("Getting transaction item")

    
    if globalVariables.isDatapoolEnabled:
        # logic for getting information from datapool
        datapool = maestro.get_datapool(label="yourdatapool")
    
        if datapool.has_next():
            globalVariables.transactionItem = datapool.next(task_id=execution.task_id)

    else:
        # Using dataframe as transactions | Edit excel path or change logic to get information based on your needs
        globalVariables.transactionItem = pd.read_excel(globalVariables.config.get("Excel_FilePath"))
        

if __name__ == '__main__':
    main()