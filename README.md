#os-kube-tesseract

CLI tool for decomposing a Openshift template file into Service (svc) and ReplicationController (rc) kubernetes file

Watch this space to have a composition option where in multiple Kubernetes files can be stashed into a Openshift template file


**********************************************************************************************************************************
Note : As of now my template files are mostly a simply wrapper around kubernetes files so not much of attributes needs filtering.
       Supports only Id field filtering while converting from OS Template to Kube svc and rc files
**********************************************************************************************************************************

Built on using :
    Python 3.5
    PyYaml <latest>