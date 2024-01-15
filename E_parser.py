from parserr import resume_to_structured
import json

OPENAI_API_KEY = "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"
parser = resume_to_structured(OPENAI_API_KEY)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(parser.ending_process("James_Hoffmann.pdf")))
    

