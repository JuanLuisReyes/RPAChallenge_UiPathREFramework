from reFramework.getMaestro import *
import reFramework.globalVariable as globalVariables

def main():
    print("Changing transaction status")
    


    if globalVariables.systemException:
        print("Transaction was set as Faulted")
        # Uncomment to mark this task as faulted on BotMaestro
        # maestro.error(task_id=execution.task_id, exception=error)

    else:
        print("Transaction was set as Success")
        globalVariables.systemException = ""
        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )
    
    globalVariables.transactionNumber = globalVariables.transactionNumber + 1

if __name__ == '__main__':
    main()