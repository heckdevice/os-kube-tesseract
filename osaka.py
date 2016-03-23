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
                  osTemplateFilename+'*'*50)
            output = decompose(osTemplateFilename)
            print("%s template is decomposed into %s kubernetes files" %
                  (osTemplateFilename, output))


def decompose(osTemplateFilename):
    output = []
    with open(osTemplateFilename, 'r') as f:
        for data in yaml.load_all(f, Loader=yaml.Loader):
            # print(data)
            for key, value in data.items():
                #print("key %s value %s" % (key, value))
                # print(filename)
                if key == 'objects':
                    for obj in value:
                        # print(obj)
                        filename = 'kube-' + data['metadata']['name']
                        outValue = {}
                        for objkey, objval in obj.items():
                            if objkey == 'kind' and objval == 'Service':
                                filename = filename + '-svc.yaml'
                            elif objkey == 'kind' and objval == 'ReplicationController':
                                filename = filename + '-rc.yaml'
                            if objkey == 'id':
                                continue
                            else:
                                # print("Adding key val %s , %s" %
                                #       (objkey, objval))
                                outValue[objkey] = objval
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
