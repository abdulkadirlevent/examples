import os


def controllerCheckCMD(name):
    fileNameTemp = name + "Controller.php"
    print('Call CONTROLLERS')

    if not os.path.exists("Controllers"):
        os.makedirs("Controllers")
        print('Create Controllers Directory')

    if os.path.exists('Controllers/'+fileNameTemp):
        os.remove('Controllers/'+fileNameTemp)
        print('Remove Controllers/' + str(fileNameTemp))

    with open('templates/PHP/controller.php', 'rt', encoding='utf-8') as f:
        ResourceTemplate = f.read()

    data = {"_ModulName_": name, "_ModulNameLower_": name.lower()}
    with open('Controllers/'+fileNameTemp, 'wt', encoding='utf-8') as f:
        f.write(ResourceTemplate.format(**data))
        print('Create Controllers/' + str(fileNameTemp))
