medical_records = []

# 创建病历功能
def create_medical_record(doctor_name, patient_name, diagnosis, treatment):
    # 创建病历
    record_id = len(medical_records) + 1
    record = {
        "record_id": record_id,
        "doctor_name": doctor_name,
        "patient_name": patient_name,
        "diagnosis": diagnosis,
        "treatment": treatment
    }
    medical_records.append(record)
    print(f"Medical record for patient {patient_name} created by Doctor {doctor_name}.")