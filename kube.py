#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
db = cgi.FieldStorage()
ch=db.getvalue("ch")
pname= db.getvalue("pname")
dname=db.getvalue("dname")
port= db.getvalue("port")
image= db.getvalue("image")
rno=db.getvalue("rno")
output="" 
if (("can" in ch))and(("you" in ch))and(("create" in ch)or("deploy" in ch)or("launch" in ch)or("run" in ch)) and (("deployment" in ch)):
   output = sp.getoutput("sudo kubectl create deployment {} --image={} --kubeconfig admin.conf" .format(dname,image))

elif (("hey" in ch)or("please" in ch))and(("show" in ch)or("display" in ch))and(("pods"in ch)or("pod" in ch)or("containers" in ch)):
   output = sp.getoutput("sudo kubectl get pod --kubeconfig admin.conf")

elif (("please"in ch)or("can" in ch)or("want" in ch))and(("expose"in ch))and(("deployment" in ch)or("pod" in ch)):
   output = sp.getoutput("sudo kubectl expose deployment {} --type=NodePort --port={} --kubeconfig admin.conf" .format(dname,port))

elif (("hey" in ch)or("i" in ch))and(("want" in ch)or("please" in ch))and(("scale"in ch)or("increase" in ch))and(("replica"in ch)or("container" in ch)or("pods" in ch)):
   output = sp.getoutput("sudo kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format(dname,rno))

elif(("please" in ch))and(("delete"in ch)or("remove"in ch))and(("deployment"in ch)):
   output = sp.getoutput("sudo kubectl delete deployment {} --kubeconfig admin.conf".format(dname))

elif (("i" in ch)and("want" in ch))and(("remove" in ch)or("delete"in ch))and(("env" in ch)or("envirnoment" in ch)or("deployments" in ch)):
   output = sp.getoutput("sudo kubectl delete all --all --kubeconfig admin.conf")

elif (("describe"in ch)or("show"in ch)or("display" in ch))and(("info"in ch)or("information" in ch))and(("pod" in ch)):
   output = sp.getoutput("sudo kubectl describe pod {} --kubeconfig admin.conf".format(pname))

elif (("hey" in ch)or("please" in ch))and(("create"in ch)or("run"in ch))and(("pod" in ch)):
   output = sp.getoutput("sudo kubectl run {} --image={} --kubeconfig admin.conf".format(pname,image))

elif (("please" in ch))and(("delete"in ch)or("remove"in ch))and(("pod"in ch)):
   output = sp.getoutput("sudo kubectl delete pod {} --kubeconfig admin.conf".format(pname))

elif (("show" in ch)or("display"in ch)or("list"in ch))and(("deployments"in ch)):
   output = sp.getoutput("sudo kubectl get deployments --kubeconfig admin.conf")

elif (("show" in ch)or("display"in ch)or("list"in ch))and(("services"in ch)):
   output = sp.getoutput("sudo kubectl get svc --kubeconfig admin.conf")


else:
   output = "Something went Wrong..."
print("""<style>
   body{
       background-color:90EE90;
      text-align:center;
       justify-content:center;
     }
      pre{
        font-size: 20px;
        color:DC143C;
      font-weight: bold;
      padding -top:0px
}
h1{
color : DarkGreen;
padding-bottom:0px;
}
</style>""")
print("""
<body>
<pre>
<h1 style = "">****************************</h1>
{}
</pre>
</body>
""".format(output))
 
