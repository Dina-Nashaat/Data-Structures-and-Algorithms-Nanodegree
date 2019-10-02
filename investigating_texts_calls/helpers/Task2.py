
def addPhoneDuration(phone, duration, ds):
    if ds.get(phone):
        ds[phone] += int(duration)
    else:
        ds[phone] = int(duration)
    
def getPhoneWithMaxDuration(phones, ds):
    maxDurationPhone = ''
    for phone in phones:
        duration = ds.get(phone)
        maxDuration = ds.get(maxDurationPhone)
        if not maxDuration:
            maxDurationPhone = phone
        elif duration:
            maxDurationPhone = phone if duration > maxDuration else maxDurationPhone
    return maxDurationPhone
