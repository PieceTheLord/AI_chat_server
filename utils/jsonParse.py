import json

def format_str_to_json(string: str) -> object:
  """Convert a json string into the json object."""
  try:
    res = json.loads(string)
    return res
  except Exception as e:
    return "Error in formatting str into json", e