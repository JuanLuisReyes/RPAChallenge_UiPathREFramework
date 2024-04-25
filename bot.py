"""
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)
"""
import reFramework.globalVariable as globalVariables
import reFramework.Initialization as init
import reFramework.getTransactionData as getTransactionData
import reFramework.process as process
import reFramework.endProcess as endProcess
import reFramework.setTransactionStatus as setTransactionStatus
from reFramework.alerts import *
from reFramework.getMaestro import *

def main():
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    init.main()
    try:
        # Missing logic for stopping the process
        getTransactionData.main()
        while globalVariables.transactionNumber < len(globalVariables.transactionItem):
            try:
                process.main()
                setTransactionStatus.main()
            except Exception as error:
                setTransactionStatus.main()
                print(error)
    except:
        print(globalVariables.config.get("LogMessage_GetTransactionDataError").ToString + globalVariables.TransactionNumber.ToString+ ". " + Exception.Message + " at Source: " + Exception.Source)
        globalVariables.transactionItem = maestro

    endProcess.main()


if __name__ == '__main__':
    main()
