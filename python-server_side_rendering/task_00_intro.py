def generate_invitations(template, attendees):
    
    # Vérifier les types
    if not isinstance(template, str):
        print(f"Error: template is not a string (got {type(template).__name__})")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees is not a list of dictionaries (got {type(attendees).__name__})")
        return

    # Vérifier template et liste vide
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Générer les fichiers
    for index, attendee in enumerate(attendees, start=1):
        content = template
        content = content.replace("{name}", attendee.get("name") or "N/A")
        content = content.replace("{event_title}", attendee.get("event_title") or "N/A")
        content = content.replace("{event_date}", attendee.get("event_date") or "N/A")
        content = content.replace("{event_location}", attendee.get("event_location") or "N/A")

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
            print(f"File '{filename}' generated successfully.")
        except Exception as e:
            print(f"Error writing file '{filename}': {e}")