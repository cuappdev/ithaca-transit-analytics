def parse_msg_json(msg):
    """This parses the json string from the message field."""
    start_index = msg.find('{')
    if start_index == 1:
        return ''
    return msg[start_index:]

def parse_key(msg_json, key):
    """This parses the value corresponding to [key] from the msg_json."""
    key_index = msg_json.find(key)
    if key_index == -1:
        return ''
    # Need to add 3 to reach the beginning of the value corresponding to this key
    # Ex) originName: 'Statler Hall'
    key_start_index = key_index + len(key) + 3
    key_end_index = msg_json.find("'", key_start_index)
    return msg_json[key_start_index: key_end_index]
