# def test_pycades_connection():
#     try:
#         # Пытаемся открыть хранилище сертификатов "Личное"
#         store = pycades.Store()
#         store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CADESCOM_MY_STORE, pycades.CERT_OPEN_EXISTING)
#
#         certs_count = store.Certificates.Count
#         print(f"Успех! Хранилище открыто. Сертификатов найдено: {certs_count}")
#
#         # Выведем информацию о первом найденном (если есть)
#         if certs_count > 0:
#             cert = store.Certificates.Item(1)
#             print(f"Пример сертификата: {cert.SubjectName}")
#             print(f"Отпечаток: {cert.Thumbprint}")
#
#         store.Close()
#
#     except Exception as e:
#         print(f"Что-то пошло не так: {e}")
#         print("Возможные причины: нет установленных сертификатов в хранилище 'Личное' или КриптоПро не запущен.")
#
#
# if __name__ == "__main__":
#     test_pycades_connection()