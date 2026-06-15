# ORDER_RESULTS

> This table contains information on results from clinical system orders. This table extracts only the last Orders (ORD) contact for each ORD record.

**Primary key:** `ORDER_PROC_ID`, `ORD_DATE_REAL`, `LINE`  
**Columns:** 61  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number of each result component within each ordered procedure. |
| 3 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 4 | `ORD_END_DATE_REAL` | FLOAT |  | This is a numeric representation of the end date for each order in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 5 | `RESULT_DATE` | DATETIME |  | The date the technician ran the tests for each order in calendar format. |
| 6 | `COMPONENT_ID` | NUMERIC | shared | The unique ID of each result component for each result. |
| 7 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 8 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for the associated patient encounter. This number is unique across all patients and encounters in the system. |
| 9 | `ORD_VALUE` | VARCHAR |  | The value returned for each result component, in short free text format. NOTE: This is how the data is stored in the database; as string format. Interface data may come in with alpha characters and this field is designed to store exactly what is stored in the database. This field stores numeric and structured numeric values in M internal format, using a period as the decimal separator irrespective of locale. |
| 10 | `ORD_NUM_VALUE` | FLOAT |  | A numeric representation of the value returned for each component where applicable. If the value contains any non-numeric characters, the value will display as 9999999. |
| 11 | `RESULT_FLAG_C_NAME` | VARCHAR | org | The category value associated with a standard HL7 flag code to mark each component result as abnormal. Any value in this field not equal to 1 is considered abnormal. |
| 12 | `REFERENCE_LOW` | VARCHAR |  | The lowest acceptable value for each result component. If the value in this column is a number or structured numeric, the numbers will be stored in M internal format, using a period as the decimal separator. |
| 13 | `REFERENCE_HIGH` | VARCHAR |  | The highest acceptable value for each result component. If the value in this column is a number or structured numeric, the numbers will be stored in M internal format, using a period as the decimal separator. |
| 14 | `REFERENCE_UNIT` | VARCHAR |  | The units for each result component value. |
| 15 | `RESULT_STATUS_C_NAME` | VARCHAR |  | The category value corresponding to the status of each result record, such as 2-Preliminary, 3-Final, 4-Corrected, 5-Incomplete. |
| 16 | `RESULT_SUB_IDN` | VARCHAR |  | This item is populated with the unique organism identifier (OVR 700 or interface) when the component of an order result is an organism and can be joined to ORDER_SENSITIVITY.SENS_ORGANISM_SID to identify details about this organism. |
| 17 | `LAB_STATUS_C_NAME` | VARCHAR |  | The category value associated with the status of each result, such as 1-In Progress, 2-Preliminary, 3-Final, 4-Edited. |
| 18 | `INTERFACE_YN` | VARCHAR |  | This Yes/No flag identifies whether each order was resulted through an interface. The field will display "Y" if the result came through an interface, otherwise the field will display "N". |
| 19 | `RESULTING_LAB_ID` | NUMERIC | FK→ | The Unique ID of the Lab running the test. |
| 20 | `RESULTING_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 21 | `COMPONENT_COMMENT` | VARCHAR |  | Contains the comments associated with a order COMPONENT_ID, i.e. this is the comments associated with a specific order component's results. If comment data is too long to fit in this item, then the comments will be found in the ORDER_RES_COMMENT table. |
| 22 | `RESULT_IN_RANGE_YN` | VARCHAR |  | A Yes/No category value to indicate whether a result has been verified to be within its reference range. This item is set by the interface when the result is sent. A null value is equivalent to a "no" value. |
| 23 | `REF_NORMAL_VALS` | VARCHAR |  | This is a free-text item which allows you to enter a reference range without tying it to a "low" or "high" value. For example, it could be a string ("negative"), a list of choices ("Yellow, orange"), or a descriptive range ("Less than 20"). The values entered in this range should always represent the "normal" values. This item will be displayed in Results Review as the reference range, superseding any values in the low or high items. It may also be displayed in reports, if the print groups are configured to use it. Multiple responses are permitted (one per line). If the value in this column is a number or structured numeric, the numbers will be stored in M internal format using a period as the decimal separator. |
| 24 | `LRR_BASED_ORGAN_ID` | NUMERIC |  | Used for storing discrete organisms. This item is used for storing isolated organisms at the component level. There may be cases where an isolated organism does not undergo sensitivity tests and therefore is only stored at the component level. Organisms with sensitivities are also stored in addition to this item. |
| 25 | `LRR_BASED_ORGAN_ID_NAME` | VARCHAR |  | The name of the organism. |
| 26 | `COMP_RES_TECHNICIA` | VARCHAR |  | ID of the Resulting Lab Technician. |
| 27 | `VALUE_NORMALIZED` | VARCHAR |  | Will contain the structured numeric result value in a delimited structured numeric format. Numbers will be in M internal format. The delimited structured numeric value is the user entered structured numeric value converted to a delimited format. Valid structured numeric formats are range, operator followed by number, and number followed by operator the value stored in this item is of the format: operator1_$c(16)_number1_$c(16)_operator2_$c(16)_number2. |
| 28 | `NUMERIC_PRECISION` | NUMERIC |  | The number of decimal digits to the right of the decimal point. |
| 29 | `COMP_OBS_INST_TM` | DATETIME (Local) |  | Timestamp to track per non-micro result component when it was collected/observed. |
| 30 | `COMP_ANL_INST_TM` | DATETIME (Local) |  | Timestamp to track per non-micro result component when it was analyzed in lab. |
| 31 | `RESULT_VAL_START_LN` | INTEGER |  | For multi-line results holds the starting line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin. This column is simply an indicator of the line number(s) where a result is stored. |
| 32 | `RESULT_VAL_END_LN` | INTEGER |  | For multi-line results holds the ending line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin. This column is simply an indicator of the line number(s) where a result is stored. |
| 33 | `RESULT_CMT_START_LN` | INTEGER |  | For multi-line results holds the starting line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin. This column is simply an indicator of the line number(s) where a result is stored. |
| 34 | `RESULT_CMT_END_LN` | INTEGER |  | For multi-line results holds the ending line number of RESULTS_CMT column from ORDER_RES_COMMENT table, where the result values begin. This column is simply an indicator of the line number(s) where a result is stored. |
| 35 | `ORD_RAW_VALUE` | VARCHAR |  | Stores the raw value of a numeric result as entered by the user. The value stored here and in column ORD_VALUE will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because ORD_VALUE will store numeric values in the M internal format. |
| 36 | `RAW_LOW` | VARCHAR |  | Stores raw value of the minimum value of the result component mentioned in column REFERENCE_LOW. The value stored here and in REFERENCE_LOW will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because REFERENCE_LOW will store numeric data in M internal format. |
| 37 | `RAW_HIGH` | VARCHAR |  | Stores raw value of the maximum value of the result component mentioned in column REFERENCE_HIGH. The value stored here and in REFERENCE_HIGH will be different in international locales for numeric data if the decimal separator used in that locale is a comma instead of a period. This is because REFERENCE_HIGH will store numeric data in M internal format. |
| 38 | `RAW_REF_VALS` | VARCHAR |  | This column stores the raw value of REF_NORMAL_VALS (i.e. the reference normal values of the result component). Since REF_NORMAL_VALS will store numeric data in M internal format, the value stored here and in REF_NORMAL_VALS will be different in international locales if the decimal separator used in that locale is a comma instead of a period. |
| 39 | `ORGANISM_QUANTITY` | VARCHAR |  | This item is used for storing isolated organisms at the component level. It contains the numeric or qualitative quantity of the organism that was observed. |
| 40 | `ORGANISM_QUANTITY_UNIT` | VARCHAR |  | This item is used for storing isolated organisms at the component level. It contains the unit associated with the quantity of the organism that was observed. |
| 41 | `COMPON_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 42 | `COMPON_LNC_SRC_C_NAME` | VARCHAR |  | Source of the component Logical Observation Identifiers Names and Codes (LOINC) ID. |
| 43 | `COMP_SNOMED_SRC_C_NAME` | VARCHAR |  | Source of the Systemized Nomenclature of Medicine – Clinical Terms (SNOMED) code (reported vs inferred). |
| 44 | `REF_UNIT_UOM_ID` | NUMERIC |  | Pointer to the record that represents the component's units of measure. |
| 45 | `REF_UNIT_UOM_ID_UNIT_NAME` | VARCHAR |  | Record name |
| 46 | `REF_RANGE_TYPE` | VARCHAR |  | Displays the type of the reference range. |
| 47 | `ORGANISM_SNOMED_CT` | VARCHAR |  | The Systemized Nomenclature of Medicine – Clinical Terms (SNOMED) code for the component's organism. |
| 48 | `ORGANISM_QUANTITY_SNOMED_CT` | VARCHAR |  | The Systemized Nomenclature of Medicine – Clinical Terms (SNOMED) code for the component's organism quantity. |
| 49 | `PERFORMING_ORG_INFO_LINE` | INTEGER |  | This is used to indicate the performing organization information for the component. This item stores the line number of the ORD related group which is used to save the performing organization information. |
| 50 | `COMPON_EXCL_CDS_YN` | VARCHAR |  | To cache if the component has a value or comment that matches a value in Excluded result text (I LSD 768). |
| 51 | `RTF_VAL_START_LINE` | INTEGER |  | If the component result value is rich text, this column gives the first line of ORD_RTF_VAL_CMT that the value is stored in. |
| 52 | `RTF_VAL_END_LINE` | INTEGER |  | If the component result value is rich text, this column gives the last line of ORD_RTF_VAL_CMT that the value is stored in. |
| 53 | `RTF_CMT_START_LINE` | INTEGER |  | If the component comment is rich text, this column gives the first line of ORD_RTF_VAL_CMT that the component comment is stored in. |
| 54 | `RTF_CMT_END_LINE` | INTEGER |  | If the component comment is rich text, this column gives the last line of ORD_RTF_VAL_CMT that the component comment is stored in. |
| 55 | `RSLT_ACCR_FLAG_YN` | VARCHAR |  | This item determines the accreditation status of the corresponding component. If set to Y-Yes, the corresponding component is accredited. If set to N-No, the corresponding component is not accredited. If null, no evaluation was performed on the component to determine if it is accredited or not. |
| 56 | `SIGNATURE_START_LN` | INTEGER |  | Gives the first line of I ORD 2090 that signatures for the related component are stored in |
| 57 | `SIGNATURE_END_LN` | INTEGER |  | Gives the last line of I ORD 2090 that signatures for the related component are stored in |
| 58 | `RES_INSTR_CONCEPT_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the component's resulting instrument at the time of verification. |
| 59 | `RESULT_TREND_C_NAME` | VARCHAR |  | Trend status for the common name at the time logged in I ORD 2057 - Result Trend Audit Instant. |
| 60 | `RESULT_TREND_UTC_DTTM` | DATETIME (UTC) |  | Instant trend status (I ORD 2056) was set. |
| 61 | `RESULT_TREND_NAME` | VARCHAR |  | Common name for which trend status (I ORD 2056) was calculated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `RESULTING_LAB_ID` | [CLARITY_LLB](CLARITY_LLB.md) | sole_pk | high |

