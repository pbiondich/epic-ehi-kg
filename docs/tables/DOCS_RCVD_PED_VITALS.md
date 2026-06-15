# DOCS_RCVD_PED_VITALS

> Contains pediatric vitals (aka birth history) received through external documents and stored in DXR.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PED_VITAL_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the pediatric vital. |
| 6 | `PED_VITAL_SOURCE_VALUE` | VARCHAR |  | This item stores the source value of a received pediatric vital before it is converted. |
| 7 | `PED_VITAL_SOURCE_UNIT` | VARCHAR |  | This item stores the source unit of a received pediatric vital before it is converted. |
| 8 | `PED_VITAL_BIRTH_LENGTH_CM` | NUMERIC |  | This item stores the patient birth length (unit is cm). |
| 9 | `PED_VITAL_BIRTH_WEIGHT_KG` | NUMERIC |  | This item stores the patient weight when discharged after birth (unit is kg). |
| 10 | `PED_VITAL_BIRTH_HC_IN_CM` | NUMERIC |  | This item stores the patient head circumference at birth (unit is cm). |
| 11 | `PED_VITAL_APGAR_1_C_NAME` | VARCHAR | org | This item stores the patient APGAR 1 score (0-10). |
| 12 | `PED_VITAL_APGAR_5_C_NAME` | VARCHAR |  | This item stores the patient APGAR 5 score (0-10). |
| 13 | `PED_VITAL_APGAR_10_C_NAME` | VARCHAR |  | This item stores the patient APGAR 10 score (0-10). |
| 14 | `PED_VITAL_GEST_AGE` | INTEGER |  | This item stores the patient gestation age at birth (unit is days). |
| 15 | `PED_VITAL_NOURISH_HAD_BM_YN` | VARCHAR |  | This item stores the patient was nourished with breast milk at birth. |
| 16 | `PED_VITAL_NRSH_MTHD_HAD_FRM_YN` | VARCHAR |  | This item stores the patient was nourished with formula at birth. |
| 17 | `PED_VITAL_DELIV_METHOD_C_NAME` | VARCHAR | org | This item stores the patient delivery method. |
| 18 | `PED_VITAL_HOSP_DAYS` | NUMERIC |  | This item stores the duration of the patient stay at birth (unit is days). |
| 19 | `PED_VITAL_DISCHARGE_WEIGHT_KG` | NUMERIC |  | This item stores the patient weight when discharged after birth (unit is kg). |
| 20 | `PED_VITAL_MULT_BIRTH_TOTAL_NUM` | INTEGER |  | This item holds the total number of births during the mother's labor and delivery of this newborn patient. |
| 21 | `PED_VITAL_MULTI_BIRTH_ORDER` | INTEGER |  | For multiple births, the place in the birth order of the current newborn patient. |
| 22 | `PED_VITAL_SOURCE_DXR_CSN` | NUMERIC |  | This item will store the contact serial number of the DXR record that owns the instance of this ped vital. |
| 23 | `PED_VITAL_LAST_UPD_DTTM` | DATETIME (UTC) |  | This item stores the instant the vitals were most recently updated. |
| 24 | `PAT_DEL_UTC_DTTM` | DATETIME (UTC) |  | Patient delivery instant (UTC). |
| 25 | `PED_VITAL_NOUR_METH_C_NAME` | VARCHAR | org | This item stores the nourishment method for the patient. |
| 26 | `PED_VITAL_LABOR_DURATION` | VARCHAR |  | Stores the duration of labor. |
| 27 | `PED_VITAL_HOSP_NAME` | VARCHAR |  | This item stores the name of the hospital where the patient was born. |
| 28 | `PED_VITAL_HOSP_LOC` | VARCHAR |  | This item stores the location of the hospital where born. |
| 29 | `PED_VITAL_COMMENT` | VARCHAR |  | This item stores the comments for a patient's birth history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

