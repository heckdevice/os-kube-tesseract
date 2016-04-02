#!./venv/bin/python
import yaml
import sys
import getopt

__author__ = "shailesh.pant@gmail.com"


def parseCLI(argv):
    osTemplateFilename = ''
    try:
        opts, args = getopt.getopt(argv, "hd:", ["osfile="])
    except getopt.GetoptError:
        print('usage : osaka.py -d <openshift_template_file>')
        sys.exit(2)
    if len(opts) == 0:
        print('usage : osaka.py -d <openshift_template_file>')

    for opt, arg in opts:
        if opt == '-h':
            print('usage : osaka.py -d <openshift_template_file>')
            sys.exit()
        elif opt in ("-d", "--osfile"):
            osTemplateFilename = arg
            print('*' * 50 + "Decomposing Openshift Template file %s" %
                  osTemplateFilename + '*' * 50)
            output = decomposeRedux(osTemplateFilename)
            print("%s template is decomposed into %s kubernetes files" %
                  (osTemplateFilename, output))


def decomposeRedux(osTemplateFilename):
    output = []
    with open(osTemplateFilename, 'r') as f:
        for data in yaml.load_all(f, Loader=yaml.Loader):
            objVals = data['objects']
            for obj in objVals:
                filename = 'kube-' + data['metadata']['name']
                fileType = None
                outValue = {}
                for objkey, objval in obj.items():
                    if objkey == 'kind' and objval == 'Service':
                        fileType = 'svc'
                        outValue[objkey] = objval
                    elif objkey == 'kind' and objval == 'ReplicationController':
                        fileType = 'rc'
                        outValue[objkey] = objval
                    elif objkey == 'kind' and objval == 'Pod':
                        fileType = 'po'
                        outValue[objkey] = objval
                    elif objkey == 'id':
                        filename = filename + '-' + objval
                    else:
                        outValue[objkey] = objval
                filename = filename + '-' + fileType + '.yaml'
                with open(filename, 'w') as outfile:
                    outfile.write(
                        yaml.dump(outValue, default_flow_style=False))
                    output.append(filename)
    return output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage : osaka.py -d <openshift_template_file>")
        exit(0)
    parseCLI(sys.argv[1:])
