import OS_Calls
import bug.BugRobot as BugRobot
import bug.Workspace as Workspace
import kinematics.Manipulator as Manipulator
import os.path


def main():

    shouldSavePlots = True
    basePlotDir = 'figures'

    OS_Calls.clear_screen()

    simType = 'bug'
    simRunner(shouldSavePlots, basePlotDir, simType)

    simType = 'manipulator'
    simRunner(shouldSavePlots, basePlotDir, simType)


def simRunner(shouldSavePlots, basePlotDir, simType):

    (configNames, configFileNames) = getConfigPaths(simType)

    for (file, configName) in zip(configFileNames, configNames):
        print('===============================')
        print(configName)
        print('===============================')
        baseSaveFName = os.path.join(basePlotDir, configName)

        if simType == 'bug':
            runBugAlgorithmComparison(file, shouldSavePlots,
                                      baseSaveFName)
        elif simType == 'manipulator':
            runManipulatorComparison(file, shouldSavePlots,
                                     baseSaveFName)


def runBugAlgorithmComparison(configFileName, shouldSavePlots, baseSaveFName):
    currWorkspace = Workspace.Workspace(configFileName=configFileName,
                                        shouldSavePlots=shouldSavePlots,
                                        baseSaveFName=baseSaveFName)

    algStr = 'bug1'
    BugRobot.runRobot(configFileName=configFileName,
                      currWorkspace=currWorkspace,
                      algorithmStr=algStr)

    algStr = 'bug2'
    BugRobot.runRobot(configFileName=configFileName,
                      currWorkspace=currWorkspace,
                      algorithmStr=algStr)


def runManipulatorComparison(configFileName, shouldSavePlots, baseSaveFName):
    Manipulator.runManipulator(configFileName=configFileName,
                               shouldSavePlots=shouldSavePlots,
                               baseSaveFName=baseSaveFName)


def getConfigPaths(simType):

    if simType == 'bug':
        configNames = ['scenario1', 'scenario2']
    elif simType == 'manipulator':
        configNames = ['scenario1']

    fullConfigNames = list(map(lambda x: simType + '_' + x, configNames))

    configDir = 'config'
    fType = '.yaml'
    configFileNames = [os.path.join(configDir, fName) + fType
                       for fName in fullConfigNames]

    return (fullConfigNames, configFileNames)


if __name__ == '__main__':
    main()
