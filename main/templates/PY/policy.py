import os


def policiesCheckCMD(name):
    fileNameTemp = name + "Policy.php"
    print('Call POLICIES')

    if not os.path.exists("Policies"):
        os.makedirs("Policies")
        print('Create Policies Directory')

    if os.path.exists('Policies/' + fileNameTemp):
        os.remove('Policies/' + fileNameTemp)
        print('Remove Policies/' + str(fileNameTemp))

    with open('templates/PHP/policy.php', 'rt', encoding='utf-8') as f:
        ResourceTemplate = f.read()

    data = {"_ModulName_": name, "_ModulNameLower_": name.lower()}
    with open('Policies/' + fileNameTemp, 'wt', encoding='utf-8') as f:
        f.write(ResourceTemplate.format(**data))
        print('Create Policies/' + str(fileNameTemp))
