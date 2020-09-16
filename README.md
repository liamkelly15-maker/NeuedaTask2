# NeuedaTask2
Planned Steps

1.Place python script files in GiThub
   python script (encryptfile) will convert json to xml and encrypt 
   python script (decryptfile) will decrypt the xml 

2.Create jenkins Job which will pull the Scripts from Github Repo
  and Run the docker commands to create Container A

3.Push the Image file to Docker Hub,Using Jenkins Plugin [ CloudBees Docker Build and publish plugin]

4.Creae a Second jenkins job that will Open the Docker Quickstart Terminal and run the Docker Shell Commands to download an image file and
then it create a container B

5.Open the Container B and Run the Second Script that will Decrypt to XMl files.
