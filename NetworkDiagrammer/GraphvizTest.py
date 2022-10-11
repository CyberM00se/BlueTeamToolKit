from diagrams import Diagram, Cluster, Edge
from diagrams.digitalocean.compute import Droplet
from diagrams.digitalocean.database import DbaasPrimary
from diagrams.elastic.elasticsearch import Logstash

with Diagram("My Diagram: Droplets", show=False, filename="my-diagram", direction="LR"):
    with Cluster("DigitalOcean"):
        droplet1 = Droplet("My first droplet")
        droplet2 = Droplet("My second droplet")
        droplet2 = Droplet("YO YO ITS SCANLAN")

    db = DbaasPrimary("My database")
    
    logstash = Logstash("Logstash service")
    
    [droplet1, droplet2] >> db >> [droplet1, droplet2]
    [droplet1, droplet2, db] >> Edge(color="firebrick", style="dashed") >> logstash