from flask import Flask
import json
from secrets import randbits
from os import listdir,remove
app= Flask(__name__)

@app.route("/dispense_voter_info",methods=["GET"])
def dispense_voter_info():
    presidents = ["Emilio Aguinaldo","Jose Laurel"]
    senators = ["Manuel Roxas","Elpidio Quirino"]
    president = presidents[randbits(1)]
    senator = senators[randbits(1)] 
    private_key = "error"
    
    #Get all the keys
    all_keyfiles = listdir("data/voter_keys")
    
    if len(all_keyfiles) > 0:
        selected_keyfile = all_keyfiles[0]
        #Dispense a Key
        with open(f"data/voter_keys/{selected_keyfile}","r") as keyfile:
            keyfile_contents = keyfile.read()
            key_object = json.loads(keyfile_contents)
            private_key = key_object["private"]
        
        remove(f"data/voter_keys/{selected_keyfile}")

    voter_info = json.dumps({"private_key":private_key,"president":president,"senator":senator})

    #Log the Key Choices
    if private_key != "error":
        with open(f"data/voter_logs/{private_key[:15]}.json","w") as logfile:
            logfile.write(voter_info)

    return voter_info