from django.shortcuts import render

from joblib import load
model = load('./models/model.joblib')

def predictor(request):
    if request.method == 'POST':
        surgery = request.POST['surgery']
        Age = request.POST['Age']
        Rectal_Temperature = request.POST['Rectal_Temperature']
        Pulse = request.POST['Pulse']
        Respiratory_Rate = request.POST['Respiratory_Rate']
        Temperature_Of_Extremities = request.POST['Temperature_Of_Extremities']
        Peripheral_Pulse = request.POST['Peripheral_Pulse']
        Mucous_Membrane = request.POST['Mucous_Membrane']
        Capillary_Refill_Time = request.POST['Capillary_Refill_Time']
        Pain = request.POST['Pain']
        Peristalsis= request.POST['Peristalsis']
        Abdominal_Distention= request.POST['Abdominal_Distention']
        Nasogastric_Tube= request.POST['Nasogastric_Tube']
        Nasogastric_Reflux= request.POST['Nasogastric_Reflux']
        Nasogastric_Reflux_Ph = request.POST['Nasogastric_Reflux_Ph']
        Rectal_Exam_Feces = request.POST['Rectal_Exam_Feces']
        Abdomen = request.POST['Abdomen']
        Packed_Cell_Volume = request.POST['Packed_Cell_Volume']
        Total_Protein = request.POST['Total_Protein']
        Abdomen_Appearance = request.POST['Abdomen_Appearance']
        Abdomen_Protein = request.POST['Abdomen_Protein']
        Surgical_Lesion = request.POST['Surgical_Lesion']
        Lesion_1 = request.POST['Lesion_1']
        Lesion_2 = request.POST['Lesion_2']
        Lesion_3 = request.POST['Lesion_3']
        CP_Data = request.POST['CP_Data']

        y_pred = model.predict([[surgery,
                             Age,Rectal_Temperature,Pulse,Respiratory_Rate,Temperature_Of_Extremities,Peripheral_Pulse,Mucous_Membrane,
                                Capillary_Refill_Time,Pain,Peristalsis,Abdominal_Distention,Nasogastric_Tube,
                                Nasogastric_Reflux,Nasogastric_Reflux_Ph,Rectal_Exam_Feces,Abdomen,Packed_Cell_Volume,
                                Total_Protein,Abdomen_Appearance,Abdomen_Protein,Surgical_Lesion,Lesion_1,
                                Lesion_2,Lesion_3,CP_Data
                                ]])
        if y_pred == 0:
            y_pred = 'The horse is likely to Died'
        elif y_pred == 1:
            y_pred = 'The horse is likely to survive'
        else:
            y_pred='The horse is likely to euthanized'
    
        return render(request, 'index.html',{'submit': y_pred})

    return render(request, 'index.html')    