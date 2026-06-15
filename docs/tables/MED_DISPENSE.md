# MED_DISPENSE

> This table contains information about a patient's med dispense history from a third-party interface. This information can be helpful for reviewing whether a patient is getting their prescriptions filled at the correct intervals.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 54  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EXT_DRUG_DESP` | VARCHAR |  | This column stores the drug description in free text. |
| 6 | `EXT_MED_REF_ID` | VARCHAR |  | This column stores a reference identifier associated with each medication dispense. |
| 7 | `EXT_DRUD_ID_STR` | VARCHAR |  | This column stores the identifier of the drug. |
| 8 | `EXT_MED_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 9 | `EXT_DRUG_CODE_SYS` | VARCHAR |  | This column stores the coding system used for the drug identifier. |
| 10 | `EXT_DRUG_DISP_INST_DTTM` | DATETIME (Local) |  | This column stores the dispense instant. |
| 11 | `EXT_DRUG_DISP_AMT` | INTEGER |  | This column stores the actual dispense amount of the drug. |
| 12 | `EXT_DRUG_DISP_UNIT` | VARCHAR |  | This column stores the drug dispense unit ID. |
| 13 | `EXT_DRUG_UNIT_TXT` | VARCHAR |  | This column stores the free text name of the dispense unit. |
| 14 | `EXT_DRUG_DOSE_FORM` | VARCHAR |  | This column stores the drug dosage form when dispensed. |
| 15 | `EXT_DRUG_RX_NUM` | VARCHAR |  | This column stores the prescription number of the dispense. |
| 16 | `EXT_DRUG_DSPPROV_ID` | NUMERIC |  | This column stores the dispensing provider ID. |
| 17 | `EXT_DRUG_DSPPROV_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 18 | `EXT_DRUG_PROV_NAME` | VARCHAR |  | The dispensing provider name for the external dispense. |
| 19 | `EXT_DRUG_UNIT_STR` | VARCHAR |  | This column stores the actual unit strength. |
| 20 | `EXT_DRUG_PHAR_PHON` | VARCHAR |  | The pharmacy phone (or other contact) number associated with the external dispense. |
| 21 | `EXT_MED_DAY_SUPPLY` | INTEGER |  | This column stores the number of days the dispense is written for. |
| 22 | `EXT_MED_ORDPROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `EXT_MED_ORD_PROVNAM` | VARCHAR |  | The name of the ordering provider for this medication. |
| 24 | `EXT_MED_ENT_ORG_NAM` | VARCHAR |  | This column stores the entering organization name of the dispense data. |
| 25 | `EXT_MED_ORD_ID` | NUMERIC |  | This column stores the linked order ID for the corresponding order record in Epic, if one exists. |
| 26 | `EXT_MED_DISP_UNT_C_NAME` | VARCHAR | org | The mapped dose unit category ID for the external dispense. |
| 27 | `EXT_MED_DAW_YN` | VARCHAR |  | Indicates whether the external dispense is marked to dispense as written. 'Y' indicates that the external dispense is marked to dispense as written. 'N' or NULL indicate that the external dispense is not marked to dispense as written. |
| 28 | `EXT_MED_REFILLS` | VARCHAR |  | This stores the original refills for an external dispense. |
| 29 | `EXT_MED_REF_REMAIN` | VARCHAR |  | This stores the refills remaining for an external dispense. |
| 30 | `EXT_MED_QUAN_REMAIN` | INTEGER |  | This stores the remaining quantity for an external dispense. |
| 31 | `EXT_MED_QUAN_REM_C_NAME` | VARCHAR |  | This stores the remaining quantity unit for an external dispense. |
| 32 | `EXT_MED_MSG_TYPE_C_NAME` | VARCHAR |  | The data source category ID for the external dispense. |
| 33 | `EXT_MED_PRI_AUTH` | VARCHAR |  | This stores the prior authorization number for an external dispense. |
| 34 | `EXT_MED_DOSE` | VARCHAR |  | Stores the discrete dose value for a dispense. |
| 35 | `EXT_MED_DOSE_UNIT_C_NAME` | VARCHAR |  | Stores the dose unit category ID for a dispense. |
| 36 | `EXT_MED_FREQ_ID` | VARCHAR |  | The unique ID of the frequency type for the external dispense. |
| 37 | `EXT_MED_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 38 | `EXT_MED_ROUTE_C_NAME` | VARCHAR | org | Stores the category ID of the route of a dispense. |
| 39 | `EXT_MED_HIST_C_NAME` | VARCHAR |  | The historical status category ID for the external dispense. |
| 40 | `WRITTEN_DATE` | DATETIME |  | This item holds the written date for a dispense. |
| 41 | `EXT_MED_SRC_DXR_CSN` | NUMERIC |  | This item stores the contact serial number (CSN) for the Document Received record that contains the external dispense information. |
| 42 | `DISP_FILTER_RSN_C_NAME` | VARCHAR |  | Stores the reason why an external dispense should be filtered from the composite record |
| 43 | `EXT_MED_FILL_STAT_C_NAME` | VARCHAR | org | The status of this fill for the external dispense. |
| 44 | `EXT_MED_FILL_REF_NUM` | VARCHAR |  | The external reference number identifying this dispense. |
| 45 | `EXT_MED_FILL_NOTE` | VARCHAR |  | The note from the external system about this fill. |
| 46 | `EXT_MED_MIXTURE_FORM_C_NAME` | VARCHAR | org | The mixture form for this dispense row. |
| 47 | `EXT_MED_MAX_DLY_DOSE` | VARCHAR |  | Stores the maximum daily dose value for a dispense |
| 48 | `EXT_MED_MAX_DLY_DOSE_QTYUNIT_C_NAME` | VARCHAR |  | Stores the maximum daily dose unit category ID for a dispense |
| 49 | `EXT_MED_PRN_CMT` | VARCHAR |  | Stores the PRN comment for a PRN dispense |
| 50 | `EXT_DRUG_DSPPROV_ZIP` | VARCHAR |  | This item stores the postal code of the pharmacy or provider that dispensed the medication. This item is only populated in Cosmos host environments. |
| 51 | `EXT_DRUG_DISP_INST_UTC_DTTM` | DATETIME (UTC) |  | This column stores the dispense instant in UTC. Assumes system local time if dispense does not have timezone. |
| 52 | `DISP_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 53 | `DISP_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 54 | `EXT_DRUG_SOLD_DATE` | DATETIME |  | This item stores the sold date of an external dispense. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

