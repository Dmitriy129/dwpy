import json
import sys

from src.scripts import script1, script1Mock, script2, script2Mock

mainConfig = json.load(open('./configs/main.json'))
run1Config = json.load(open('./configs/run1.json'))
run2Config = json.load(open('./configs/run2.json'))

availableScripts = {
    "script1": lambda: script1(mainConfig, run1Config),
    "script2": lambda: script2(mainConfig, run2Config),
}

mockedScripts = {
    "script1": lambda mockNumber: script1Mock(mainConfig, run1Config, mockNumber),
    "script2": lambda mockNumber: script2Mock(mainConfig, run2Config, mockNumber),
}

print(sys.argv)
scriptName = None
isMock = None
mockNumber = None


if(len(sys.argv) >= 2):
    scriptName = sys.argv[1]
    if(len(sys.argv) >= 3):
        isMock = sys.argv[2] == "mock"
        if(len(sys.argv) >= 4):
            mockNumber = sys.argv[3]

selectedScript = None

if(isMock):
    if scriptName in mockedScripts:
        selectedScript = mockedScripts[scriptName]
        if(mockNumber != None and mockNumber.isdigit()):
            def selectedScript(): return mockedScripts[scriptName](
                int(mockNumber))

        else:
            print('Need mock grade number')
    else:
        print(f'Script "{scriptName}" not available')
else:
    if scriptName in availableScripts:
        selectedScript = availableScripts[scriptName]
    else:
        print(f'Script "{scriptName}" not available')

print(f'Script "{scriptName}" starting...')
selectedScript()
print("done")
