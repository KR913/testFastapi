# testFastapi

bosch_auth=('FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\\697c5136-e719-40a1-a52a-11cd330bb5db', '13513f28-934d-4374-9f23-98e1e6aa6968')
bosch_software_url = 'https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules/'
curl "https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules" -u "FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\697c5136-e719-40a1-a52a-11cd330bb5db:13513f28-934d-4374-9f23-98e1e6aa6968" -i -X POST -H "Content-Type: application/json;charset=UTF-8" -d "[ { \"vendor\" : \"Example Ltd.\",\"name\" : \"myOs\",\"description\" : \"First version of MyOS.\",\"type\" : \"os\",\"version\" : \"1.0\" } ]"
