import reFramework.initAllSettings as initSettings
import reFramework.initApplications as initApplications
import reFramework.endProcess as endProcess

def main():
    try:
        # Initializing setting and applications
        initSettings.main()
        initApplications.main()
    except:
        endProcess.main()

if __name__ == '__main__':
    main()

