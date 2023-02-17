from datetime import datetime

def getSortData(request):
    
    date_value = request.form.get("dateTH")
    
    dateOrder = request.form.get("dateOrder")
    languagesOrder = request.form.get("languagesOrder")
    intervalOrder = request.form.get("intervalOrder")
    starsOrder = request.form.get("starsOrder")
    

    orderList = list([int(dateOrder), int(languagesOrder), int(intervalOrder), int(starsOrder)])
    
    if(date_value == "↕"):
        dateS = None
    elif(date_value == "↑"):
        dateS = "up"
    elif(date_value == "↓"):
        dateS= "down"
    else:
        dateS = None
        
    language_value = request.form.get("languageTH")
    if(language_value == "↕"):
        languageS = None
    elif(language_value == "↑"):
        languageS = "up"
    elif(language_value == "↓"):
        languageS= "down"
    else:
        languageS = None
        
    interval_value = request.form.get("intervalTH")
    if(interval_value == "↕"):
        intervalS = None
    elif(interval_value == "↑"):
        intervalS = "up"
    elif(interval_value == "↓"):
        intervalS= "down"
    else:
        intervalS = None
        
    stars_value = request.form.get("starsTH")
    if(stars_value == "↕"):
        starsS = None
    elif(stars_value == "↑"):
        starsS = "up"
    elif(stars_value == "↓"):
        starsS= "down"
    else:
        starsS = None
    
    return orderList, dateS, languageS, intervalS, starsS

def sort_items(notes, user, dateS, languageS, intervalS, starsS, orderList):
    from .models import User, Note
    
    dateOrder = orderList[0]
    languagesOrder = orderList[1]
    intervalOrder = orderList[2]
    starsOrder = orderList[3]
    
    orderList = sorted(orderList, key=lambda x: x, reverse=True)
    
    for order in orderList:
        if dateS != None and dateOrder == order:
            if(dateS == "up"):
                notes = sorted(notes, key=lambda x: x.date)
            else:
                notes = sorted(notes, key=lambda x: x.date, reverse=True)

        if languageS != None and languagesOrder == order:
            if(languageS == "up"):
                notes = sorted(notes, key=lambda x: x.language)
            else:
                notes = sorted(notes, key=lambda x: x.language, reverse=True)       
        
        if intervalS != None and intervalOrder == order:
            if(intervalS == "up"):
                notes = sorted(notes, key=lambda x: x.interval)
            else:
                notes = sorted(notes, key=lambda x: x.interval, reverse=True)     
        
        if starsS != None and starsOrder == order:
            if(starsS == "up"):
                notes = sorted(notes, key=lambda x: x.stars)
            else:
                notes = sorted(notes, key=lambda x: x.stars, reverse=True)
        
    return notes        

def filtrateNotes(notes, user, date1, date2, interval1, interval2, language1, stars1, stars2):
    from .models import User, Note
    selected_itemsDate = []
    selected_itemsInterval = []
    selected_itemsLanguage = []
    selected_itemsStars = []
    selected_items = []
    i = 0
    for note in notes:
        
        try:
            true_date = bool(datetime.strptime(date1, '%Y-%m-%d'))
            true_date = bool(datetime.strptime(date2, '%Y-%m-%d'))
        except:
            true_date = False

        if date1 != None and date2 != None and date1 and true_date:
            if note.date >= datetime.strptime(date1, '%Y-%m-%d').date() and note.date <= datetime.strptime(date2, '%Y-%m-%d').date():
                selected_itemsDate.append(i)
        else:
            selected_itemsDate.append(i)
                
        try:
            true_interval = bool(int(interval1))
            true_interval = bool(int(interval2))
        except:
            true_interval = False
            
        if interval1 != None and interval2 != None and true_interval:
            if note.interval >= int(interval1) and note.interval <= int(interval2):
                selected_itemsInterval.append(i)
        else:
            selected_itemsInterval.append(i)    
        
        if language1 != None:
            if note.language == language1:
                selected_itemsLanguage.append(i)
        else:
            selected_itemsLanguage.append(i)
        
        if stars1 != None and stars2 != None:
            if note.stars >= int(stars1) and note.stars <= int(stars2):
                selected_itemsStars.append(i)
        else:
            selected_itemsStars.append(i)
        i+=1
    
    
    selected_items = set(selected_itemsDate).intersection(selected_itemsInterval,selected_itemsLanguage,selected_itemsStars)
    notes = [note for i, note in enumerate(User.query.filter_by(id=user).first_or_404().notes) if i in selected_items]
    return notes
    
def getFormData(request):
    date1 = date2 = interval1 = interval2 = language1 = stars1 = stars2 = None
    IsChecked = False

    CheckDate = request.form.get("CheckDate")
    CheckInterval = request.form.get("CheckInterval")
    CheckLanguages = request.form.get("CheckLanguages")
    CheckStars = request.form.get("CheckStars")
    
    if(CheckDate):
        date1 = request.form.get("FiltrationDate1")
        date2 =  request.form.get("FiltrationDate2")
        IsChecked = True

    if(CheckInterval):
        interval1 = request.form.get("FiltrationInterval1")
        interval2 =  request.form.get("FiltrationInterval2")
        IsChecked = True

    if(CheckLanguages):
        language1 = request.form.get("FiltrationLanguages1")
        IsChecked = True

    if(CheckStars):
        stars1 = int(request.form.get("FiltrationStar1"))
        stars2 =  int(request.form.get("FiltrationStar2"))
        IsChecked = True

    return IsChecked, date1, date2, interval1, interval2, language1, stars1, stars2