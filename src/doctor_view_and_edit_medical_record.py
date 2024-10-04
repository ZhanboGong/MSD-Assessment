# 初始化病历的空列表
medical_records = []

# 查看病历功能
def view_medical_record(patient_name):
    found = False
    for record in medical_records:
        if record['patient_name'] == patient_name:
            print(f"Record ID: {record['record_id']}\nDoctor: {record['doctor_name']}\nPatient: {record['patient_name']}\nDiagnosis: {record['diagnosis']}\nTreatment: {record['treatment']}")
            found = True
    if not found:
        print(f"No medical record found for patient {patient_name}.")

# 编辑病历功能
def edit_medical_record(record_id, new_diagnosis=None, new_treatment=None):
    for record in medical_records:
        if record['record_id'] == record_id:
            if new_diagnosis:
                record['diagnosis'] = new_diagnosis
            if new_treatment:
                record['treatment'] = new_treatment
            print(f"Medical record {record_id} updated.")
            return
    print(f"Medical record with ID {record_id} not found.")
