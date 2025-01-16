import json
from collections import Counter

def logParser(logfilePath="server.log") -> list:
    """ Parsing logfile and count events

    Args:
        logfilePath (str, optional): Where is logfile. Defaults to "server.log".

    Returns:
        list: return in correct syntax. IP {EVENT:count}
    """
    events = {}
    
    # READ
    with open(logfilePath, "r") as logfile:
        for line in logfile:
            # SPLIT in segments
            body = line.strip().split()
            ip, event = body[2], body[3]
            # If already exist return list else create key and give empty list. After that append to list.
            events.setdefault(ip, []).append(event)

    return {ip: dict(Counter(e)) for ip, e in events.items()}

def putInJSON(data, output="output.json") -> str:
    """Put any data in JSON file

    Args:
        data (_type_): any data.
        output (str, optional): where save json. Defaults to "output.json".

    Returns:
        str: Info about, data already saved. 
    """
    with open(output, "w") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    return f"Dati saglabāti '{output}' failā."

# RUN
events = logParser()
print(putInJSON(events))
