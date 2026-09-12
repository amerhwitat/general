SUPPORTED_LOCALES={"ar","en","he","el","cop","fr","de","es"}
def parse_voice_command(locale:str, transcript:str)->dict:
    if locale.split("-")[0] not in SUPPORTED_LOCALES: raise ValueError("unsupported locale")
    text=transcript.strip()
    low=text.lower()
    intent="unknown"
    if any(x in low for x in ("create project","new project")): intent="create_project"
    elif any(x in low for x in ("create issue","create task","new task")): intent="create_work_item"
    elif "status" in low: intent="show_status"
    return {"locale":locale,"transcript":text,"intent":intent,"confidence":0.7 if intent!="unknown" else 0.2,"parameters":{}}
