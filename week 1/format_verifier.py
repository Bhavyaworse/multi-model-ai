def verify_batch_serial(serial_code):
    if len(serial_code) != 8:
        return False
        
    if not serial_code[:3].isalpha():
        return False
        
    if not serial_code[3:].isdigit():
        return False
        
    return True

def clean_label_spacing(raw_string):
    words = raw_string.split()
    joined_string = " ".join(words)
    return joined_string.lower()

print(verify_batch_serial("QA_X2026"))
print(verify_batch_serial("QAX19402"))

raw_log = "   UNIT   SPEED_ERROR   CRITICAL   "
print(clean_label_spacing(raw_log))
