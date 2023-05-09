import os


def modelsCheckCMD(name):
    fileNameTemp = name + ".php"
    print('Call MODELS')

    if not os.path.exists("Models"):
        os.makedirs("Models")
        print('Create Models Directory')

    if os.path.exists('Models/'+fileNameTemp):
        os.remove('Models/'+fileNameTemp)
        print('Remove Models/' + str(fileNameTemp))

    with open('templates/PHP/model.php', 'rt', encoding='utf-8') as f:
        ResourceTemplate = f.read()

    data = {"_ModulName_": name, "_ModulNameLower_": name.lower()}
    with open('Models/'+fileNameTemp, 'wt', encoding='utf-8') as f:
        f.write(ResourceTemplate.format(**data))
        print('Create Models/' + str(fileNameTemp))
