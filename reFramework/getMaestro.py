# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from botcity.web import WebBot, Browser, By
import reFramework.globalVariable as globalVariables

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
# Runner passes the server url, the id of the task being executed,
# the access token and the parameters that this task receives (when applicable).

maestro = BotMaestroSDK.from_sys_args()
## Fetch the BotExecution with details from the task, including parameters
execution = maestro.get_execution()

bot = WebBot()
bot.headless = False
bot.browser = Browser.CHROME
webDriver_filePath = r"resources\chromedriver.exe"
bot.driver_path = webDriver_filePath