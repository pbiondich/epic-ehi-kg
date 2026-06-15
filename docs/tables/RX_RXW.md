# RX_RXW

> This table contains no add single response data for ambulatory pharmacy work requests. Each work request is associated with a set of fill requests. A fill request is a contact on the order record which contains information about the specific dispense of the attached order. The patient, the order, and the order DAT is stored on the order record of the work request, which also links the work request to its associated fill request. This value lives in table RX_RXW_ORDER_INFO. Each work request is also linked to a patient, for which the work request was originally created. Pickup priority and contact information is also stored in this record to assist in prescription filling and dispensing.

**Primary key:** `RECORD_ID`  
**Columns:** 45  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | Work request ID. This is the primary key for the work request table. |
| 2 | `MASTER_PATIENT_ID` | VARCHAR |  | The unique identifier for the main patient in a work request. Additional patients attached to the work request are reported in the RXW_ORDER_INFO table in association with the specific fill request for that patient. This column can be linked to the PATIENT table in order to report on any patient noadd information. |
| 3 | `PLANNED_PICKUP_INST` | DATETIME (UTC) |  | The date and time the patient plans to pick up the fills associated with this work request. Used in conjunction with the fill priority to determine the overall priority of the work request for filling. |
| 4 | `WAITING_SINCE_DTTM` | DATETIME (UTC) |  | The instant when the work request was marked as waiting. |
| 5 | `DELIVERY_METHOD_C_NAME` | VARCHAR | org | The prescription delivery method for the work request. Pickup and mail order are two examples of this. |
| 6 | `DELIVERY_HOUSE_NUM` | VARCHAR |  | The house number of the prescription delivery address. |
| 7 | `DELIVERY_CITY` | VARCHAR |  | The city of the prescription delivery address. |
| 8 | `DELIVERY_STATE_C_NAME` | VARCHAR | org | The state of the prescription delivery address. |
| 9 | `DELIVERY_ZIP` | VARCHAR |  | The ZIP code of the prescription delivery address. |
| 10 | `DELIVERY_DIST_C_NAME` | VARCHAR | org | The district of the prescription delivery address. |
| 11 | `DELIVERY_COUNTY_C_NAME` | VARCHAR | org | The county of the prescription delivery address. |
| 12 | `DELIVERY_COUNTRY_C_NAME` | VARCHAR | org | The country of the prescription delivery address. |
| 13 | `DELIVERY_ADDRTYP_C_NAME` | VARCHAR |  | The type of address from the patient that is used for the prescription delivery address on the work request. For example, the patient's home address will commonly be used as the ship to address. |
| 14 | `RX_PMT_GUARANTOR_ID` | NUMERIC |  | If Professional Billing integration is enabled, this contains the guarantor account associated with the sale of merchandise products. |
| 15 | `DELIVERY_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column contains the CSN of the patient encounter associated with a room delivery work request. |
| 16 | `DELIVERY_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 17 | `DELIVERY_ROOM_RECORD_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 18 | `DELIVERY_EXAM_ROOM_NUMBER` | VARCHAR |  | The column contains the free-text room number that represents the exam room the patient occupied at the time of delivery of room delivery work request. |
| 19 | `DELIVERY_BED_ID` | VARCHAR |  | This column contains the ADT bed (BED) record that represents the physical bed the patient occupied at the time of delivery of a room delivery work request. |
| 20 | `DELIVERY_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 21 | `CREATION_USER_ID` | VARCHAR |  | The user that created the work request. |
| 22 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `DELIVERY_ADDR_NAME` | VARCHAR |  | Stores the name used as part of the shipping address when delivering this medication. |
| 24 | `RETURN_ADDR_NAME` | VARCHAR |  | Stores the name that gets displayed on the return address when shipping prescriptions. |
| 25 | `RETURN_HOUSE_NUM` | VARCHAR |  | The house number to put on the return address when shipping prescriptions. |
| 26 | `RETURN_CITY` | VARCHAR |  | The city part of the return address when shipping prescriptions. |
| 27 | `RETURN_STATE_C_NAME` | VARCHAR |  | The state part of the return address when shipping prescriptions. |
| 28 | `RETURN_ZIP` | VARCHAR |  | The zip code for the return address when shipping prescriptions. |
| 29 | `RETURN_DISTRICT_C_NAME` | VARCHAR |  | The district for the return address when shipping prescriptions. |
| 30 | `RETURN_COUNTY_C_NAME` | VARCHAR |  | The county for the return address when shipping prescriptions. |
| 31 | `RETURN_COUNTRY_C_NAME` | VARCHAR |  | The country for the return address when shipping prescriptions. |
| 32 | `PACKAGE_WEIGHT` | NUMERIC |  | The weight of the package when shipping prescriptions to patients. The weight is always stored in grams and converted to appropriate units. |
| 33 | `SHIP_TOTAL_COST` | NUMERIC |  | Stores the total cost of goods in the shipment. Represents the retail price of the goods that it would cost to replace the shipment were it to be lost. |
| 34 | `SHIP_PCKG_TYPE_C_NAME` | VARCHAR | org | Stores the type of package used for delivering the shipment. |
| 35 | `SHIP_EXTERNAL_IDENTIFIER` | VARCHAR |  | Stores the external Identifier for this shipment so the external system can give us updates at a later point. |
| 36 | `SHIP_DELIV_DATE` | DATETIME |  | Contains the estimated delivery date for the shipment to arrive. |
| 37 | `SHIP_DELIV_COST` | NUMERIC |  | Stores the cost of shipping for this package. |
| 38 | `SHIP_STATUS_C_NAME` | VARCHAR |  | Contains the status of the shipment we are sending. |
| 39 | `SHIPMENT_WORKFLOW_C_NAME` | VARCHAR |  | Stores the workflow that started this shipment. This is used internally to drive what actions to take when the shipment is completed. |
| 40 | `DELIVERY_TIMING_C_NAME` | VARCHAR |  | Describes when the work request should arrive at the patient if the delivery method is similar to mail or courier. |
| 41 | `RX_DELIVERY_PHONE` | VARCHAR |  | Contains a phone number to call/text to contact the person receiving a shipment. |
| 42 | `RX_DELIVERY_EMAIL` | VARCHAR |  | Stores the email that should be used to contact the person receiving a shipment. |
| 43 | `RETURN_ADDR_PHONE` | VARCHAR |  | The phone number added to the return address for a shipping label. |
| 44 | `RX_DELIVERY_DATE` | DATETIME |  | The date when the shipment is to arrive at the patient's address. |
| 45 | `OTHER_AMOUNT_TOTAL` | NUMERIC |  | This item contains the total amount due for other items in this dispense transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DELIVERY_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

