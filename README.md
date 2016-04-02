#os-kube-tesseract
<head>
<title>os-kube-tesseract :: A CLI based tool for transforming Openshift template files to Kubernetes file(s)</title>
<meta name='keywords' content='openshift, kubernetes, transform templates, tesseract, decompose template files, osaka'>
</head>
#
#
<h3>CLI tool for decomposing a Openshift template file into Services (svc), Pods (po) and ReplicationControllers (rc) file
</h3>

Watch this space to have a composition option where in multiple Kubernetes files can be stashed into a Openshift template file
****
 - Supports only Id field filtering while converting from OS Template to Kubernetes Service(s), Pod(s)and ReplicationController files

*****
Note : As of now my template files are mostly a simple wrapper around kubernetes files, so not much of attributes needs filtering
******
Built on using :
#
   - Python 3.5
   - PyYaml (latest version)
