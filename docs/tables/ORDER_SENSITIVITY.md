# ORDER_SENSITIVITY

> The ORDER_SENSITIVITY table contains information on the sensitivity of orders placed in clinical system.

**Primary key:** `ORDER_PROC_ID`, `ORD_DATE_REAL`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number of the sensitivity data recorded within each procedure record. |
| 3 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 4 | `ORD_END_DATE_REAL` | FLOAT |  | This is a numeric representation of the end date for each order in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `RESULT_DATE` | DATETIME |  | The date the technician ran the tests for each order |
| 7 | `ORGANISM_ID` | NUMERIC | FK→ | The ID of the organism that was cultured and tested for susceptibility. |
| 8 | `ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |
| 9 | `ANTIBIOTIC_C_NAME` | VARCHAR | org | The category value of each antibiotic that was tested on each organism culture. |
| 10 | `SUSCEPT_C_NAME` | VARCHAR | org | The category value associated with the susceptibility of the organism culture to the antibiotic. These correspond to standard HL7 susceptibilities: 1-Resistant, 2-Moderately sensitive, 3-Intermediate, and so on. |
| 11 | `SENSITIVITY_VALUE` | VARCHAR |  | This item is not populated by the EMR. It may be populated with the sensitivity value from an interface. |
| 12 | `LAB_STATUS_C_NAME` | VARCHAR |  | The category value associated with the status of each result, such as 1-In Progress, 2-Preliminary, 3-Final, 4-Edited. |
| 13 | `SENS_ORGANISM_SID` | VARCHAR |  | This item will hold the sub ids for each organism helping the application to create a unique data structure for the display of microbiology results. The unique data structure will use this item in conjunction with organism name or id as one of the key subscripts thus preventing errors with the display. E.g. Salmonella typhi (Strain Ty2) and Salmonella typhi (Strain CT18) may have the same name (Salmonella typhi) but will have different sub ids depending on the external system sending the data. In order to display both of the above, a unique sub id is required. |
| 14 | `SENS_COM_ORG_RES_ID` | NUMERIC |  | This item stores the RES (Results master file) record id which stores comments related to the organisms. The item is related to the organisms stored in item ORD 2220 and the line number of this item will match directly to the organism line number. |
| 15 | `SENS_OBS_INST_TM` | DATETIME (Local) |  | Timestamp to track per micro result component when it was collected/observed. |
| 16 | `SENS_ANL_INST_TM` | DATETIME (Local) |  | Timestamp to track per micro result component when it was analyzed in lab. |
| 17 | `SENS_START_LN` | INTEGER |  | This columns contains the start line of ORD-2290 (extracted in SENS_LONG_VAL) where the long sensitivity value will begin. |
| 18 | `SENS_END_LN` | INTEGER |  | This column contains the end line of ORD-2290(extracted in SENS_LONG_VAL) where the long sensitivity value will terminate. |
| 19 | `SENS_COMM` | VARCHAR |  | This column contains a short sensitivity note for ORD-2290 (extracted in SENS_LONG_VAL). |
| 20 | `SENS_COMM_START_LN` | INTEGER |  | This column contains the start line in ORD-2290(extracted in SENS_LONG_VAL) of a long sensitivity comment. |
| 21 | `SENS_COMM_END_LN` | INTEGER |  | This column contains the end line in ORD-2290(extracted in SENS_LONG_VAL) of a long sensitivity comment. |
| 22 | `SENSITIVITY_UNITS` | VARCHAR |  | Indicates units applied for antibiotics on a sensitivity test. |
| 23 | `SENS_STATUS_C_NAME` | VARCHAR |  | Indicates the status of a sensitivity test. |
| 24 | `ANTIBIO_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 25 | `METHOD_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 26 | `SENS_REF_RANGE` | VARCHAR |  | Indicates the reference range for antibiotics on a sensitivity test. |
| 27 | `HIDE_ANTIBIOTIC_YN` | VARCHAR |  | Indicates whether the antibiotic result is hidden from a user when viewed from within the patient’s chart. |
| 28 | `SENS_UNIT_UOM_ID` | NUMERIC |  | Pointer to the UOM (units of measure master file) record that represents the sensitivity's unit. |
| 29 | `SENS_UNIT_UOM_ID_UNIT_NAME` | VARCHAR |  | Record name |
| 30 | `SENS_METHOD_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 31 | `RESULTING_LAB_ID` | NUMERIC | FK→ | The unique identifier of the resulting agency which is responsible for an antibiotic sensitivity. |
| 32 | `RESULTING_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 33 | `SENS_ACCR_STAT_YN` | VARCHAR |  | This item determines the accreditation status of the corresponding antibiotic. If set to Y-Yes, the corresponding antibiotic is accredited. If set to N-No, the corresponding antibiotic is not accredited. If null, no evaluation was performed on the antibiotic to determine if it is accredited or not. |
| 34 | `SENS_INSTR_CONCEPT_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the sensitivity's resulting instrument at the time of verification. |
| 35 | `LAB_SENS_KEY_IDENT` | VARCHAR |  | Stores a unique test key representing the lab susceptibility test associated with this sensitivity result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `ORGANISM_ID` | [CLARITY_ORGANISM](CLARITY_ORGANISM.md) | sole_pk | high |
| `RESULTING_LAB_ID` | [CLARITY_LLB](CLARITY_LLB.md) | sole_pk | high |

